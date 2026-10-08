import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "emotion.db"


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_conn()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS emotion_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emotion TEXT NOT NULL,
        intensity INTEGER NOT NULL,
        content TEXT NOT NULL,
        ai_summary TEXT,
        ai_advice TEXT,
        ai_tags TEXT,
        created_at TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()
