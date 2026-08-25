from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

from app.config import get_settings


def get_retriever():
    settings = get_settings()

    embeddings = OpenAIEmbeddings(
        model=settings.embedding_model,
        api_key=settings.openai_api_key,
    )

    vectorstore = QdrantVectorStore.from_existing_collection(
        embedding=embeddings,
        url=settings.qdrant_url,
        api_key=settings.qdrant_api_key,
        collection_name=settings.qdrant_collection_name,
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": settings.retrieval_k,
        }
    )

    return retriever
