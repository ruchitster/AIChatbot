import uuid

from qdrant_client.models import PointStruct

from app.services.qdrant_service import client

COLLECTION_NAME = "documents"


def save_vector(
    vector,
    document_id,
    chunk_text
):

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={
                    "document_id": document_id,
                    "chunk": chunk_text
                }
            )
        ]
    )