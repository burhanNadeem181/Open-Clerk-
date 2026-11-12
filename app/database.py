import sqlite3
from pathlib import Path

DB_PATH = Path("openclerk.db")


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                business TEXT NOT NULL,
                message TEXT NOT NULL,
                priority TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def save_lead(*, name, email, business, message, priority):
    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO leads (name, email, business, message, priority)
            VALUES (?, ?, ?, ?, ?)
            """,
            (name, email, business, message, priority),
        )
        row = connection.execute(
            "SELECT * FROM leads WHERE id = ?", (cursor.lastrowid,)
        ).fetchone()
        return dict(row)


def list_leads():
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT * FROM leads ORDER BY id DESC"
        ).fetchall()
        return [dict(row) for row in rows]
