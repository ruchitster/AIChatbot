import { useState, useEffect, useRef } from "react";
import { sendMessage } from "../services/chatService";
import { createMessage } from "../models/chatModel";

export default function useChatController() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const bottomRef = useRef(null);

  // load history
  useEffect(() => {
    const saved = localStorage.getItem("chat_history");
    if (saved) setMessages(JSON.parse(saved));
  }, []);

  // persist + scroll
  useEffect(() => {
    localStorage.setItem("chat_history", JSON.stringify(messages));
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const send = async () => {
    if (!input.trim()) return;

    const userMsg = createMessage("user", input);
    setMessages((prev) => [...prev, userMsg]);

    const currentInput = input;
    setInput("");
    setLoading(true);

    try {
      const res = await sendMessage(currentInput);

      const botMsg = createMessage("assistant", res.reply);

      setMessages((prev) => [...prev, botMsg]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        createMessage("assistant", "Something went wrong."),
      ]);
    } finally {
      setLoading(false);
    }
  };

  return {
    messages,
    input,
    setInput,
    loading,
    send,
    bottomRef,
  };
}