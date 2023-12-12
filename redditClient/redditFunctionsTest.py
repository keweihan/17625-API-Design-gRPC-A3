import unittest
from unittest.mock import MagicMock
import reddit_client
import redditFunctions

# mock data
mock_post = reddit_client.RedditPost(id="post1", title="Mock Post", text="This is a mock post")
mock_comments = [
    reddit_client.RedditComment(id="comment1", text="Mock Comment 1", score=100),
    reddit_client.RedditComment(id="comment2", text="Mock Comment 2", score=5),
    reddit_client.RedditComment(id="comment3", text="Mock Comment 3", score=3)
]

mock_comments_empty = []

class TestRedditFunctions(unittest.TestCase):
    def setUp(self):
        # Set up mock RedditServer and stub functions
        mock_client = reddit_client.RedditServer()
        mock_client.retrieve_post = MagicMock(return_value=mock_post)
        mock_client.retrieve_comments = MagicMock(return_value=mock_comments)
        mock_client.expand_comment = MagicMock(return_value=mock_comments)

    # Post object should be the same as call to client
    def test_retrieve_post(self):
        mock_client = reddit_client.RedditServer()
        mock_client.retrieve_post = MagicMock(return_value=mock_post)
        
        post = redditFunctions.retrieve_post(mock_client, "post1")
        self.assertEqual(post.id, "post1")
        self.assertEqual(post.title, "Mock Post")
        self.assertEqual(post.text, "This is a mock post")
        
    # Assuming client has correct implementation, this function should return same value objects as client
    def test_retrieve_most_upvoted_comments(self):
        mock_client = reddit_client.RedditServer()
        mock_client.retrieve_comments = MagicMock(return_value=mock_comments)

        comments = redditFunctions.retrieve_most_upvoted_comments(mock_client, "post1", 3)
        self.assertEqual(len(comments), 3)
        self.assertEqual(comments[0].id, "comment1")
        self.assertEqual(comments[1].id, "comment2")
        self.assertEqual(comments[2].id, "comment3")
        
        self.assertEqual(comments[0].score, 100)
        self.assertEqual(comments[1].score, 5)
        self.assertEqual(comments[2].score, 3)

    # If most upvoted has no replies, Should return empty.
    def test_expand_most_upvoted(self):
        mock_client = reddit_client.RedditServer()
        mock_client.expand_comment = MagicMock(return_value=mock_comments_empty)
        
        comments = redditFunctions.expand_most_upvoted(mock_client, "post1", 2)
        self.assertEqual(len(comments), 0)

    # If most upvoted has no replies, Should return None.
    def test_most_upvoted_subcomment(self):
        mock_client = reddit_client.RedditServer()
        mock_client.expand_comment = MagicMock(return_value=mock_comments_empty)
        
        comment = redditFunctions.most_upvoted_subcomment(mock_client, "post1")
        
        self.assertIsNone(comment)

if __name__ == '__main__':
    unittest.main()
