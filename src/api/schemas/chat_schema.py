"""Schemas for chat endpoint payloads."""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Schema for chat input payload."""

    user_id: str = Field(..., description="Unique user identifier")
    message: str = Field(..., min_length=1, description="User message / question")


class ChatResponse(BaseModel):
    """Schema for chat output payload."""

    answer: str
