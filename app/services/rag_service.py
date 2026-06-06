from datetime import datetime

from app.rag.retriever import search
from app.services.gemini_service import call_gemini

from app.memory.session_store import (
    get_history,
    add_message
)


def rag_chat(
    message: str,
    session_id: str
):

    msg = message.lower()

    if "today" in msg and (
        "date" in msg or
        "day" in msg
    ):
        return {
            "reply":
            datetime.now().strftime(
                "%A, %d %B %Y"
            )
        }

    if "time" in msg:
        return {
            "reply":
            datetime.now().strftime(
                "%H:%M:%S"
            )
        }

    try:
        context = search(message)

    except Exception:
        context = "No documents uploaded yet."

    history = get_history(
        session_id
    )

    conversation = ""

    for item in history:

        conversation += (
            f"{item['role']}: "
            f"{item['content']}\n"
        )

    prompt = f"""
You are a helpful AI assistant.

Conversation History:
{conversation}

Context:
{context}

User:
{message}
"""

    response = call_gemini(prompt)

    try:

        answer = (
            response["candidates"][0]
            ["content"]["parts"][0]
            ["text"]
        )

        add_message(
            session_id,
            "user",
            message
        )

        add_message(
            session_id,
            "assistant",
            answer
        )

    except Exception:
        pass

    return response