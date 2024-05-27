import asyncpg

from task_one.config import DB_USER, DB_PASSWORD, DB_NAME, DB_HOST, DB_PORT


async def get_database_connection():
    return await asyncpg.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        host=DB_HOST,
        port=DB_PORT
    )


async def execute(request: str):
    conn = await get_database_connection()
    try:
        data = await conn.fetch(request)
    finally:
        await conn.close()

    return data
