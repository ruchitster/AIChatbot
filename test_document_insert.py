from app.services.document_service import save_document

doc_id = save_document(
    "Ruchit.pdf",
    "pdf"
)

print("Document ID:", doc_id)