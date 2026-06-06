import os
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

FAISS_PATH = "faiss_index"


def get_retriever():

    if not os.path.exists(FAISS_PATH):
        return None

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    return FAISS.load_local(
        FAISS_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )


def search(query: str):

    db = get_retriever()

    if db is None:
        return []

    docs = db.similarity_search(query, k=3)

    return [doc.page_content for doc in docs]