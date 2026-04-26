import asyncpg
import os
from dotenv import load_dotenv
import asyncio
import asyncpg


load_dotenv()


DB_URL = os.getenv('DB_URL')

async def create_pool():
    return await asyncpg.create_pool(DB_URL)

async def init_db(pool):


    if not DB_URL:
        raise RuntimeError("DB_URL is not set")

    # retry connect
    for i in range(15):
        try:
            pool = await asyncpg.create_pool(DB_URL)
            print("DB connected")
            break
        except Exception as e:
            print(f"DB not ready ({i}), retrying...", e)
            await asyncio.sleep(2)

    if pool is None:
        raise RuntimeError("Failed to connect to DB")

    async with pool.acquire() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id BIGINT PRIMARY KEY,
                username TEXT,
                created_at TIMESTAMPTZ DEFAULT NOW()
            )
        """)

        await conn.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                user_id BIGINT,
                movie TEXT,
                created_at TIMESTAMPTZ DEFAULT NOW(),
                UNIQUE(user_id, movie)
            )
        """)


async def save_user(pool, user_id: int, username: str | None):
    async with pool.acquire() as conn:
        await conn.execute("""
            INSERT INTO users (id, username)
            VALUES ($1, $2)
            ON CONFLICT (id)
            DO UPDATE SET username = EXCLUDED.username
        """, user_id, username)
        


async def save_history(pool, user_id: int, movie: str):
    async with pool.acquire() as conn:
        await conn.execute("""
            INSERT INTO history (user_id, movie, created_at)
            VALUES ($1, $2, NOW())
            ON CONFLICT (user_id, movie)
            DO UPDATE SET created_at = NOW()
        """, user_id, movie)
        

async def get_history(pool, user_id: int):
    
    async with pool.acquire() as conn:
        rows = await conn.fetch("""
            SELECT id, user_id, movie, created_at
            FROM history
            WHERE user_id = $1
            ORDER BY created_at DESC
        """, user_id)

        return rows