from app.services.rag_service import rag_chat

response = rag_chat("hello")

print("TYPE:", type(response))
print("RESPONSE:")
print(response)