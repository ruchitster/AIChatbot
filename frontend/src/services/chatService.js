import api from "../api/chatApi";
import { getSessionId } from "../utils/session";

export const sendMessage = async (message) => {
  const res = await api.post("/chat", {
    message,
    session_id: getSessionId(),
  });

  return res.data;
};