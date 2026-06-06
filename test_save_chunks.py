from app.rag.pdf_parser import extract_pdf_text
from app.rag.chunker import chunk_text

from app.services.document_service import (
    save_document,
    save_chunk
)

# Create document record
document_id = save_document(
    "Ruchit.pdf",
    "pdf"
)

print("Document ID:", document_id)

# Extract text
text = extract_pdf_text(
    "uploads/Ruchit.pdf"
)

# Chunk text
chunks = chunk_text(
    text,
    chunk_size=500,
    overlap=50
)

print("Chunks:", len(chunks))

# Save chunks
for chunk in chunks:

    save_chunk(
        document_id,
        chunk
    )

print("Chunks saved successfully")