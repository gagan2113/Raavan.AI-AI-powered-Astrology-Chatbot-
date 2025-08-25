"""
UI Components for the Raavan AI application.
Contains reusable UI components and layouts.
"""

import streamlit as st
from datetime import datetime
from typing import Optional, Tuple, Any, Dict
from config.settings import UIConfig, PersonaConfig
from utils.helpers import (
    get_default_birth_time, 
    validate_name, 
    validate_location,
    format_datetime_display
)


class HeaderComponent:
    """Component for app header and title"""
    
    @staticmethod
    def render():
        """Render the main header"""
        st.markdown('<h1 class="main-title">🗡️ Raavan AI</h1>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Your Personal Guide to the Ramayan</p>', unsafe_allow_html=True)


class WelcomeComponent:
    """Component for welcome message"""
    
    @staticmethod
    def render():
        """Render welcome card for new users"""
        st.markdown(f"""
        <div class="welcome-card">
            <h3>🙏 Welcome to Raavan's Court</h3>
            <p>{PersonaConfig.WELCOME_MESSAGE}</p>
        </div>
        """, unsafe_allow_html=True)


class ChatHistoryComponent:
    """Component for displaying chat history"""
    
    @staticmethod
    def render(history):
        """
        Render chat history.
        
        Args:
            history: List of chat messages
        """
        for qa in history:
            with st.chat_message("user"):
                st.markdown(qa["question"])
            with st.chat_message("assistant"):
                st.markdown(qa["answer"])


class AstrologyInputComponent:
    """Component for astrology input form"""
    
    @staticmethod
    def render() -> Tuple[str, datetime, str, bool]:
        """
        Render astrology input form.
        
        Returns:
            Tuple[str, datetime, str, bool]: name, birth_datetime, location, is_valid
        """
        with st.container():
            name = st.text_input("✨ Full Name", placeholder="Enter your full name")
            
            col1, col2 = st.columns(2)
            with col1:
                dob = st.date_input(
                    "📅 Birth Date", 
                    value=datetime(
                        UIConfig.DEFAULT_BIRTH_YEAR,
                        UIConfig.DEFAULT_BIRTH_MONTH,
                        UIConfig.DEFAULT_BIRTH_DAY
                    )
                )
            with col2:
                tob = st.time_input(
                    "⏰ Birth Time", 
                    value=get_default_birth_time()
                )
            
            location = st.text_input("📍 Birth Place", placeholder="City, Country")
            
            # Combine date and time
            birth_datetime = datetime.combine(dob, tob)
            
            # Validate inputs
            is_valid = validate_name(name) and validate_location(location)
            
            return name, birth_datetime, location, is_valid


class AstrologyResultsComponent:
    """Component for displaying astrology results"""
    
    @staticmethod
    def render(name: str, location: str, birth_datetime: datetime, planets: Dict[str, Any]):
        """
        Render astrology calculation results.
        
        Args:
            name (str): Person's name
            location (str): Birth location
            birth_datetime (datetime): Birth date and time
            planets (Dict[str, Any]): Planetary positions
        """
        st.success(f"🌟 Horoscope for **{name}**")
        st.info(f"📍 **Place:** {location}")
        st.info(f"📅 **Date & Time:** {format_datetime_display(birth_datetime)}")

        if planets:
            st.markdown("### 🪐 Planetary Positions")
            for planet, details in planets.items():
                emoji = details.get("emoji", "🪐")
                st.markdown(f"""
                **{emoji} {planet}:**  
                🔸 Sign: {details['sign_name']}  
                🔸 Position: {details['degrees']:.2f}°  
                🔸 Degree in Sign: {details['degree_in_sign']:.2f}°  
                """)
        else:
            st.error("❌ Error calculating planetary positions. Please try again.")


class SidebarComponent:
    """Component for sidebar layout and content"""
    
    @staticmethod
    def render_settings():
        """Render settings section in sidebar"""
        st.markdown("## ⚙️ Settings")
        
        if st.button("🗑️ Clear Chat History"):
            st.session_state.history = []
            st.success("Chat history cleared!")
            st.rerun()
    
    @staticmethod
    def render_astrology_section():
        """Render astrology calculator section"""
        st.markdown("---")
        st.markdown("## 🔮 Astrology Calculator")
        st.markdown("*Generate your personalized horoscope*")
        
        return AstrologyInputComponent.render()
    
    @staticmethod
    def render_about_section():
        """Render about section"""
        st.markdown("---")
        st.markdown("### 📚 About")
        st.markdown("""
        This AI assistant embodies the wisdom and knowledge of Raavan, 
        drawing from authentic sources of the Ramayan to provide 
        insightful answers about this epic tale.
        """)


class ChatInterfaceComponent:
    """Component for main chat interface"""
    
    @staticmethod
    def render_chat_area():
        """Render main chat area header"""
        st.markdown("## 💬 Chat with Raavan")
    
    @staticmethod
    def handle_user_input() -> Optional[str]:
        """
        Handle user input from chat input.
        
        Returns:
            Optional[str]: User's question if provided
        """
        return st.chat_input(PersonaConfig.DEFAULT_CHAT_PLACEHOLDER)
    
    @staticmethod
    def display_thinking():
        """Display thinking message"""
        return st.spinner(PersonaConfig.THINKING_MESSAGE)


class ErrorComponent:
    """Component for error handling and display"""
    
    @staticmethod
    def render_validation_error():
        """Render validation error for astrology form"""
        st.error("Please fill in your name and birth place!")
    
    @staticmethod
    def render_api_error(error_message: str):
        """
        Render API error message.
        
        Args:
            error_message (str): Error message to display
        """
        st.error(f"API Error: {error_message}")
    
    @staticmethod
    def render_calculation_error():
        """Render calculation error message"""
        st.error("Error in calculations. Please check your inputs and try again.")
