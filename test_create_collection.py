from qdrant_client import models
from app.services.qdrant_service import client

client.create_collection(
    collection_name="documents",
    vectors_config=models.VectorParams(
        size=3072,
        distance=models.Distance.COSINE
    )
)

print("Collection created")