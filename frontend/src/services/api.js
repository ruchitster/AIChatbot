const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export const streamMessage = async (message, onChunk) => {
  const response = await fetch(`${API_BASE_URL}/chat-stream`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  });

  const reader = response.body.getReader();
  const decoder = new TextDecoder("utf-8");

  let result = "";

  while (true) {
    const { value, done } = await reader.read();
    if (done) break;

    const chunk = decoder.decode(value);
    result += chunk;

    onChunk(result);
  }
};