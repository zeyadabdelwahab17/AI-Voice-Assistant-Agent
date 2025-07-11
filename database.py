import sqlite3

conn = sqlite3.connect("conversations.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    response TEXT,
    status TEXT NOT NULL,         -- 'success', 'error', 'timeout'
    response_time_ms INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

def save_conversation(question, response, status, response_time_ms):
    try:
        cursor.execute(
            "INSERT INTO conversations (question, response, status, response_time_ms) VALUES (?, ?, ?, ?)",
            (question, response, status, response_time_ms)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Database error: {e}")
        return False
    
#pull last N messages (for the memory)
def get_recent_conversation(limit=5):
    cursor.execute(
        "SELECT question, response FROM conversations ORDER BY id DESC LIMIT ?",
        (limit,)
    )
    rows = cursor.fetchall()
    rows.reverse()  # So they appear in the correct order
    return rows
