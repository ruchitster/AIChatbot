export default function MessageBubble({ message }) {
  const isUser = message.role === "user";

  const copyText = () => {
    navigator.clipboard.writeText(message.content);
  };

  return (
    <div className={`message ${isUser ? "user" : "assistant"} fade`}>
      <div className="bubble">

        {/* ACTIONS */}
        <div className="actions">
          <button onClick={copyText}>Copy</button>
        </div>

        {message.content}
      </div>
    </div>
  );
}