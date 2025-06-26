import sqlite3

def init_db():
    conn = sqlite3.connect("transactions.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            location TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_entry(amount, location, timestamp):
    conn = sqlite3.connect("transactions.db")
    c = conn.cursor()
    c.execute("INSERT INTO transactions (amount, location, timestamp) VALUES (?, ?, ?)",
              (amount, location, timestamp.isoformat()))
    conn.commit()
    conn.close()

def get_all_entries():
    conn = sqlite3.connect("transactions.db")
    c = conn.cursor()
    c.execute("SELECT amount, location, timestamp FROM transactions")
    rows = c.fetchall()
    conn.close()
    return [{"amount": r[0], "location": r[1], "timestamp": r[2]} for r in rows]
