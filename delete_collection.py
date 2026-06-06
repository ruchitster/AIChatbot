from app.services.qdrant_service import client

client.delete_collection("documents")

print("Collection deleted")