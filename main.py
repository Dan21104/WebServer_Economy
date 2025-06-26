from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import init_db, save_entry
from models import Entry
from datetime import datetime, timezone

app = FastAPI()

app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")

init_db()

@app.get("/api/transactions")
def get_transactions():
    from database import get_all_entries
    return get_all_entries()

@app.post("/api/entry")  
def create_entry(entry: Entry):
    timestamp = datetime.now(timezone.utc)
    save_entry(entry.amount, entry.location, timestamp)
    return {"status": "ok", "timestamp": timestamp}
