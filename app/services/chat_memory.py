from sqlalchemy import text
from app.db.database import SessionLocal


def save_message(session_id, role, message):
    db = SessionLocal()

    query = text("""
        INSERT INTO ChatMessages (SessionId, Role, Message)
        VALUES (:session_id, :role, :message)
    """)

    db.execute(query, {
        "session_id": session_id,
        "role": role,
        "message": message
    })

    db.commit()
    db.close()


def get_last_messages(session_id, limit=10):
    db = SessionLocal()

    query = text("""
        SELECT TOP (:limit) Role, Message
        FROM ChatMessages
        WHERE SessionId = :session_id
        ORDER BY Id DESC
    """)

    result = db.execute(query, {
        "session_id": session_id,
        "limit": limit
    }).fetchall()

    db.close()

    return result[::-1]