from app.rag.vector_db import collection
from app.rag.embedder import get_embedding


def add_document(doc_id: str, text: str):

    embedding = get_embedding(text)

    collection.add(
        ids=[doc_id],
        embeddings=[embedding],
        documents=[text]
    )