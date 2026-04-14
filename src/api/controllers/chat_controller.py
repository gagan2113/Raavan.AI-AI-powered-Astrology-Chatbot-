"""Controller logic for chat API endpoint."""

from src.api.schemas.chat_schema import ChatRequest, ChatResponse
from src.services.llm_service import llm_service
from src.services.rag_service import rag_service


def handle_chat(request: ChatRequest) -> ChatResponse:
    """Generate a Raavan persona answer using RAG context and Groq LLaMA."""
    context = rag_service.retrieve_context(request.message)
    answer = llm_service.query_llama(request.message, context)
    return ChatResponse(answer=answer)
