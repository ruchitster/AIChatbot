from qdrant_client.models import (
    VectorParams,
    Distance
)

from app.services.qdrant_service import client

COLLECTION_NAME = "documents"

try:
    client.delete_collection(
        collection_name=COLLECTION_NAME
    )
    print("Collection deleted")
except Exception as e:
    print("Delete:", e)

client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(
        size=3072,
        distance=Distance.COSINE
    )
)

print("Collection recreated")