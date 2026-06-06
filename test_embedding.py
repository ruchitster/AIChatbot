from google import genai

from app.core.config import GEMINI_API_KEY

client = genai.Client(
    api_key=GEMINI_API_KEY
)

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents="Ruchit is building a RAG chatbot"
)

embedding = result.embeddings[0].values

print("Vector Length:", len(embedding))