from sqlalchemy import text
from app.db.database import engine


def save_document(filename, filetype):

    query = text("""
        INSERT INTO Documents
        (
            FileName,
            FileType
        )
        OUTPUT INSERTED.Id
        VALUES
        (
            :filename,
            :filetype
        )
    """)

    with engine.begin() as conn:

        result = conn.execute(
            query,
            {
                "filename": filename,
                "filetype": filetype
            }
        )

        return result.scalar()



def save_chunk(
    document_id,
    chunk_text
):

    query = text("""
        INSERT INTO DocumentChunks
        (
            DocumentId,
            ChunkText
        )
        VALUES
        (
            :document_id,
            :chunk_text
        )
    """)

    with engine.begin() as conn:

        conn.execute(
            query,
            {
                "document_id": document_id,
                "chunk_text": chunk_text
            }
        )