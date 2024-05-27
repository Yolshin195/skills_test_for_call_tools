import unittest

from task_one.db import execute


class TestDatabase(unittest.IsolatedAsyncioTestCase):

    async def test_articles_loaded(self):
        articles = await execute("SELECT * FROM article")
        self.assertTrue(len(articles) == 5)

    async def test_comments_loaded(self):
        comments = await execute("SELECT * FROM comment")
        self.assertTrue(len(comments) == 9)


if __name__ == '__main__':
    unittest.main()
