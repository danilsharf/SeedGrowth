from fastapi import FastAPI
from pydantic import BaseModel
from app.db import supabase
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EntryCreate(BaseModel):
    raw_text: str
@app.get("/")
def root():
    return {"message": "SeedGrowth API"}

@app.get("/test-db")
def test_db():
    result = (
        supabase
        .table("daily_entries")
        .select("*")
        .limit(5)
        .execute()
    )
    return result.data

@app.get("/goals/current")
def get_current_goal():
    response = (
        supabase
        .table("goals")
        .select("*")
        .eq("status", "active")
        .limit(1)
        .execute()
    )
    return response.data[0] if response.data else None

@app.get("/entries")
def get_entries():
    result = (
        supabase
        .table("daily_entries")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )
    return result.data

@app.post("/entries")
def create_entry(entry: EntryCreate):
    result = (
        supabase
        .table("daily_entries")
        .insert({
            "raw_text": entry.raw_text
        })
        .execute()
    )
    return result.data

@app.delete("/entries/{entry_id}")
def delete_entry(entry_id: str):
    result = (
        supabase
        .table("daily_entries")
        .delete()
        .eq("id", entry_id)
        .execute()
    )
    return {"success": True}