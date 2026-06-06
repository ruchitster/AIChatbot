export function createMessage(role, content) {
  return {
    id: Date.now(),
    role,
    content,
  };
}