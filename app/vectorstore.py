from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

from app.config import get_settings


def create_vectorstore(documents):
    settings = get_settings()

    embeddings = OpenAIEmbeddings(
        model=settings.embedding_model,
        api_key=settings.openai_api_key,
    )

    vectorstore = QdrantVectorStore.from_documents(
        documents=documents,
        embedding=embeddings,
        url=settings.qdrant_url,
        api_key=settings.qdrant_api_key,
        collection_name=settings.qdrant_collection_name,
    )

    return vectorstore
