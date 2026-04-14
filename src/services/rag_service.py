"""Service for ChromaDB retrieval (RAG)."""

from typing import Any, Dict

from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import Chroma

from src.config.settings import EmbeddingsConfig


class SentenceTransformerEmbedding:
    """Wrapper for sentence transformers to work with Chroma."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Embed multiple documents."""
        return self.model.encode(texts, convert_to_tensor=False).tolist()

    def embed_query(self, text: str) -> list[float]:
        """Embed a single query."""
        return self.model.encode(text, convert_to_tensor=False).tolist()


class RAGService:
    """Handles vector database setup and context retrieval."""

    def __init__(self):
        self.embedding = None
        self.vectordb = None
        self._initialize_vector_db()

    def _initialize_vector_db(self) -> None:
        """Initialize embeddings and Chroma with a fallback model strategy."""
        try:
            self.embedding = SentenceTransformerEmbedding(
                model_name=EmbeddingsConfig.MODEL_NAME
            )

            self.vectordb = Chroma(
                persist_directory=EmbeddingsConfig.PERSIST_DIRECTORY,
                embedding_function=self.embedding,
            )
        except Exception:
            try:
                self.embedding = SentenceTransformerEmbedding(
                    model_name="all-MiniLM-L6-v2"
                )

                self.vectordb = Chroma(
                    persist_directory=EmbeddingsConfig.PERSIST_DIRECTORY,
                    embedding_function=self.embedding,
                )
            except Exception:
                self.embedding = None
                self.vectordb = None

    def retrieve_context(self, question: str, k: int = EmbeddingsConfig.DEFAULT_K) -> str:
        """Retrieve top-k similar chunks from Chroma for the given question."""
        if self.vectordb is None:
            return ""

        try:
            results = self.vectordb.similarity_search(question, k=k)
            return "\n\n".join([doc.page_content for doc in results])
        except Exception as exc:
            return f"Error retrieving context: {str(exc)}"

    def get_database_stats(self) -> Dict[str, Any]:
        """Return basic vector database connectivity details."""
        if self.vectordb is None:
            return {"status": "Unavailable", "error": "Vector DB not initialized"}

        try:
            collection = self.vectordb._collection
            return {
                "collection_name": collection.name if hasattr(collection, "name") else "Unknown",
                "status": "Connected",
            }
        except Exception as exc:
            return {"status": "Error", "error": str(exc)}


rag_service = RAGService()
