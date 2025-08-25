"""
Custom CSS styles for the Raavan AI application.
Contains all styling for the Streamlit interface.
"""

def get_custom_css():
    """
    Returns the custom CSS for the application.
    
    Returns:
        str: Complete CSS string for styling the Streamlit app
    """
    return """
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Global styling */
        * {
            font-family: 'Inter', sans-serif;
        }
        
        /* Main app background - Dark to Teal Vertical Gradient */
        .stApp {
            background: linear-gradient(180deg, #000000 0%, #0f4c5c 100%);
            background-attachment: fixed;
            min-height: 100vh;
        }
        
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
            background: rgba(15, 76, 92, 0.15);
            border-radius: 20px;
            margin: 2rem auto;
            backdrop-filter: blur(15px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(15, 76, 92, 0.3);
        }
        
        /* Title styling - Modern Light Typography */
        .main-title {
            text-align: center;
            color: #ffffff;
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
            background: linear-gradient(90deg, #ffffff 0%, #00b4d8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .subtitle {
            text-align: center;
            color: #e0f7fa;
            font-size: 1.3rem;
            margin-bottom: 2rem;
            font-style: italic;
            font-weight: 300;
        }
        
        /* Welcome message - Modern Minimalistic */
        .welcome-card {
            background: linear-gradient(180deg, rgba(0, 0, 0, 0.8) 0%, rgba(15, 76, 92, 0.8) 100%);
            color: #ffffff;
            padding: 2rem;
            border-radius: 18px;
            text-align: center;
            margin: 2rem 0;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(15, 76, 92, 0.3);
            backdrop-filter: blur(10px);
        }
        
        /* Chat messages styling - Dark to Teal Theme */
        .stChatMessage {
            border-radius: 15px !important;
            margin: 1rem 0 !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
            border: 1px solid rgba(15, 76, 92, 0.2) !important;
        }
        
        /* User message */
        .stChatMessage[data-testid="user"] {
            background: linear-gradient(180deg, rgba(0, 0, 0, 0.9) 0%, rgba(15, 76, 92, 0.9) 100%) !important;
        }
        
        .stChatMessage[data-testid="user"] .stMarkdown {
            color: #e0f7fa !important;
        }
        
        /* Assistant message */
        .stChatMessage[data-testid="assistant"] {
            background: linear-gradient(180deg, rgba(15, 76, 92, 0.9) 0%, rgba(0, 0, 0, 0.9) 100%) !important;
        }
        
        .stChatMessage[data-testid="assistant"] .stMarkdown {
            color: #e0f7fa !important;
        }
        
        /* Sidebar styling - Dark to Teal Theme */
        .css-1d391kg, .css-1cypcdb {
            background: linear-gradient(180deg, #000000 0%, #0f4c5c 100%) !important;
        }
        
        /* Sidebar content container */
        .css-1d391kg .css-6qob1r, .css-1cypcdb .css-6qob1r {
            background: rgba(15, 76, 92, 0.2) !important;
            border-radius: 15px !important;
            padding: 1.5rem !important;
            margin: 1rem 0.5rem !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
            backdrop-filter: blur(10px) !important;
            border: 1px solid rgba(15, 76, 92, 0.3) !important;
        }
        
        /* Sidebar text elements */
        .css-1d391kg .stMarkdown, .css-1cypcdb .stMarkdown {
            color: #e0f7fa !important;
        }
        
        .css-1d391kg .stMarkdown h1, .css-1cypcdb .stMarkdown h1,
        .css-1d391kg .stMarkdown h2, .css-1cypcdb .stMarkdown h2,
        .css-1d391kg .stMarkdown h3, .css-1cypcdb .stMarkdown h3 {
            color: #ffffff !important;
            font-weight: 600 !important;
        }
        
        /* Sidebar labels */
        .css-1d391kg label, .css-1cypcdb label {
            color: #e0f7fa !important;
            font-weight: 500 !important;
            font-size: 0.95rem !important;
        }
        
        /* Input styling */
        .stTextInput > div > div > input,
        .stDateInput > div > div > input,
        .stTimeInput > div > div > input {
            border-radius: 10px !important;
            border: 2px solid #e9ecef !important;
            padding: 0.75rem !important;
            font-size: 1rem !important;
            background: white !important;
            color: #2c3e50 !important;
        }
        
        .stTextInput > div > div > input:focus,
        .stDateInput > div > div > input:focus,
        .stTimeInput > div > div > input:focus {
            border-color: #667eea !important;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
            outline: none !important;
        }
        
        /* Sidebar specific input styling */
        .css-1d391kg .stTextInput > div > div > input,
        .css-1d391kg .stDateInput > div > div > input,
        .css-1d391kg .stTimeInput > div > div > input,
        .css-1cypcdb .stTextInput > div > div > input,
        .css-1cypcdb .stDateInput > div > div > input,
        .css-1cypcdb .stTimeInput > div > div > input {
            background: white !important;
            border: 2px solid #ddd !important;
            color: #2c3e50 !important;
            font-size: 0.95rem !important;
            padding: 0.6rem 0.75rem !important;
            border-radius: 8px !important;
        }
        
        .css-1d391kg .stTextInput > div > div > input:focus,
        .css-1d391kg .stDateInput > div > div > input:focus,
        .css-1d391kg .stTimeInput > div > div > input:focus,
        .css-1cypcdb .stTextInput > div > div > input:focus,
        .css-1cypcdb .stDateInput > div > div > input:focus,
        .css-1cypcdb .stTimeInput > div > div > input:focus {
            border-color: #667eea !important;
            box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2) !important;
        }
        
        /* Time input specific fixes */
        .css-1d391kg .stTimeInput input[type="time"],
        .css-1cypcdb .stTimeInput input[type="time"] {
            background: white !important;
            color: #2c3e50 !important;
            border: 2px solid #ddd !important;
            padding: 0.6rem !important;
            border-radius: 8px !important;
            font-size: 0.95rem !important;
            cursor: pointer !important;
        }
        
        .css-1d391kg .stTimeInput input[type="time"]:focus,
        .css-1cypcdb .stTimeInput input[type="time"]:focus {
            border-color: #667eea !important;
            box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2) !important;
            outline: none !important;
        }
        
        /* Button styling - Modern Teal with Hover Glow */
        .stButton > button {
            background: linear-gradient(180deg, #000000 0%, #0f4c5c 100%) !important;
            color: #ffffff !important;
            border: 2px solid #0f4c5c !important;
            border-radius: 12px !important;
            padding: 0.75rem 1.5rem !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
            width: 100% !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
        }
        
        .stButton > button:hover {
            background: linear-gradient(180deg, #0f4c5c 0%, #00b4d8 100%) !important;
            color: #000000 !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(0, 180, 216, 0.4) !important;
            border-color: #00b4d8 !important;
        }
        
        /* Sidebar toggle button styling - Small corner button */
        .stButton[key="close_sidebar"] > button,
        .stButton[key="open_sidebar"] > button {
            background: linear-gradient(180deg, #000000 0%, #0f4c5c 100%) !important;
            color: #ffffff !important;
            border: 1px solid #0f4c5c !important;
            border-radius: 8px !important;
            width: 35px !important;
            height: 35px !important;
            padding: 0 !important;
            font-size: 0.9rem !important;
            font-weight: bold !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4) !important;
            position: fixed !important;
            top: 15px !important;
            left: 15px !important;
            z-index: 1000 !important;
            opacity: 0.8 !important;
        }
        
        .stButton[key="close_sidebar"] > button:hover,
        .stButton[key="open_sidebar"] > button:hover {
            background: linear-gradient(180deg, #0f4c5c 0%, #00b4d8 100%) !important;
            color: #000000 !important;
            transform: scale(1.05) !important;
            box-shadow: 0 4px 15px rgba(0, 180, 216, 0.5) !important;
            border-color: #00b4d8 !important;
            opacity: 1 !important;
        }
        
        /* Sidebar button styling */
        .css-1d391kg .stButton > button,
        .css-1cypcdb .stButton > button {
            background: linear-gradient(180deg, #000000 0%, #0f4c5c 100%) !important;
            color: #ffffff !important;
            border: 2px solid #0f4c5c !important;
            border-radius: 10px !important;
            padding: 0.6rem 1.2rem !important;
            font-weight: 600 !important;
            font-size: 0.9rem !important;
            transition: all 0.3s ease !important;
            width: 100% !important;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.3) !important;
        }
        
        .css-1d391kg .stButton > button:hover,
        .css-1cypcdb .stButton > button:hover {
            background: linear-gradient(180deg, #0f4c5c 0%, #00b4d8 100%) !important;
            color: #000000 !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 6px 18px rgba(0, 180, 216, 0.3) !important;
            border-color: #00b4d8 !important;
        }
        
        /* Chat input styling - Dark Theme */
        .stChatInputContainer > div {
            border-radius: 15px !important;
            background: rgba(15, 76, 92, 0.2) !important;
            border: 2px solid #0f4c5c !important;
            backdrop-filter: blur(10px) !important;
        }
        
        .stChatInputContainer input {
            font-size: 1.1rem !important;
            padding: 1rem !important;
            background: transparent !important;
            color: #ffffff !important;
        }
        
        .stChatInputContainer input::placeholder {
            color: #b0bec5 !important;
        }
        
        /* Logo styling */
        .logo {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(180deg, #ffffff 0%, #00b4d8 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            margin: 0 auto;
        }
        
        /* Sidebar headers */
        .css-1d391kg h2, .css-1cypcdb h2 {
            color: #ffffff !important;
            font-weight: 600 !important;
            margin-bottom: 1rem !important;
        }
        
        .css-1d391kg h3, .css-1cypcdb h3 {
            color: #e0f7fa !important;
            font-weight: 500 !important;
        }
        
        /* Sidebar success/error messages */
        .css-1d391kg .stSuccess, .css-1cypcdb .stSuccess,
        .css-1d391kg .stError, .css-1cypcdb .stError,
        .css-1d391kg .stWarning, .css-1cypcdb .stWarning,
        .css-1d391kg .stInfo, .css-1cypcdb .stInfo {
            background: rgba(15, 76, 92, 0.3) !important;
            border-radius: 8px !important;
            margin: 0.5rem 0 !important;
            border: 1px solid rgba(15, 76, 92, 0.4) !important;
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            .main-title {
                font-size: 2.2rem;
            }
            .main .block-container {
                padding: 1rem;
                margin: 1rem;
                border-radius: 15px;
            }
        }
        
        /* Hide Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display:none;}
        
        /* Success/error messages */
        .stSuccess, .stError, .stWarning, .stInfo {
            border-radius: 10px !important;
        }
    </style>
    """

def apply_custom_background(image_url=None):
    """
    Apply custom background image to the app.
    
    Args:
        image_url (str, optional): URL of the background image
    
    Returns:
        str: CSS string with custom background
    """
    if image_url:
        return f"""
        <style>
            .stApp {{
                background-image: url('{image_url}');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
        </style>
        """
    return ""
