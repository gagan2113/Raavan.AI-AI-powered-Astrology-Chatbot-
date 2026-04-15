# Raavan AI - Astrology Chatbot Backend

Raavan AI is a FastAPI backend that combines two capabilities: a Ramayana chatbot powered by retrieval-augmented generation, and Vedic astrology endpoints that calculate planetary positions and produce a personalized reading.

## Features

- Ramayana question answering through a Raavan persona
- Astrology calculations using Swiss Ephemeris
- Personalized astrology reading endpoint with LLM interpretation
- ChromaDB-backed vector retrieval for contextual answers
- CORS support for browser-based frontends

## Requirements

- Python 3.11 or newer
- `pip`
- A Groq API key

## Installation

1. Clone the repository.

   ```bash
   git clone <your-repo-url>
   cd "Raavan.AI – AI-powered Astrology Chatbot"
   ```

2. Create and activate a virtual environment.

   Windows PowerShell:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   Windows Command Prompt:

   ```cmd
   python -m venv .venv
   .venv\Scripts\activate.bat
   ```

   macOS/Linux:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies.

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root.

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   CORS_ORIGINS=http://localhost:3000,http://localhost:8001
   ```

## Running the Backend

Start the API with Uvicorn:

```bash
uvicorn src.app.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:

- Health check: http://localhost:8000/health
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

You can also run the legacy launcher:

```bash
python main.py
```

## Project Structure

```text
Raavan.AI/
├── main.py
├── requirements.txt
├── README.md
├── Backend.md
├── FRONTEND_INTEGRATION.md
├── data/
│   └── ramayan.txt
├── chroma_db/
└── src/
    ├── app/
    │   └── main.py
    ├── api/
    │   ├── controllers/
    │   ├── routes/
    │   └── schemas/
    ├── config/
    │   └── settings.py
    ├── services/
    └── utils/
```

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{ "status": "ok" }
```

### Chat

```http
POST /api/chat
```

Request:

```json
{
  "user_id": "user123",
  "message": "Who is Ram?"
}
```

Response:

```json
{
  "answer": "..."
}
```

### Astrology

```http
POST /api/astrology
```

Request:

```json
{
  "name": "John Doe",
  "dob": "1990-05-15",
  "time": "14:30",
  "location": "New York"
}
```

Response:

```json
{
  "planets": {
    "sun": {
      "degrees": 21.45,
      "sign": 1,
      "sign_name": "Taurus",
      "degree_in_sign": 21.45,
      "emoji": "☀️"
    }
  }
}
```

### Astrology Reading

```http
POST /api/astrology-reading
```

Request:

```json
{
  "name": "John Doe",
  "dob": "1990-05-15",
  "time": "14:30",
  "location": "New York"
}
```

Response:

```json
{
  "name": "John Doe",
  "dob": "1990-05-15",
  "time": "14:30",
  "location": "New York",
  "planets": {},
  "reading": "..."
}
```

## Configuration

The backend reads configuration from environment variables in `src/config/settings.py`.

- `GROQ_API_KEY` - required for LLM responses
- `CORS_ORIGINS` - comma-separated list of allowed frontend origins

The current app configuration is defined in [src/config/settings.py](src/config/settings.py) and the FastAPI app entry point is [src/app/main.py](src/app/main.py).

## Testing

Test the API with `curl`:

```bash
curl http://localhost:8000/health
```

```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"user_id":"user1","message":"Who is Ram?"}'
```

```bash
curl -X POST http://localhost:8000/api/astrology-reading \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "dob": "1990-05-15",
    "time": "14:30",
    "location": "New York"
  }'
```

## Documentation

- [Backend.md](Backend.md) - full API documentation
- [FRONTEND_INTEGRATION.md](FRONTEND_INTEGRATION.md) - frontend integration guide

## Notes

- `main.py` is kept as a simple launcher for local development.
- `chroma_db/` is generated at runtime and can be removed if you need to rebuild the vector store.
