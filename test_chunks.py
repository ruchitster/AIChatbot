from app.rag.pdf_parser import extract_pdf_text
from app.services.chunk_service import create_chunks

text = extract_pdf_text(
    "uploads/Ruchit.pdf"
)

chunks = create_chunks(text)

print("Chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print("\nCHUNK", i + 1)
    print(chunk[:200])