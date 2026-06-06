from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import os

from app.rag.pdf_parser import extract_pdf_text
from app.rag.image_parser import extract_image_text
from app.rag.chunker import chunk_text
from app.rag.embeddings import create_embedding
from app.rag.qdrant_store import save_vector

from app.services.document_service import (
    save_document,
    save_chunk
)

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/upload")
async def upload_files(
    files: list[UploadFile] = File(...)
):

    uploaded_docs = []

    for file in files:

        file_path = os.path.join(
            UPLOAD_DIR,
            file.filename
        )

        # Save file
        with open(
            file_path,
            "wb"
        ) as buffer:

            buffer.write(
                await file.read()
            )

        # Extract text
        if file.content_type == "application/pdf":

            text = extract_pdf_text(
                file_path
            )

        elif file.content_type.startswith(
            "image/"
        ):

            text = extract_image_text(
                file_path
            )

        else:

            continue

        # Chunk text
        chunks = chunk_text(
            text,
            chunk_size=800,
            overlap=150
        )

        # Save document
        document_id = save_document(
            file.filename,
            file.content_type
        )

        # Save chunks + vectors
        for chunk in chunks:

            save_chunk(
                document_id,
                chunk
            )

            vector = create_embedding(
                chunk
            )

            save_vector(
                vector,
                document_id,
                chunk
            )

        uploaded_docs.append({
            "document_id": document_id,
            "filename": file.filename,
            "chunks": len(chunks)
        })

    return {
        "success": True,
        "documents": uploaded_docs
    }