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

    def remember(self, key, value):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO memory (key, value) VALUES (?, ?)", (key, value))
        self.conn.commit()

    def recall(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM memory")
        memory = []
        for row in cursor:
            memory.append(f"{row[1]}:{row[2]}")
        return memory
