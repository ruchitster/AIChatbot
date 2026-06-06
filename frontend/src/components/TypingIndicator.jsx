export default function TypingIndicator() {
  return (
    <div style={{ display: "flex", gap: "4px", padding: "10px" }}>
      <span className="dot">●</span>
      <span className="dot">●</span>
      <span className="dot">●</span>

      <style>
        {`
          .dot {
            animation: blink 1.4s infinite;
            font-size: 18px;
            opacity: 0.3;
          }

          .dot:nth-child(2) { animation-delay: 0.2s; }
          .dot:nth-child(3) { animation-delay: 0.4s; }

          @keyframes blink {
            0%, 80%, 100% { opacity: 0.2; }
            40% { opacity: 1; }
          }
        `}
      </style>
    </div>
  );
}