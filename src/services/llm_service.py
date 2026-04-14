"""Service for Groq LLaMA API calls."""

import requests

from src.config.settings import APIConfig, PersonaConfig


class LLMService:
    """Handles interaction with the Groq LLaMA chat completion API."""

    def __init__(self):
        self.api_url = APIConfig.GROQ_API_URL
        self.headers = APIConfig.get_headers()
        self.model_name = APIConfig.MODEL_NAME
        self.max_tokens = APIConfig.MAX_TOKENS
        self.temperature = APIConfig.TEMPERATURE
        self.timeout = APIConfig.REQUEST_TIMEOUT

    def query_llama(self, question: str, context: str, system_prompt: str = None) -> str:
        """Generate an answer using provided context and system prompt.
        
        Args:
            question: The user's question or prompt
            context: Additional context to include (can be empty string)
            system_prompt: Optional custom system prompt. If None, uses Raavan persona prompt.
            
        Returns:
            Generated response from LLM
        """
        try:
            # Use custom system prompt if provided, otherwise use Raavan persona
            prompt = system_prompt or PersonaConfig.SYSTEM_PROMPT
            
            messages = [
                {
                    "role": "system",
                    "content": prompt,
                },
            ]
            
            # Include context in user message if provided
            if context and context.strip():
                user_content = f"{question}\n\nContext:\n{context}"
            else:
                user_content = question
                
            messages.append({
                "role": "user",
                "content": user_content,
            })

            payload = {
                "model": self.model_name,
                "messages": messages,
                "max_tokens": self.max_tokens,
                "temperature": self.temperature,
            }

            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=self.timeout,
            )
            response.raise_for_status()

            return response.json()["choices"][0]["message"]["content"]

        except requests.exceptions.RequestException as exc:
            return f"⚠ Network error: {str(exc)}"
        except KeyError as exc:
            return f"⚠ API response error: Missing key {str(exc)}"
        except Exception as exc:
            return f"⚠ Error calling Groq LLaMA: {str(exc)}"


llm_service = LLMService()
