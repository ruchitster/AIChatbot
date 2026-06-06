from qdrant_client import QdrantClient

from app.core.config import (
    QDRANT_URL,
    QDRANT_API_KEY
)

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)