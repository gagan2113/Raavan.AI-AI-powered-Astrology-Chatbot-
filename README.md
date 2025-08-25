# 🗡️ Raavan AI - Your Ramayan Guide

A modular Streamlit application that embodies the wisdom of Raavan, the demon king of Lanka, to answer questions about the Ramayan using AI and vector search.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or download the project**
   ```bash
   cd "C:\Users\HP\OneDrive\Desktop\Raavan.ai"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run main.py
   ```

## 📁 Project Structure

```
Raavan.ai/
├── main.py                    # 🚀 Main entry point
├── requirements.txt           # 📦 Dependencies
├── README.md                  # 📚 This file
├── data/                      # 📄 Original data files
├── chroma_db/                 # 🗄️ Vector database
└── src/                       # 📁 Source code
    ├── app/                   # 🎯 Core application logic
    │   └── main.py           # Main app orchestration
    ├── ui/                    # 🎨 UI components
    │   └── components.py     # Reusable UI components
    ├── api/                   # 🔌 API services
    │   └── services.py       # External API integrations
    ├── styles/                # 💅 CSS and styling
    │   └── main.py           # Custom styles
    ├── utils/                 # 🛠️ Helper functions
    │   └── helpers.py        # Utilities & calculations
    ├── config/                # ⚙️ Configuration
    │   └── settings.py       # Settings & constants
    └── assets/                # 🎭 Static files (images, etc.)
```

## ✨ Features

- **🤖 AI Chat Interface**: Chat with Raavan about the Ramayan
- **🔮 Astrology Calculator**: Generate personalized horoscopes
styling
- **📱 Responsive Design**: Works on desktop and mobile
- **🏗️ Modular Architecture**: Clean, maintainable code structure

## 🔧 Configuration

### API Keys
Edit `src/config/settings.py` to configure your API keys:

```python
class APIConfig:
    GROQ_API_KEY = "your_groq_api_key_here"
    # ... other settings
```

## 🎯 Usage

1. **Start the application**: `streamlit run main.py`
2. **Ask questions**: Type questions about the Ramayan in the chat
3. **Generate horoscope**: Use the sidebar astrology calculator

---

Made with ❤️ for exploring the wisdom of the Ramayan through AI - Modular Ramayan Chatbot

A sophisticated AI chatbot that embodies the wisdom of Raavan from the Ramayan, featuring astrology calculations and a beautiful ChatGPT-like interface.

## 🏗️ Project Structure

```
Raavan.ai/
├── main.py                    # Main entry point
├── requirements.txt           # Dependencies
├── data/                      # Original data files
│   └── ramayan.txt
├── chroma_db/                 # Vector database
│   └── ...
└── src/                       # Source code (modular structure)
    ├── __init__.py
    ├── app/                   # Core application logic
    │   ├── __init__.py
    │   └── main.py           # Main app class and orchestration
    ├── ui/                    # UI components
    │   ├── __init__.py
    │   └── components.py     # Reusable UI components
    ├── api/                   # API services
    │   ├── __init__.py
    │   └── services.py       # Groq API and vector DB services
    ├── styles/                # CSS and styling
    │   ├── __init__.py
    │   └── main.py           # Custom CSS styles
    ├── utils/                 # Helper functions
    │   ├── __init__.py
    │   └── helpers.py        # Utility functions and astrology
    ├── config/                # Configuration
    │   ├── __init__.py
    │   └── settings.py       # App settings and constants
    └── assets/                # Static files (images, icons)
        └── __init__.py
```

## 🚀 Quick Start

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd "C:\Users\HP\OneDrive\Desktop\Raavan.ai"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run main.py
   ```

### Usage

1. **Chat Interface**: Ask questions about the Ramayan
2. **Astrology Calculator**: Generate personalized horoscopes
3. **Settings**: Clear chat history and manage preferences

## 📁 Module Descriptions

### 🎯 Core Application (`src/app/`)
- **`main.py`**: Main application class with session management
- Orchestrates all components and services
- Handles routing and error management

### 🎨 UI Components (`src/ui/`)
- **`components.py`**: Reusable Streamlit components
- Header, sidebar, chat interface, astrology forms
- Modular and easy to maintain

### 🔌 API Services (`src/api/`)
- **`services.py`**: External API integrations
- Groq LLaMA API service
- Vector database operations

### 💅 Styles (`src/styles/`)
- **`main.py`**: Custom CSS for ChatGPT-like interface
- Responsive design with beautiful gradients
- Sidebar styling and mobile optimization

### 🛠️ Utilities (`src/utils/`)
- **`helpers.py`**: Helper functions and calculations
- Astrology calculator using Swiss Ephemeris
- Date/time formatting and validation

### ⚙️ Configuration (`src/config/`)
- **`settings.py`**: All app configuration and constants
- API keys, endpoints, and default values
- Environment-specific settings

### 🎭 Assets (`src/assets/`)
- Static files like images and icons
- Background images and UI assets

## 🎨 Key Features

### ✨ Beautiful Interface
- **ChatGPT-inspired design** with gradient backgrounds
- **Responsive layout** for desktop and mobile
- **Glass-morphism effects** with backdrop blur

### 🤖 AI-Powered Chat
- **Raavan persona** with authentic tone and knowledge
- **Context-aware responses** using vector database
- **Multi-language support** (English/Hindi)

### 🔮 Astrology Calculator
- **Swiss Ephemeris integration** for accurate calculations
- **Planetary positions** with zodiac signs
- **Beautiful result display** with emoji indicators

### 📱 User Experience
- **Session management** with chat history
- **Input validation** and error handling
- **Loading states** and user feedback

## 🔧 Configuration

### API Keys
Update your API key in `src/config/settings.py`:
```python
class APIConfig:
    GROQ_API_KEY = "your-api-key-here"
```

### Custom Background
Modify the CSS in `src/styles/main.py` to use your own background image:
```python
# Replace the gradient with your image URL
background-image: url('YOUR_IMAGE_URL');
```

### Default Values
Customize default values in `src/config/settings.py`:
```python
class UIConfig:
    DEFAULT_BIRTH_YEAR = 2000
    DEFAULT_BIRTH_TIME = "12:00"
```

## 🧪 Development

### Adding New Components
1. Create component in `src/ui/components.py`
2. Import and use in `src/app/main.py`
3. Add styling in `src/styles/main.py`

### Adding New Services
1. Create service class in `src/api/services.py`
2. Initialize in `src/app/main.py`
3. Add configuration in `src/config/settings.py`

### Adding Utilities
1. Add functions to `src/utils/helpers.py`
2. Import where needed
3. Add tests if required

## 📚 Dependencies

- **Streamlit**: Web framework
- **LangChain**: Vector database and embeddings
- **SwissEph**: Astrology calculations
- **Requests**: API calls
- **ChromaDB**: Vector storage

## 🎯 Benefits of This Structure

### 🔧 Maintainability
- **Separation of concerns**: Each module has a specific purpose
- **Easy debugging**: Issues are isolated to specific modules
- **Code reusability**: Components can be reused across the app

### 📈 Scalability
- **Easy to extend**: Add new features without touching existing code
- **Team collaboration**: Multiple developers can work on different modules
- **Testing**: Each module can be tested independently

### 🚀 Performance
- **Lazy loading**: Only import what you need
- **Caching**: Streamlit caching works better with modular code
- **Memory efficiency**: Clear separation of resources

## 🔮 Future Enhancements

- Add user authentication
- Implement database for user profiles
- Add more astrology features
- Create mobile app version
- Add voice input/output

## 📄 License

This project is for educational and personal use.

---

**Created with ❤️ for learning modular Python development**
