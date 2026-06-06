import { useState } from "react";
import { handleStreamMessage } from "../controllers/chatController";

export default function ChatView() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  return (
    <div style={styles.container}>
      <h2>AI RAG Chat System 🤖</h2>

      {/* CHAT WINDOW */}
      <div style={styles.chatBox}>
        {chat.map((c, i) => (
          <div
            key={i}
            style={{
              ...styles.message,
              alignSelf: c.role === "user" ? "flex-end" : "flex-start",
              backgroundColor: c.role === "user" ? "#DCF8C6" : "#F1F0F0",
            }}
          >
            <b>{c.role}:</b> {c.text}
          </div>
        ))}
      </div>

      {/* INPUT BOX */}
      <div style={styles.inputBox}>
        <input
          style={styles.input}
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Ask something..."
        />

        <button
          style={styles.button}
          onClick={() => {
            if (!message.trim()) return;

            handleStreamMessage(message, setChat);
            setMessage("");
          }}
        >
          Send
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    maxWidth: 600,
    margin: "40px auto",
    fontFamily: "Arial",
  },
  chatBox: {
    border: "1px solid #ddd",
    padding: 10,
    height: 400,
    overflowY: "auto",
    display: "flex",
    flexDirection: "column",
    gap: 10,
    marginBottom: 10,
  },
  message: {
    padding: 10,
    borderRadius: 10,
    maxWidth: "70%",
  },
  inputBox: {
    display: "flex",
    gap: 10,
  },
  input: {
    flex: 1,
    padding: 10,
    borderRadius: 5,
    border: "1px solid #ccc",
  },
  button: {
    padding: "10px 20px",
    cursor: "pointer",
  },
};