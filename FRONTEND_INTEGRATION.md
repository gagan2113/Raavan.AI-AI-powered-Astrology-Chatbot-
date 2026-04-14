# Frontend Integration Guide - Raavan AI Updates

## Overview

This document outlines all frontend changes needed to integrate with the updated Raavan AI backend, specifically the new Astrology Reading feature and enhanced API endpoints.

---

## API Endpoints Summary

### Existing Endpoints (No Changes Required)

**1. Health Check**
- **URL:** `GET /health`
- **Response:** `{ "status": "ok" }`

**2. Chat Endpoint**
- **URL:** `POST /api/chat`
- **Request:** `{ "user_id": string, "message": string }`
- **Response:** `{ "answer": string }`

### New/Updated Endpoints

**3. Astrology (Planetary Positions Only)**
- **URL:** `POST /api/astrology`
- **Request:** `{ "name": string, "dob": string (YYYY-MM-DD), "time": string (HH:MM), "location": string }`
- **Response:** `{ "planets": { [planetName]: PlanetPosition } }`

**4. Astrology Reading (NEW - With Interpretation)**
- **URL:** `POST /api/astrology-reading`
- **Request:** `{ "name": string, "dob": string (YYYY-MM-DD), "time": string (HH:MM), "location": string }`
- **Response:** `{ "name": string, "dob": string, "time": string, "location": string, "planets": {...}, "reading": string }`

---

## Type Definitions

Add these TypeScript types to your frontend project:

```typescript
// types/api.ts

// Chat Types
export interface ChatRequest {
  user_id: string;
  message: string;
}

export interface ChatResponse {
  answer: string;
}

// Astrology Types
export interface PlanetPosition {
  degrees: number;
  sign: number;
  sign_name: string;
  degree_in_sign: number;
  emoji: string;
}

export interface AstrologyRequest {
  name: string;
  dob: string; // YYYY-MM-DD
  time: string; // HH:MM
  location: string;
}

export interface AstrologyResponse {
  planets: Record<string, PlanetPosition>;
}

export interface AstrologyReadingResponse {
  name: string;
  dob: string;
  time: string;
  location: string;
  planets: Record<string, PlanetPosition>;
  reading: string; // Full astrology reading/interpretation
}

export interface ApiError {
  detail: string | Array<{
    type: string;
    loc: string[];
    msg: string;
    input: Record<string, any>;
  }>;
}
```

---

## API Service Layer

Create a robust API service to handle all requests:

```typescript
// services/api.ts

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

class ApiService {
  // Health Check
  async checkHealth(): Promise<boolean> {
    try {
      const response = await fetch(`${API_BASE_URL}/health`);
      return response.status === 200;
    } catch {
      return false;
    }
  }

  // Chat Endpoint
  async sendChat(userId: string, message: string): Promise<string> {
    const response = await fetch(`${API_BASE_URL}/api/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_id: userId, message })
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Chat request failed');
    }

    const data: ChatResponse = await response.json();
    return data.answer;
  }

  // Astrology - Planets Only
  async getAstrologyPlanets(
    name: string,
    dob: string,
    time: string,
    location: string
  ): Promise<Record<string, PlanetPosition>> {
    const response = await fetch(`${API_BASE_URL}/api/astrology`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, dob, time, location })
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Astrology request failed');
    }

    const data: AstrologyResponse = await response.json();
    return data.planets;
  }

  // Astrology - Full Reading with Interpretation (NEW)
  async getAstrologyReading(
    name: string,
    dob: string,
    time: string,
    location: string
  ): Promise<AstrologyReadingResponse> {
    const response = await fetch(`${API_BASE_URL}/api/astrology-reading`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, dob, time, location })
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Astrology reading request failed');
    }

    const data: AstrologyReadingResponse = await response.json();
    return data;
  }
}

export const apiService = new ApiService();
```

---

## React Component Examples

### 1. Chat Component (Existing - No Changes)

```tsx
// components/ChatBox.tsx

import { useState } from 'react';
import { apiService } from '../services/api';

