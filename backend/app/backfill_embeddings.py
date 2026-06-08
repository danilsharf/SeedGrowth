from app.db import supabase
from app.embeddings import create_embedding

response = (
    supabase
    .table("daily_entries")
    .select("id, raw_text")
    .is_("embedding", "null")
    .execute()
)

entries = response.data

print(f"Found {len(entries)} entries without embeddings")

for entry in entries:
    print(f"Processing {entry['id']}")

    embedding = create_embedding(
        entry["raw_text"]
    )

    (
        supabase
        .table("daily_entries")
        .update({
            "embedding": embedding
        })
        .eq("id", entry["id"])
        .execute()
    )

print("Done!")

# RUN: python -m app.backfill_embeddings