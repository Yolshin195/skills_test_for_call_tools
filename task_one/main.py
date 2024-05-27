import asyncio

from task_one.db import execute


async def get_articles_without_comments():
    articles = await execute("""
            SELECT article.id, article.title, article.text 
            FROM article 
            WHERE NOT EXISTS (
                SELECT 1 
                FROM comment 
                WHERE article.id = comment.article_id
            )
        """)
    return articles


async def main():
    articles = await get_articles_without_comments()
    for article in articles:
        print(article)


if __name__ == "__main__":
    asyncio.run(main())