export function ChatBox() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const answer = await apiService.sendChat('user123', message);
      setResponse(answer);
      setMessage('');
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to send message');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-box">
      <form onSubmit={handleSendMessage}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Ask Raavan about the Ramayana..."
          disabled={loading}
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Asking...' : 'Ask'}
        </button>
      </form>

      {error && <div className="error">{error}</div>}
      {response && (
        <div className="response">
          <h3>Raavan's Answer:</h3>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}
```

### 2. Astrology Planets Component (Existing - No Changes)

```tsx
// components/AstrologyPlanets.tsx

import { useState } from 'react';
import { apiService } from '../services/api';
import { PlanetPosition } from '../types/api';

export function AstrologyPlanets() {
  const [formData, setFormData] = useState({
    name: '',
    dob: '',
    time: '12:00',
    location: ''
  });
  const [planets, setPlanets] = useState<Record<string, PlanetPosition> | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const result = await apiService.getAstrologyPlanets(
        formData.name,
        formData.dob,
        formData.time,
        formData.location
      );
      setPlanets(result);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to get planets');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="astrology-planets">
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
          {loading ? 'Calculating...' : 'Get Planetary Positions'}
        </button>
      </form>

      {error && <div className="error">{error}</div>}
      {planets && (
        <div className="planets-grid">
          {Object.entries(planets).map(([name, position]) => (
            <div key={name} className="planet-card">
              <div className="planet-emoji">{position.emoji}</div>
              <h3>{name}</h3>
              <p>{position.sign_name}</p>
              <p className="degrees">{position.degrees.toFixed(2)}°</p>
              <p className="in-sign">{position.degree_in_sign.toFixed(2)}° in {position.sign_name}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
```

### 3. NEW - Astrology Reading Component (UPDATED)

```tsx
// components/AstrologyReading.tsx

import { useState } from 'react';
import { apiService } from '../services/api';
import { AstrologyReadingResponse, PlanetPosition } from '../types/api';

export function AstrologyReading() {
  const [formData, setFormData] = useState({
    name: '',
    dob: '',
    time: '12:00',
    location: ''
  });
  const [readingData, setReadingData] = useState<AstrologyReadingResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [showPlanets, setShowPlanets] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const result = await apiService.getAstrologyReading(
        formData.name,
        formData.dob,
        formData.time,
        formData.location
      );
      setReadingData(result);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to generate reading');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="astrology-reading">
      <form onSubmit={handleSubmit} className="reading-form">
        <div className="form-group">
          <label>Full Name *</label>
          <input
            type="text"
            placeholder="Enter your full name"
            value={formData.name}
            onChange={(e) => setFormData({...formData, name: e.target.value})}
            required
          />
        </div>

        <div className="form-row">
          <div className="form-group">
            <label>Date of Birth *</label>
            <input
              type="date"
              value={formData.dob}
              onChange={(e) => setFormData({...formData, dob: e.target.value})}
              required
            />
          </div>

          <div className="form-group">
            <label>Time of Birth *</label>
            <input
              type="time"
              value={formData.time}
              onChange={(e) => setFormData({...formData, time: e.target.value})}
              required
            />
          </div>
        </div>

        <div className="form-group">
          <label>Place of Birth *</label>
          <input
            type="text"
            placeholder="e.g., Mumbai, India"
            value={formData.location}
            onChange={(e) => setFormData({...formData, location: e.target.value})}
            required
          />
        </div>

        <button type="submit" disabled={loading} className="submit-btn">
          {loading ? 'Generating Your Cosmic Reading...' : 'Get Full Astrology Reading'}
        </button>
      </form>

      {error && (
        <div className="error-box">
          <strong>Error:</strong> {error}
        </div>
      )}

      {readingData && (
        <div className="reading-result">
          <div className="reading-header">
            <h2>Your Cosmic Reading</h2>
            <p className="reading-meta">
              {readingData.name} • {readingData.dob} • {readingData.time} • {readingData.location}
            </p>
          </div>

          {/* Toggle Planets Section */}
          <div className="planets-toggle">
            <button
              onClick={() => setShowPlanets(!showPlanets)}
              className="toggle-btn"
            >
              {showPlanets ? '▼ Hide Planetary Positions' : '▶ Show Planetary Positions'}
            </button>

            {showPlanets && (
              <div className="planets-display">
                <div className="planets-grid">
                  {Object.entries(readingData.planets).map(([name, position]) => (
                    <div key={name} className="planet-item">
                      <span className="emoji">{position.emoji}</span>
                      <span className="name">{name}</span>
                      <span className="sign">{position.sign_name}</span>
                      <span className="degrees">{position.degrees.toFixed(0)}°</span>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Main Reading Section */}
          <div className="reading-content">
            <div className="reading-text" style={{whiteSpace: 'pre-wrap', lineHeight: '1.8'}}>
              {readingData.reading}
            </div>
          </div>

          {/* Export Option */}
          <div className="reading-actions">
            <button onClick={() => downloadReading(readingData)} className="download-btn">
              📥 Download Reading
            </button>
            <button onClick={() => copyReading(readingData)} className="copy-btn">
              📋 Copy to Clipboard
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

// Helper Functions
function downloadReading(data: AstrologyReadingResponse) {
  const content = `Your COSMIC ASTROLOGY READING
=====================================

Name: ${data.name}
Date of Birth: ${data.dob}
Time of Birth: ${data.time}
Place of Birth: ${data.location}

PLANETARY POSITIONS
${Object.entries(data.planets)
  .map(([name, pos]) => `${pos.emoji} ${name}: ${pos.degrees.toFixed(2)}° in ${pos.sign_name}`)
  .join('\n')}

=====================================

${data.reading}

Generated by Raavan AI
https://raavan-ai.com`;

  const blob = new Blob([content], { type: 'text/plain' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = `${data.name}_astrologyreading.txt`;
  link.click();
  URL.revokeObjectURL(url);
}

function copyReading(data: AstrologyReadingResponse) {
  const content = `${data.name} - ${data.dob}\n\n${data.reading}`;
  navigator.clipboard.writeText(content).then(() => {
    alert('Reading copied to clipboard!');
  });
}
```

---

## State Management (Redux Example)

If using Redux, add these reducers:

```typescript
// redux/slices/astrologySlice.ts

import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { apiService } from '../../services/api';
import { AstrologyReadingResponse } from '../../types/api';

export const fetchAstrologyReading = createAsyncThunk(
  'astrology/fetchReading',
  async (
    params: {
      name: string;
      dob: string;
      time: string;
      location: string;
    },
    { rejectWithValue }
  ) => {
    try {
      return await apiService.getAstrologyReading(
        params.name,
        params.dob,
        params.time,
        params.location
      );
    } catch (error) {
      return rejectWithValue(error instanceof Error ? error.message : 'Unknown error');
    }
  }
);

interface AstrologyState {
  reading: AstrologyReadingResponse | null;
  loading: boolean;
  error: string | null;
}

const initialState: AstrologyState = {
  reading: null,
  loading: false,
  error: null
};

const astrologySlice = createSlice({
  name: 'astrology',
  initialState,
  reducers: {
    clearReading: (state) => {
      state.reading = null;
      state.error = null;
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchAstrologyReading.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchAstrologyReading.fulfilled, (state, action) => {
        state.loading = false;
        state.reading = action.payload;
      })
      .addCase(fetchAstrologyReading.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      });
  }
});

export const { clearReading } = astrologySlice.actions;
export default astrologySlice.reducer;
```

Usage in component:
```typescript
import { useDispatch, useSelector } from 'react-redux';
import { fetchAstrologyReading } from '../redux/slices/astrologySlice';

function AstrologyReadingComponent() {
  const dispatch = useDispatch();
  const { reading, loading, error } = useSelector((state) => state.astrology);

  const handleSubmit = (formData) => {
    dispatch(fetchAstrologyReading(formData));
  };

  // ... rest of component
}
```

---

## Environment Configuration

Add to your `.env.local`:

```bash
REACT_APP_API_URL=http://localhost:8000
REACT_APP_API_TIMEOUT=30000
```

For production:
```bash
REACT_APP_API_URL=https://api.raavan-ai.com
REACT_APP_API_TIMEOUT=30000
```

---

## Error Handling Best Practices

```typescript
// utils/errorHandler.ts

export class ApiError extends Error {
  constructor(
    public status: number,
    public detail: string | any,
    message?: string
  ) {
    super(message || detail?.toString());
  }
}

export function handleApiError(error: unknown): string {
  if (error instanceof ApiError) {
    if (Array.isArray(error.detail)) {
      // Validation errors
      return error.detail
        .map((err: any) => `${err.loc.join('.')}: ${err.msg}`)
        .join(', ');
    }
    return error.detail;
  }
  if (error instanceof Error) {
    return error.message;
  }
  return 'An unexpected error occurred';
}
```

---

## Form Validation

```typescript
// utils/validation.ts

export function validateAstrologyForm(data: {
  name: string;
  dob: string;
  time: string;
  location: string;
}): { valid: boolean; errors: Record<string, string> } {
  const errors: Record<string, string> = {};

  if (!data.name?.trim()) {
    errors.name = 'Name is required';
  }

  if (!data.dob) {
    errors.dob = 'Date of birth is required';
  } else if (!/^\d{4}-\d{2}-\d{2}$/.test(data.dob)) {
    errors.dob = 'Invalid date format (use YYYY-MM-DD)';
  }

  if (!data.time) {
    errors.time = 'Time of birth is required';
  } else if (!/^\d{2}:\d{2}$/.test(data.time)) {
    errors.time = 'Invalid time format (use HH:MM)';
  }

  if (!data.location?.trim()) {
    errors.location = 'Location is required';
  }

  return {
    valid: Object.keys(errors).length === 0,
    errors
  };
}
```

---

## CSS Styling Suggestions

```css
/* styles/astrology.css */

.astrology-reading {
  max-width: 900px;
  margin: 2rem auto;
  padding: 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(102, 126, 234, 0.2);
}

.reading-form {
  display: grid;
  gap: 1.5rem;
  margin-bottom: 2rem;
  background: rgba(255, 255, 255, 0.95);
  padding: 2rem;
  border-radius: 8px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group label {
  font-weight: 600;
  color: #333;
  font-size: 0.95rem;
}

.form-group input {
  padding: 0.75rem;
  border: 2px solid #e0e0e0;
  border-radius: 6px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.form-group input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.submit-btn {
  padding: 1rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.submit-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(102, 126, 234, 0.3);
}

.submit-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.reading-result {
  background: rgba(255, 255, 255, 0.95);
  padding: 2rem;
  border-radius: 8px;
  margin-top: 2rem;
}

.reading-header {
  border-bottom: 3px solid #667eea;
  padding-bottom: 1.5rem;
  margin-bottom: 2rem;
}

.reading-header h2 {
  margin: 0 0 0.5rem 0;
  color: #333;
  font-size: 2rem;
}

.reading-meta {
  color: #666;
  font-size: 0.95rem;
  margin: 0;
}

.planets-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}

.planet-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem;
  background: #f5f5f5;
  border-radius: 8px;
  text-align: center;
}

.planet-item .emoji {
  font-size: 2rem;
}

.planet-item .name {
  font-weight: 600;
  color: #333;
}

.planet-item .sign {
  color: #667eea;
  font-weight: 500;
}

.planet-item .degrees {
  color: #999;
  font-size: 0.9rem;
}

.reading-content {
  color: #333;
  line-height: 1.8;
  font-size: 1.05rem;
  margin: 2rem 0;
  padding: 1.5rem;
  background: #fafafa;
  border-left: 4px solid #667eea;
  border-radius: 4px;
}

.error-box {
  background: #fee;
  color: #c33;
  padding: 1rem;
  border-radius: 6px;
  margin: 1rem 0;
  border: 1px solid #fcc;
}

.reading-actions {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 2px solid #e0e0e0;
}

.download-btn,
.copy-btn {
  flex: 1;
  padding: 0.75rem 1rem;
  border: 2px solid #667eea;
  background: white;
  color: #667eea;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.download-btn:hover,
.copy-btn:hover {
  background: #667eea;
  color: white;
}
```

---

## Testing Examples

```typescript
// __tests__/apiService.test.ts

import { apiService } from '../services/api';

describe('ApiService', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('should fetch astrology reading successfully', async () => {
    const mockResponse = {
      name: 'Test User',
      dob: '1990-05-15',
      time: '12:00',
      location: 'Delhi',
      planets: {},
      reading: 'Test reading'
    };

    global.fetch = jest.fn(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve(mockResponse)
      })
    ) as jest.Mock;

    const result = await apiService.getAstrologyReading(
      'Test User',
      '1990-05-15',
      '12:00',
      'Delhi'
    );

    expect(result).toEqual(mockResponse);
    expect(global.fetch).toHaveBeenCalledWith(
      'http://localhost:8000/api/astrology-reading',
      expect.any(Object)
    );
  });

  test('should handle API errors gracefully', async () => {
    global.fetch = jest.fn(() =>
      Promise.resolve({
        ok: false,
        json: () => Promise.resolve({ detail: 'Invalid input' })
      })
    ) as jest.Mock;

    await expect(
      apiService.getAstrologyReading('', '1990-05-15', '12:00', 'Delhi')
    ).rejects.toThrow();
  });
});
```

---

## Summary of Changes

| Feature | Endpoint | Type | Status |
|---------|----------|------|--------|
| Health Check | GET /health | Existing | No changes |
| Chat | POST /api/chat | Existing | No changes |
| Astrology Planets | POST /api/astrology | Existing | No changes |
| **Astrology Reading** | **POST /api/astrology-reading** | **NEW** | **Implement** |

---

## Next Steps for Frontend

1. ✅ Add TypeScript types from this guide
2. ✅ Create API service layer
3. ✅ Implement AstrologyReading component
4. ✅ Add form validation
5. ✅ Setup Redux store (if using Redux)
6. ✅ Add CSS styling
7. ✅ Create unit tests
8. ✅ Configure environment variables
9. ✅ Test with backend API
10. ✅ Deploy to production

---

## Questions & Support

For issues or questions about the API:
- Check [Backend.md](./Backend.md) for detailed endpoint documentation
- Ensure backend is running on `http://localhost:8000`
- Verify API_BASE_URL in environment variables
- Check browser console for CORS errors

