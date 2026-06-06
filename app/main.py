from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.chat_routes import router as chat_router
from app.routes.upload_routes import router as upload_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-chatbot-nu-neon.vercel.app",
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(upload_router)