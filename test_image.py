from app.rag.image_parser import extract_image_text

text = extract_image_text(
    "uploads/sample.png"
)

print(text)