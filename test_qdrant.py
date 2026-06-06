from app.services.qdrant_service import client

collections = client.get_collections()

for c in collections.collections:
    print(c.name)