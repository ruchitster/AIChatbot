from app.services.rag_service import rag_chat

def chat_controller(message: str):
    return rag_chat(message)