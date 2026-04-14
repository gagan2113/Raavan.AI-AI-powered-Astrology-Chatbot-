# Raavan AI Backend - API Documentation

## Overview

**Application Name:** Raavan AI Backend  
**Version:** 1.0.0  
**Description:** REST APIs for Raavan chatbot (RAG + Groq) and astrology calculations.

---

## Base URL

```
http://localhost:8000
```

> **Note:** For production, replace `localhost:8000` with your deployed server URL.

---

## API Endpoints

### 1. Health Check

Check if the backend server is running and operational.

**Endpoint:** `GET /health`

**Method:** GET

**Headers:**
```json
{
  "Content-Type": "application/json"
}
```

**Request:**
```bash
curl -X GET http://localhost:8000/health
```

**Response (200 OK):**
```json
{
  "status": "ok"
}
```

---

### 2. Chat Endpoint - Ask Raavan about Ramayana

Query the chatbot with questions about the Ramayana. The backend retrieves context from the knowledge base and generates responses in Raavan's persona using Groq LLaMA.

**Endpoint:** `POST /api/chat`

**Method:** POST

**Headers:**
```json
{
  "Content-Type": "application/json"
}
```

**Request Body Schema:**
```json
{
  "user_id": "string (required)",
  "message": "string (required, min 1 character)"
}
```

**Example Request:**
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user123",
    "message": "Name all the brothers of Ram"
  }'
```

**Example Response (200 OK):**
```json
{
  "answer": "The audacity. You dare to ask about the brothers of Ram? As if I, Raavan, the mighty King of Lanka, would not know the family of that insignificant prince. Very well, I shall indulge you.\n\nAccording to the tales of the Ramayan, Ram has three brothers. They are:\n\n1. Lakshman: The loyal and trusted brother, always by Ram's side. His skills in warfare and devotion to Ram are well-known.\n2. Bharat: The prince who ruled Ayodhya in Ram's absence. His love for Ram and his desire to bring him back to the kingdom are notable.\n3. Shatrughn: The brave and strong brother, often considered the most powerful of the four. His valour and loyalty to Ram are commendable.\n\nThere, I have listed all the brothers of Ram for you. Now, do not waste my time with such trivial questions. You should be grateful that I, the great Raavan, deign to answer your queries."
}
```

**Error Response (422 Unprocessable Entity):**
```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "message"],
      "msg": "Field required",
      "input": {"user_id": "user123"}
    }
  ]
}
```

**Error Response (500 Internal Server Error):**
```json
{
  "detail": "Error processing chat request"
}
```

---

### 3. Astrology Reading Endpoint - Get Full Personalized Horoscope Reading

Generate a comprehensive personalized astrology reading with planetary positions and detailed interpretation (personality, strengths, weaknesses, career, future predictions, guidance).

**Endpoint:** `POST /api/astrology-reading`

**Method:** POST

**Headers:**
```json
{
  "Content-Type": "application/json"
}
```

**Request Body Schema:**
```json
{
  "name": "string (required, min 1 character)",
  "dob": "string in YYYY-MM-DD format (required)",
  "time": "string in HH:MM format (required)",
  "location": "string (required, min 1 character)"
}
```

**Example Request:**
```bash
curl -X POST http://localhost:8000/api/astrology-reading \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Priya Sharma",
    "dob": "1998-07-22",
    "time": "09:45",
    "location": "Mumbai, India"
  }'
```

**Example Response (200 OK):**
```json
{
  "name": "Priya Sharma",
  "dob": "1998-07-22",
  "time": "09:45",
  "location": "Mumbai, India",
  "planets": {
    "Sun": {
      "degrees": 98.45,
      "sign": 3,
      "sign_name": "Cancer",
      "degree_in_sign": 8.45,
      "emoji": "☀️"
    },
    "Moon": {
      "degrees": 215.32,
      "sign": 7,
      "sign_name": "Libra",
      "degree_in_sign": 5.32,
      "emoji": "🌙"
    }
  },
  "reading": "🔮 PERSONALITY TRAITS:\nPriya, born under the nurturing waters of Cancer with the balanced Moon in Libra, presents a fascinating blend of emotional depth and social grace. Your Cancer Sun grants you a profound connection to your inner world—intuitive, protective, and deeply family-oriented. Yet your Libra Moon softens these waters with an innate desire for harmony, diplomacy, and aesthetic beauty. You are both the emotional protector and the peaceful negotiator, creating a personality that draws others in with genuine warmth while maintaining surprising objectivity when needed...\n\n🌟 STRENGTHS:\n1. Emotional Intelligence: Your Cancer Sun combined with Libra Moon gives you exceptional ability to read emotions and maintain relationships...\n\n⚠️ WEAKNESSES & CHALLENGES:\n1. Indecision: Libra's tendency to weigh all options can paralyze your Cancer intuition...\n\n💼 CAREER & LIFE PATH INSIGHTS:\nYour natural inclination towards roles involving human connection, aesthetics, and emotional work is strong...\n\n🔮 FUTURE PREDICTIONS:\n\nShort Term (Next 6-12 months):\nWith your Moon in Libra, expect harmony in relationships during this period...\n\nLong Term (2-5 years):\nYour Saturn cycle suggests a period of maturation and responsibility...\n\n🧭 GUIDANCE & REMEDIES:\n1. Life Advice: Honor both your need for emotional security and your desire for equilibrium...\n2. Best Days: Practice important decisions on Mondays and Fridays...\n3. Mantras: Recite mantras honoring the Moon to strengthen emotional clarity...\n4. Working With Your Energy: Channel your protective instincts into meaningful relationships..."
}
```

**Error Response (400 Bad Request - Invalid Date):**
```json
{
  "detail": "Invalid birth date format. Use YYYY-MM-DD"
}
```

**Error Response (500 Internal Server Error):**
```json
{
  "detail": "Error generating astrology reading: [error message]"
}
```

---

### Original Astrology Endpoint - Planetary Positions Only

Calculate horoscope planetary positions from birth details (date, time, location).

**Endpoint:** `POST /api/astrology`

**Method:** POST

**Headers:**
```json
{
  "Content-Type": "application/json"
}
```

**Request Body Schema:**
```json
{
  "name": "string (required, min 1 character)",
  "dob": "string in YYYY-MM-DD format (required)",
  "time": "string in HH:MM format (required)",
  "location": "string (required, min 1 character)"
}
```

**Example Request:**
```bash
curl -X POST http://localhost:8000/api/astrology \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Raj Kumar",
    "dob": "1995-03-15",
    "time": "14:30",
    "location": "New Delhi, India"
  }'
