from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DB_SERVER, DB_NAME, DB_USER, DB_PASSWORD, DB_DRIVER

DATABASE_URL = (
    "mssql+pyodbc:///?odbc_connect="
    f"DRIVER={{{DB_DRIVER}}};"
    f"SERVER={DB_SERVER};"
    f"DATABASE={DB_NAME};"
    f"UID={DB_USER};"
    f"PWD={DB_PASSWORD};"
    "Encrypt=no;"
    "TrustServerCertificate=yes;"
)

engine = create_engine(DATABASE_URL, fast_executemany=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)