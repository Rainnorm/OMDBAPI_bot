import aiosqlite
from datetime import datetime
DB_NAME = 'bot.db'


async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                         id INTEGER PRIMARY KEY,
                         username TEXT,
                         created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                            )
                        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS history (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            user_id INTEGER,
                                            movie TEXT,
                                            created_at TEXT,
                                            UNIQUE(user_id, movie)
                                        )
                        """)
        await db.commit()


async def save_user(user_id, username):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
                        """
                        INSERT INTO users (id, username)
                        VALUES (?, ?)
                        ON CONFLICT(id) DO UPDATE SET
                                    username = excluded.username
                        """,
                        (user_id, username)
                        )
        await db.commit()


async def save_history(user_id, movie):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            """
            INSERT INTO history (user_id, movie, created_at)
            VALUES (?, ?, ?)
            ON CONFLICT(user_id, movie)
            DO UPDATE SET created_at = excluded.created_at;
            """,
            (user_id, movie, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )

        await db.commit()


async def get_history(user_id):
    async with aiosqlite.connect("bot.db") as db:
        cursor = await db.execute(
            """
            SELECT id, user_id, movie, created_at
            FROM history
            WHERE user_id = ?
            ORDER BY created_at DESC
            """,
            (user_id,)
        )

        rows = await cursor.fetchall()
        return rows