```

**Example Response (200 OK):**
```json
{
  "planets": {
    "Sun": {
      "degrees": 0.45,
      "sign": 11,
      "sign_name": "Pisces",
      "degree_in_sign": 24.68,
      "emoji": "☀️"
    },
    "Moon": {
      "degrees": 120.32,
      "sign": 4,
      "sign_name": "Cancer",
      "degree_in_sign": 0.32,
      "emoji": "🌙"
    },
    "Mercury": {
      "degrees": 15.78,
      "sign": 11,
      "sign_name": "Pisces",
      "degree_in_sign": 15.78,
      "emoji": "☿️"
    },
    "Venus": {
      "degrees": 350.12,
      "sign": 11,
      "sign_name": "Pisces",
      "degree_in_sign": 20.12,
      "emoji": "♀️"
    },
    "Mars": {
      "degrees": 45.89,
      "sign": 1,
      "sign_name": "Aries",
      "degree_in_sign": 15.89,
      "emoji": "♂️"
    },
    "Jupiter": {
      "degrees": 180.45,
      "sign": 6,
      "sign_name": "Virgo",
      "degree_in_sign": 0.45,
      "emoji": "♃"
    },
    "Saturn": {
      "degrees": 220.67,
      "sign": 7,
      "sign_name": "Libra",
      "degree_in_sign": 10.67,
      "emoji": "♄"
    },
    "Rahu": {
      "degrees": 90.23,
      "sign": 3,
      "sign_name": "Gemini",
      "degree_in_sign": 0.23,
      "emoji": "☊"
    },
    "Ketu": {
      "degrees": 270.23,
      "sign": 9,
      "sign_name": "Sagittarius",
      "degree_in_sign": 0.23,
      "emoji": "☋"
    }
  }
}
```

**Error Response (400 Bad Request - Invalid Date):**
```json
{
  "detail": "Invalid birth date format. Use YYYY-MM-DD"
}
```

**Error Response (400 Bad Request - Invalid Time):**
```json
{
  "detail": "Invalid birth time format. Use HH:MM"
}
```

**Error Response (422 Unprocessable Entity - Missing Field):**
```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "dob"],
      "msg": "Field required",
      "input": {
        "name": "John Doe",
        "time": "14:30",
        "location": "New York"
      }
    }
  ]
}
```

**Error Response (500 Internal Server Error):**
```json
{
  "detail": "Error calculating horoscope: [error message]"
}
```

---

## CORS Configuration

The backend is configured to accept requests from frontend applications. By default, CORS is enabled for all origins (`*`).

To restrict CORS origins in production, set the `CORS_ORIGINS` environment variable:

```bash
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

---

## Response Codes

| Code | Description | Example |
|------|-------------|---------|
| **200** | OK - Request successful | Chat/Astrology endpoints return valid response |
| **400** | Bad Request - Invalid input | Invalid date/time format in astrology endpoint |
| **422** | Unprocessable Entity - Missing required fields | Missing `message` in chat request |
| **500** | Internal Server Error - Server error | Database/LLM API failure |

---

## Authentication

Currently, the API does not require authentication. All endpoints are publicly accessible.

> **Future Enhancement:** Add API key or JWT token-based authentication if needed.

---

## Rate Limiting

No rate limiting is implemented. For production, consider adding rate limiting to prevent abuse.

---

## Frontend Integration Examples

### JavaScript (Fetch API)

