from app.services.qdrant_service import client

info = client.get_collection("documents")

print("Points:", info.points_count)