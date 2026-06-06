from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.search import search
from app.services.chat_memory import save_message, get_last_messages
from app.services.gemini_service import call_gemini

router = APIRouter()


class ChatRequest(BaseModel):
    session_id: str
    message: str


@router.post("/chat")
def chat(data: ChatRequest):

    save_message(
        data.session_id,
        "user",
        data.message
    )

    history = get_last_messages(
        data.session_id,
        limit=10
    )

    rag_context = search(
        data.message
    )

    prompt = """
You are a helpful AI assistant.

Answer ONLY using the provided Knowledge Base.

If the answer is not present in the Knowledge Base,
reply:

"I could not find that information in the uploaded documents."

Conversation History:
"""

    for msg in history:
        prompt += f"{msg.Role}: {msg.Message}\n"

    prompt += f"""

Knowledge Base:
{rag_context}

Question:
{data.message}
"""

    reply = call_gemini(prompt)

    save_message(
        data.session_id,
        "assistant",
        reply
    )

    return {"reply": reply}