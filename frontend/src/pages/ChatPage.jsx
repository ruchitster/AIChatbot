import { useState, useEffect, useRef } from "react";
import { sendMessage } from "../services/chatService";

import MessageBubble from "../components/MessageBubble";
import Loader from "../components/Loader";

export default function ChatPage() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  const handleSend = async () => {
    if (!message.trim()) return;

    const userMessage = {
      id: Date.now(),
      role: "user",
      content: message,
    };

    setMessages((prev) => [...prev, userMessage]);

    const currentMessage = message;
    setMessage("");

    try {
      setLoading(true);

      const response = await sendMessage(
        currentMessage
      );

      const aiMessage = {
        id: Date.now() + 1,
        role: "assistant",
        content: response.reply,
      };

      setMessages((prev) => [
        ...prev,
        aiMessage,
      ]);
    } catch (error) {
      console.error(
        "Chat Error:",
        error
      );
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  return (
    <div
      style={{
        maxWidth: "900px",
        margin: "auto",
        padding: "20px",
      }}
    >
      {/* DEBUG TEST */}
      <h1
        style={{
          color: "red",
          fontSize: "40px",
        }}
      >
        TEST PAGE 123
      </h1>

      {/* Upload Placeholder */}
      <div
        style={{
          border: "2px solid red",
          padding: "15px",
          marginBottom: "20px",
          borderRadius: "10px",
        }}
      >
        Upload Area Test
      </div>

      {/* Chat Box */}
      <div
        style={{
          height: "600px",
          overflowY: "auto",
          border: "1px solid #ddd",
          padding: "15px",
          borderRadius: "10px",
        }}
      >
        {messages.map((msg) => (
          <MessageBubble
            key={msg.id}
            message={msg}
          />
        ))}

        {loading && <Loader />}

        <div ref={bottomRef} />
      </div>

      {/* Input Box */}
      <div
        style={{
          marginTop: "10px",
          display: "flex",
          gap: "10px",
        }}
      >
        <input
          value={message}
          onChange={(e) =>
            setMessage(e.target.value)
          }
          onKeyDown={handleKeyDown}
          placeholder="Type a message..."
          style={{
            flex: 1,
            padding: "12px",
          }}
        />

        <button onClick={handleSend}>
          Send
        </button>
      </div>
    </div>
  );
}