**Chat Request:**
```javascript
const chatRequest = async (userId, message) => {
  const response = await fetch('http://localhost:8000/api/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      user_id: userId,
      message: message
    })
  });
  const data = await response.json();
  return data.answer;
};

// Usage
chatRequest('user123', 'Who is Ram?').then(answer => {
  console.log(answer);
});
```

**Astrology Reading Request (with interpretation):**
```javascript
const getFullAstrologyReading = async (name, dob, time, location) => {
  const response = await fetch('http://localhost:8000/api/astrology-reading', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: name,
      dob: dob,  // Format: YYYY-MM-DD
      time: time, // Format: HH:MM
      location: location
    })
  });
  const data = await response.json();
  return {
    planets: data.planets,
    reading: data.reading
  };
};

// Usage
getFullAstrologyReading('Priya Sharma', '1998-07-22', '09:45', 'Mumbai').then(result => {
  console.log("Planets:", result.planets);
  console.log("Reading:", result.reading);
});
```

### React Example - Astrology Reading

```jsx
import { useState } from 'react';

function AstrologyReadingForm() {
  const [formData, setFormData] = useState({
    name: '',
    dob: '',
    time: '',
    location: ''
  });
  const [readingData, setReadingData] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/api/astrology-reading', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });
      const data = await response.json();
      setReadingData(data);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Name"
          value={formData.name}
          onChange={(e) => setFormData({...formData, name: e.target.value})}
          required
        />
        <input
          type="date"
          value={formData.dob}
          onChange={(e) => setFormData({...formData, dob: e.target.value})}
          required
        />
        <input
          type="time"
          value={formData.time}
          onChange={(e) => setFormData({...formData, time: e.target.value})}
          required
        />
        <input
          type="text"
          placeholder="Location"
          value={formData.location}
          onChange={(e) => setFormData({...formData, location: e.target.value})}
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Generating Reading...' : 'Get Full Reading'}
        </button>
      </form>
      
      {readingData && (
        <div>
          <h2>Your Astrology Reading: {readingData.name}</h2>
          <h3>Planetary Positions</h3>
          <pre>{JSON.stringify(readingData.planets, null, 2)}</pre>
          
          <h3>Your Reading</h3>
          <div style={{whiteSpace: 'pre-wrap', fontFamily: 'serif'}}>
            {readingData.reading}
          </div>
        </div>
      )}
    </div>
  );
}

export default AstrologyReadingForm;
```

---

## Postman Setup

1. **Import Collection:**
   - Create a new Postman collection called "Raavan AI Backend"

2. **Add Requests:**
   - **Health Check:** GET `http://localhost:8000/health`
   - **Chat:** POST `http://localhost:8000/api/chat` with JSON body
   - **Astrology (Planets Only):** POST `http://localhost:8000/api/astrology` with JSON body
   - **Astrology (Full Reading):** POST `http://localhost:8000/api/astrology-reading` with JSON body

3. **Set Environment Variables:**
   - Create a Postman environment with variable `BASE_URL` = `http://localhost:8000`
   - Replace hardcoded URLs with `{{BASE_URL}}/api/chat`, etc.

---

## Environment Variables

Create a `.env` file in the project root:

```bash
# Groq API Key (Required)
GROQ_API_KEY=your_groq_api_key_here

# CORS Origins (Optional, default: *)
CORS_ORIGINS=http://localhost:3000,http://localhost:5173

# App Settings
APP_NAME=Raavan AI Backend
APP_VERSION=1.0.0
```

---

## Running the Backend

**Development:**
```bash
uvicorn src.app.main:app --host localhost --port 8000 --reload
```

**Production:**
```bash
uvicorn src.app.main:app --host 0.0.0.0 --port 8000
```

---

## Key Features

✅ **RAG-based Chatbot:** Retrieves Ramayana context from ChromaDB and generates responses  
✅ **Raavan Persona:** LLM responses are in Raavan's character voice  
✅ **Astrology Calculations:** Computes planetary positions using Swiss Ephemeris  
✅ **Astrology Readings:** AI-powered Vedic astrology interpretations with personality traits, career insights, and future predictions  
✅ **CORS Enabled:** Ready for frontend integration  
✅ **Error Handling:** Comprehensive error messages with HTTP status codes  
✅ **Modular Architecture:** Clean separation of routes, controllers, services, and schemas

---

## Support & Debugging

**Check Server Status:**
```bash
curl http://localhost:8000/health
```

**View Logs:**
Watch the terminal where the uvicorn server is running for real-time logs.

**Common Issues:**

| Issue | Solution |
|-------|----------|
| Port 8000 already in use | Kill process: `Get-Process python \| Stop-Process -Force` or use `--port 8001` |
| CORS errors on frontend | Ensure `CORS_ORIGINS` env var includes your frontend URL |
| Invalid date format | Use YYYY-MM-DD for `dob`, HH:MM for `time` |
| Groq API key error | Verify `GROQ_API_KEY` is set in `.env` file |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-04-15 | Initial release with Chat and Astrology endpoints |

