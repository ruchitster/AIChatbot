from app.rag.embeddings import create_embedding
from app.services.qdrant_service import client

COLLECTION_NAME = "documents"


def search(query: str):

    query_vector = create_embedding(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=3
    )

    chunks = []

    for point in results.points:
        chunks.append(
            point.payload["chunk"]
        )

    return "\n\n".join(chunks)