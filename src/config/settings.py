"""Configuration settings for the Raavan AI FastAPI backend."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# ========== PROJECT PATHS ==========
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data"
CHROMA_DB_DIR = PROJECT_ROOT / "chroma_db"


# ========== APP CONFIGURATION ==========
class AppConfig:
    """FastAPI app and CORS configuration."""

    APP_NAME = "Raavan AI Backend"
    APP_VERSION = "1.0.0"
    APP_DESCRIPTION = "REST APIs for Raavan chatbot (RAG + Groq) and astrology calculations."

    # Comma-separated list, e.g. "http://localhost:3000,http://127.0.0.1:5173"
    CORS_ORIGINS = [
        origin.strip()
        for origin in os.getenv("CORS_ORIGINS", "*").split(",")
        if origin.strip()
    ]

    if not CORS_ORIGINS:
        CORS_ORIGINS = ["*"]


# ========== API CONFIGURATION ==========
class APIConfig:
    """Groq API configuration and request constants."""

    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
    MODEL_NAME = "meta-llama/llama-4-scout-17b-16e-instruct"

    MAX_TOKENS = 700
    TEMPERATURE = 0.7
    REQUEST_TIMEOUT = 30

    @classmethod
    def get_headers(cls):
        """Build request headers for Groq API calls."""
        return {
            "Authorization": f"Bearer {cls.GROQ_API_KEY}",
            "Content-Type": "application/json",
        }


# ========== EMBEDDINGS CONFIGURATION ==========
class EmbeddingsConfig:
    """Configuration for embeddings and vector retrieval."""

    MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
    PERSIST_DIRECTORY = str(CHROMA_DB_DIR)
    DEFAULT_K = 7


# ========== ASTROLOGY CONFIGURATION ==========
class AstrologyConfig:
    """Astrology constants used by planetary calculations."""

    ZODIAC_SIGNS = [
        "Aries",
        "Taurus",
        "Gemini",
        "Cancer",
        "Leo",
        "Virgo",
        "Libra",
        "Scorpio",
        "Sagittarius",
        "Capricorn",
        "Aquarius",
        "Pisces",
    ]

    PLANET_EMOJIS = {
        "Sun": "☀️",
        "Moon": "🌙",
        "Mars": "♂️",
        "Mercury": "☿️",
        "Jupiter": "♃",
        "Venus": "♀️",
        "Saturn": "♄",
        "Uranus": "♅",
        "Neptune": "♆",
        "Pluto": "♇",
    }


# ========== RAAVAN PERSONA CONFIGURATION ==========
class PersonaConfig:
    """Prompt and persona configuration for LLM responses."""

    SYSTEM_PROMPT = (
        "You are Raavan, the demon king of Lanka from the Ramayan. "
        "Answer the question ONLY using the context provided. "
        "Give detailed, informative, and long answers. "
        "Use simple, clear English or Indian English so anyone can easily understand your answers. "
        "Use Raavan's tone: bold, confident, slightly arrogant, egotistic and authoritative. "
        "Detect the user's preferred language from the question:\n"
        "- If the question is in Hindi, answer in Hindi.\n"
        "- If the question is in English, answer in English.\n"
        "- If the user specifies a preferred language (e.g., 'Please answer in Hindi'), follow that instruction.\n"
        "Do NOT make up answers outside the context. "
        "If the answer is not in the context, respond: "
        "'This is outside the Ramayan, I know nothing of this.' in the same language as requested."
    )
