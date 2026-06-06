import time
from app.services.rag_service import rag_chat

def stream_chat(message: str):

    response = rag_chat(message)

    # SAFETY: handle both dict and string
    if isinstance(response, str):
        text = response
    else:
        text = (
            response.get("candidates", [{}])[0]
            .get("content", {})
            .get("parts", [{}])[0]
            .get("text", "")
        )

    # SAFETY: if empty response
    if not text:
        text = "No response generated"

    for word in text.split():
        yield word + " "
        time.sleep(0.03)