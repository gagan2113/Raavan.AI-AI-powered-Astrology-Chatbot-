"""
Main entry point for the Raavan AI application.

This is the main Streamlit app file that users will run.
It imports and initializes the modular application structure.

Usage:
    streamlit run main.py
"""

import sys
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

# Add src directory to Python path for imports
current_dir = Path(__file__).parent
src_path = current_dir / "src"
sys.path.insert(0, str(src_path))

# Import and run the application
from app.main import create_app


def main():
    """Main entry point for the application"""
    try:
        # Create and run the application
        app = create_app()
        app.run()
        
    except Exception as e:
        import streamlit as st
        st.error(f"Failed to start application: {str(e)}")
        st.info("Please check your configuration and try again.")


if __name__ == "__main__":
    main()
