# test_qdrant_insert.py

from app.rag.embeddings import create_embedding
from app.rag.qdrant_store import save_vector

text = "Ruchit knows React, Node.js and SQL Server"

vector = create_embedding(text)

save_vector(
    vector,
    1,
    text
)

print("Vector saved successfully")