import sqlite3


class Memory:
    def __init__(self):
        self.conn = sqlite3.connect("loki_memory.db")
        self.init_db()

    def init_db(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT NOT NULL,
            value TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        self.conn.commit()

    def remember(self, data):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO memory (key, value) VALUES (?, ?)", (data.key, data.value)
        )

    def recall(self):
    #TODO: Make Loki recall everything in his brain
