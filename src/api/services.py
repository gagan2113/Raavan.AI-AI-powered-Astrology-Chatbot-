"""
API services for external integrations.
Handles all API calls including Groq LLaMA and vector database operations.
"""

import requests
from typing import Dict, Any, Optional
from config.settings import APIConfig, PersonaConfig


class GroqAPIService:
    """Service for interacting with Groq LLaMA API"""
    
    def __init__(self):
        self.api_url = APIConfig.GROQ_API_URL
        self.headers = APIConfig.get_headers()
        self.model_name = APIConfig.MODEL_NAME
        self.max_tokens = APIConfig.MAX_TOKENS
    
    def query_llama(self, question: str, context: str) -> str:
        """
        Query the Groq LLaMA model with context.
        
        Args:
            question (str): User's question
            context (str): Retrieved context from vector database
            
        Returns:
            str: Generated response from LLaMA
        """
        try:
            messages = [
                {
                    "role": "system",
                    "content": PersonaConfig.SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": f"Question: {question}\n\nContext:\n{context}"
                }
            ]
            
            payload = {
                "model": self.model_name,
                "messages": messages,
                "max_tokens": self.max_tokens
            }
            
            response = requests.post(
                self.api_url, 
                headers=self.headers, 
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            
            answer = response.json()["choices"][0]["message"]["content"]
            return answer
            
        except requests.exceptions.RequestException as e:
            return f"⚠ Network error: {str(e)}"
        except KeyError as e:
            return f"⚠ API response error: Missing key {str(e)}"
        except Exception as e:
            return f"⚠ Error calling Groq LLaMA: {str(e)}"


class VectorDatabaseService:
    """Service for vector database operations"""
    
    def __init__(self, vectordb):
        """
        Initialize with ChromaDB instance.
        
        Args:
            vectordb: ChromaDB instance
        """
        self.vectordb = vectordb
    
    def retrieve_context(self, question: str, k: int = 7) -> str:
        """
        Retrieve relevant context from vector database.
        
        Args:
            question (str): User's question
            k (int): Number of documents to retrieve
            
        Returns:
            str: Combined context from retrieved documents
        """
        try:
            results = self.vectordb.similarity_search(question, k=k)
            context_text = "\n\n".join([doc.page_content for doc in results])
            return context_text
        except Exception as e:
            return f"Error retrieving context: {str(e)}"
    
    def get_database_stats(self) -> Dict[str, Any]:
        """
        Get statistics about the vector database.
        
        Returns:
            Dict[str, Any]: Database statistics
        """
        try:
            # Get collection info if available
            collection = self.vectordb._collection
            return {
                "collection_name": collection.name if hasattr(collection, 'name') else "Unknown",
                "status": "Connected"
            }
        except Exception as e:
            return {
                "status": "Error",
                "error": str(e)
            }
