from app.rag.pdf_parser import extract_pdf_text
from app.rag.chunker import chunk_text

text = extract_pdf_text(
    "uploads/Ruchit.pdf"
)

chunks = chunk_text(
    text,
    chunk_size=500,
    overlap=50
)

print("Total Chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print("\n================")
    print("CHUNK", i + 1)
    print("================")
    print(chunk)