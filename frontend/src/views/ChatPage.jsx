import { useState, useEffect, useRef } from "react";
import { sendMessage } from "../services/chatService";
import MessageBubble from "../components/MessageBubble";
import FileUpload from "../components/FileUpload";
import TypingIndicator from "../components/TypingIndicator";
import "../styles/chatgpt.css";

export default function ChatPage() {
  const [chats, setChats] = useState([]);
  const [activeChatId, setActiveChatId] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  // ✅ NEW: error state for upload/chat UI messages
  const [error, setError] = useState("");

  const bottomRef = useRef(null);

  useEffect(() => {
    const saved = localStorage.getItem("chat_app");

    if (saved) {
      const data = JSON.parse(saved);
      setChats(data.chats || []);
      setActiveChatId(data.activeChatId || data.chats?.[0]?.id || null);
    } else {
      setChats([]);
      setActiveChatId(null);
    }
  }, []);

  const createChat = () => {
    const chat = {
      id: Date.now().toString(),
      title: `New Chat ${chats.length + 1}`,
      messages: [],
    };

    setChats((prev) => [chat, ...prev]);
    setActiveChatId(chat.id);
  };

  const deleteChat = (id) => {
    const updated = chats.filter((c) => c.id !== id);

    if (!updated.length) {
      setChats([]);
      setActiveChatId(null);
      return;
    }

    setChats(updated);

    if (activeChatId === id) {
      setActiveChatId(updated[0].id);
    }
  };

  const activeChat = chats.find((c) => c.id === activeChatId);

  const handleSend = async () => {
    if (!message.trim()) return;

    const userMsg = {
      id: Date.now(),
      role: "user",
      content: message,
    };

    setChats((prev) =>
      prev.map((c) =>
        c.id === activeChatId
          ? { ...c, messages: [...c.messages, userMsg] }
          : c
      )
    );

    const text = message;
    setMessage("");
    setLoading(true);

    try {
      const res = await sendMessage(text);

      const aiMsg = {
        id: Date.now() + 1,
        role: "assistant",
        content: res.reply,
      };

      setChats((prev) =>
        prev.map((c) =>
          c.id === activeChatId
            ? { ...c, messages: [...c.messages, aiMsg] }
            : c
        )
      );
    } catch (err) {
      console.error(err);
      setError("❌ Failed to send message");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">

      {/* SIDEBAR */}
      <div className="sidebar">
        <button className="new-chat-btn" onClick={createChat}>
          + New Chat
        </button>

        {chats.map((chat) => (
          <div key={chat.id} className="chat-item">
            <div
              onClick={() => setActiveChatId(chat.id)}
              style={{ flex: 1 }}
            >
              {chat.title}
            </div>

            <button onClick={() => deleteChat(chat.id)}>
              ✕
            </button>
          </div>
        ))}
      </div>

      {/* MAIN */}
      <div className="main">

        <div className="header">
          ChatGPT Clone (RAG)
        </div>

        {/* ✅ ERROR BANNER */}
        {error && (
          <div className="error-banner">
            {error}
          </div>
        )}

        <div className="messages">
          {activeChat?.messages?.map((m) => (
            <MessageBubble key={m.id} message={m} />
          ))}

          {loading && <TypingIndicator />}

          <div ref={bottomRef} />
        </div>

        {/* INPUT BAR */}
        <div className="input-bar">

          {/* ✅ File Upload with error handling */}
          <FileUpload setError={setError} />

          <input
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
            placeholder="Message..."
          />

          <button onClick={handleSend}>➤</button>
        </div>
      </div>
    </div>
  );
}