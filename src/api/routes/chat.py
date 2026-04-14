"""Chat route definitions."""

from fastapi import APIRouter

from src.api.controllers.chat_controller import handle_chat
from src.api.schemas.chat_schema import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse, summary="Ask Raavan about the Ramayan")
def chat(request: ChatRequest) -> ChatResponse:
    """Process a chat question and return Raavan's answer."""
    return handle_chat(request)
