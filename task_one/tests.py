import unittest

from task_one.db import execute
from task_one.main import get_articles_without_comments


class TestDatabase(unittest.IsolatedAsyncioTestCase):

    async def test_articles_loaded(self):
        articles = await execute("SELECT * FROM article")
        self.assertTrue(len(articles) == 5)

    async def test_comments_loaded(self):
        comments = await execute("SELECT * FROM comment")
        self.assertTrue(len(comments) == 9)

    async def test_get_articles_without_comments(self):
        articles_without_comments = await get_articles_without_comments()
        article_ids = [article['id'] for article in articles_without_comments]
        self.assertTrue(len(articles_without_comments) == 2)
        self.assertListEqual([2, 3], article_ids)


if __name__ == '__main__':
    unittest.main()
