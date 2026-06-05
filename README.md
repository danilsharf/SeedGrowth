# SeedGrowth

AI-powered personal growth and journaling platform.

## Architecture

```text
Browser
   ↓
Next.js
   ↓
FastAPI
   ↓
Supabase
```

## Accessing the Application

### Backend

Start the backend:

```bash
cd backend

source .venv/bin/activate

uvicorn app.main:app --reload
```

Backend API:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

OpenAPI schema:

```text
http://localhost:8000/openapi.json
```

### Frontend

Start the frontend:

```bash
cd frontend

npm install
npm run dev
```

Open in browser:

```text
http://localhost:3000
```

## Current API Endpoints

### Create Entry

```http
POST /entries
```

Example request:

```json
{
  "raw_text": "Worked on FastAPI today"
}
```

### Get Entries

```http
GET /entries
```

Returns all journal entries.

## Tech Stack

### Backend

- Python
- FastAPI
- Supabase
- PostgreSQL

### Frontend

- Next.js
- React
- TypeScript

### AI

- OpenAI API
- Embeddings
- RAG (planned)

## Progress

- [x] Database schema
- [x] FastAPI setup
- [x] Supabase integration
- [x] Create Entry API
- [ ] Get Entries API
- [ ] Frontend dashboard
- [ ] OpenAI integration
- [ ] Embeddings
- [ ] RAG insights

## Author

Dan Sharf