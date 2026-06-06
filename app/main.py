from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from app.routes.chat_routes import router as chat_router
from app.routes.upload_routes import router as upload_router

# Load environment variables
load_dotenv()

app = FastAPI()

# Get frontend URL from .env
FRONTEND_URL = os.getenv("FRONTEND_URL")

# Base CORS origins (local dev)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

# Add production frontend URL if available
if FRONTEND_URL:
    origins.append(FRONTEND_URL)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(chat_router)
app.include_router(upload_router)