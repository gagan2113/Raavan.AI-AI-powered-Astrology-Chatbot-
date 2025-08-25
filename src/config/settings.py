"""
Configuration settings for Raavan AI application.
Contains all constants, API keys, and environment variables.
"""

import os
from pathlib import Path

# ========== PROJECT PATHS ==========
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data"
CHROMA_DB_DIR = PROJECT_ROOT / "chroma_db"

# ========== API CONFIGURATION ==========
class APIConfig:
    """API configuration and endpoints"""
    
    # Groq API Settings
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
    MODEL_NAME = "meta-llama/llama-4-scout-17b-16e-instruct"
    
    # Request Settings
    MAX_TOKENS = 700
    TEMPERATURE = 0.7
    
    @classmethod
    def get_headers(cls):
        """Get API headers for Groq requests"""
        return {
            "Authorization": f"Bearer {cls.GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

# ========== EMBEDDINGS CONFIGURATION ==========
class EmbeddingsConfig:
    """Configuration for embeddings and vector database"""
    
    MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
    PERSIST_DIRECTORY = str(CHROMA_DB_DIR)
    DEFAULT_K = 7  # Number of documents to retrieve

# ========== UI CONFIGURATION ==========
class UIConfig:
    """UI settings and constants"""
    
    PAGE_TITLE = "Raavan AI - Your Ramayan Guide"
    PAGE_ICON = "🗡️"
    LAYOUT = "wide"
    SIDEBAR_STATE = "expanded"
    
    # Default values
    DEFAULT_BIRTH_YEAR = 2000
    DEFAULT_BIRTH_MONTH = 1
    DEFAULT_BIRTH_DAY = 1
    DEFAULT_BIRTH_TIME = "12:00"

# ========== ASTROLOGY CONFIGURATION ==========
class AstrologyConfig:
    """Astrology calculation settings"""
    
    ZODIAC_SIGNS = [
        'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
        'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
    ]
    
    PLANET_EMOJIS = {
        "Sun": "☀️", "Moon": "🌙", "Mars": "♂️", "Mercury": "☿️",
        "Jupiter": "♃", "Venus": "♀️", "Saturn": "♄", 
        "Uranus": "♅", "Neptune": "♆", "Pluto": "♇"
    }

# ========== RAAVAN PERSONA CONFIGURATION ==========
class PersonaConfig:
    """Configuration for Raavan's personality and responses"""
    
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
    
    WELCOME_MESSAGE = (
        "🙏 Welcome to Raavan's Court. "
        "I am Raavan, the ten-headed king of Lanka. Ask me anything about the Ramayan, "
        "and I shall answer with the wisdom of ages. My knowledge spans the sacred texts, "
        "and I speak with the authority of one who lived through these epic tales."
    )
    
    DEFAULT_CHAT_PLACEHOLDER = "Ask Raavan anything about the Ramayan... 🗡️"
    THINKING_MESSAGE = "Raavan is contemplating your question..."

# ========== ENVIRONMENT SETTINGS ==========
def load_environment():
    """Load environment variables if available"""
    # You can add dotenv loading here if needed
    pass

# Initialize environment on import
load_environment()
