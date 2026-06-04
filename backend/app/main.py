from fastapi import FastAPI
from pydantic import BaseModel
from app.db import supabase

app = FastAPI()

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