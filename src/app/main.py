"""
Main application logic and orchestration.
Contains the core app class and session management.
"""

import streamlit as st
from datetime import datetime
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from config.settings import UIConfig, EmbeddingsConfig
from config.settings import UIConfig, PersonaConfig
from api.services import GroqAPIService, VectorDatabaseService
from utils.helpers import AstrologyCalculator, combine_date_time
from ui.components import (
    HeaderComponent, WelcomeComponent, ChatHistoryComponent,
    SidebarComponent, ChatInterfaceComponent, AstrologyResultsComponent,
    ErrorComponent
)
from styles.main import get_custom_css


class RaavanAIApp:
    """Main application class for Raavan AI"""
    
    def __init__(self):
        """Initialize the application"""
        self.setup_page_config()
        self.apply_styling()
        self.initialize_services()
        self.initialize_session_state()
    
    def setup_page_config(self):
        """Configure Streamlit page settings"""
        st.set_page_config(
            page_title=UIConfig.PAGE_TITLE,
            page_icon=UIConfig.PAGE_ICON,
            layout=UIConfig.LAYOUT,
            initial_sidebar_state=UIConfig.SIDEBAR_STATE
        )
    
    def apply_styling(self):
        """Apply custom CSS styling"""
        st.markdown(get_custom_css(), unsafe_allow_html=True)
    
    def initialize_services(self):
        """Initialize API services and database connections"""
        try:
            # Initialize embeddings with better error handling
            self.embedding = HuggingFaceEmbeddings(
                model_name=EmbeddingsConfig.MODEL_NAME,
                model_kwargs={'device': 'cpu'},  # Force CPU usage
                encode_kwargs={'normalize_embeddings': True}  # Normalize embeddings
            )
            
            # Initialize vector database
            self.vectordb = Chroma(
                persist_directory=EmbeddingsConfig.PERSIST_DIRECTORY,
                embedding_function=self.embedding
            )
            
            # Initialize services
            self.groq_service = GroqAPIService()
            self.vector_service = VectorDatabaseService(self.vectordb)
            self.astrology_calculator = AstrologyCalculator()
            
        except Exception as e:
            st.error(f"Error initializing services: {str(e)}")
            # Try alternative embedding model
            try:
                st.info("Trying alternative embedding model...")
                self.embedding = HuggingFaceEmbeddings(
                    model_name="all-MiniLM-L6-v2",  # Simpler model name
                    model_kwargs={'device': 'cpu'}
                )
                
                self.vectordb = Chroma(
                    persist_directory=EmbeddingsConfig.PERSIST_DIRECTORY,
                    embedding_function=self.embedding
                )
                
                self.groq_service = GroqAPIService()
                self.vector_service = VectorDatabaseService(self.vectordb)
                self.astrology_calculator = AstrologyCalculator()
                
                st.success("Services initialized with alternative model!")
                
            except Exception as e2:
                st.error(f"Failed to initialize with alternative model: {str(e2)}")
                st.warning("Running app without vector database functionality...")
                
                # Initialize without vector database
                self.embedding = None
                self.vectordb = None
                self.groq_service = GroqAPIService()
                self.vector_service = None
                self.astrology_calculator = AstrologyCalculator()
    
    def initialize_session_state(self):
        """Initialize Streamlit session state"""
        if "history" not in st.session_state:
            st.session_state.history = []
    
    def render_header(self):
        """Render application header"""
        HeaderComponent.render()
    
    def render_welcome_message(self):
        """Render welcome message for new users"""
        if len(st.session_state.history) == 0:
            WelcomeComponent.render()
    
    def render_sidebar_toggle(self):
        """Render small sidebar toggle button with arrow in corner"""
        # Show appropriate arrow based on sidebar state
        if st.session_state.sidebar_open:
            if st.button("◀", key="close_sidebar", help="Close sidebar"):
                st.session_state.sidebar_open = False
                st.rerun()
        else:
            if st.button("▶", key="open_sidebar", help="Open sidebar"):
                st.session_state.sidebar_open = True
                st.rerun()
    
    def render_sidebar(self):
        """Render sidebar with settings and astrology calculator"""
        with st.sidebar:
            # Settings section
            SidebarComponent.render_settings()
            
            # Astrology section
            name, birth_datetime, location, is_valid = SidebarComponent.render_astrology_section()
            
            # Handle horoscope generation
            if st.button("✨ Generate Horoscope"):
                self.handle_horoscope_generation(name, birth_datetime, location, is_valid)
            
            # About section
            SidebarComponent.render_about_section()
    
    def handle_horoscope_generation(self, name: str, birth_datetime: datetime, location: str, is_valid: bool):
        """
        Handle horoscope generation logic.
        
        Args:
            name (str): Person's name
            birth_datetime (datetime): Birth date and time
            location (str): Birth location
            is_valid (bool): Whether inputs are valid
        """
        if is_valid:
            with st.spinner("🌟 Calculating planetary positions..."):
                try:
                    # Calculate Julian Day
                    julian_day = self.astrology_calculator.calculate_julian_day(birth_datetime)
                    
                    # Get planetary positions
                    planets = self.astrology_calculator.get_planetary_positions(julian_day)
                    
                    # Display results
                    AstrologyResultsComponent.render(name, location, birth_datetime, planets)
                    
                except Exception as e:
                    st.error(f"Error calculating horoscope: {str(e)}")
        else:
            ErrorComponent.render_validation_error()
    
    def render_chat_interface(self):
        """Render main chat interface"""
        # Chat area header
        ChatInterfaceComponent.render_chat_area()
        
        # Display chat history
        ChatHistoryComponent.render(st.session_state.history)
        
        # Handle user input
        user_question = ChatInterfaceComponent.handle_user_input()
        
        if user_question:
            self.process_user_message(user_question)
    
    def process_user_message(self, user_question: str):
        """
        Process user message and generate response.
        
        Args:
            user_question (str): User's question
        """
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_question)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            with ChatInterfaceComponent.display_thinking():
                try:
                    # Retrieve context from vector database if available
                    context = ""
                    if self.vector_service is not None:
                        context = self.vector_service.retrieve_context(
                            user_question, 
                            k=EmbeddingsConfig.DEFAULT_K
                        )
                    else:
                        st.info("Vector database not available. Using base model without context.")
                    
                    # Generate response using Groq API
                    answer = self.groq_service.query_llama(user_question, context)
                    
                    # Display response
                    st.markdown(answer)
                    
                    # Store in history
                    st.session_state.history.append({
                        "question": user_question, 
                        "answer": answer
                    })
                    
                except Exception as e:
                    error_message = f"Error generating response: {str(e)}"
                    st.error(error_message)
                    ErrorComponent.render_api_error(error_message)
    
    def run(self):
        """Main application entry point"""
        try:
            # Initialize sidebar state
            if 'sidebar_open' not in st.session_state:
                st.session_state.sidebar_open = True
            
            # Render toggle button
            self.render_sidebar_toggle()
            
            # Render header
            self.render_header()
            
            # Render welcome message
            self.render_welcome_message()
            
            # Render sidebar conditionally
            if st.session_state.sidebar_open:
                self.render_sidebar()
            
            # Render chat interface
            self.render_chat_interface()
            
        except Exception as e:
            st.error(f"Application error: {str(e)}")
            st.stop()


def create_app():
    """
    Factory function to create and return app instance.
    
    Returns:
        RaavanAIApp: Application instance
    """

    return RaavanAIApp()


# Streamlit entry point
if __name__ == "__main__":
    app = create_app()
    app.run()
