from app.rag.pdf_parser import extract_pdf_text

text = extract_pdf_text(
    "uploads/Ruchit.pdf"
)

print(text)