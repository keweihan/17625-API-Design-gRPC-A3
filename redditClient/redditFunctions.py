import reddit_client
from typing import List

def retrieve_post(client: reddit_client.RedditServer, post_id) -> reddit_client.RedditPost:
    """
    Retrieve a post
    """
    return client.retrieve_post(post_id) 

def retrieve_most_upvoted_comments(client: reddit_client.RedditServer, post_id, number) -> List[reddit_client.RedditPost]:
    """
    Retrieve most upvoted comments under the post
    """
    return client.retrieve_comments(post_id, number) 
    

def expand_most_upvoted(client: reddit_client.RedditServer, post_id, number) -> List[reddit_client.RedditPost]:
    """
    Expand the most upvoted comment
    """
    comments = client.retrieve_comments(post_id, number)
    if not comments:
        return []

    # First comment is most upvoted one
    most_upvoted_comment_id = comments[0].id
    return client.expand_comment(most_upvoted_comment_id, number)

def most_upvoted_subcomment(client: reddit_client.RedditServer, post_id) -> reddit_client.RedditPost:
    """
    Return the most upvoted reply under the most upvoted comment, or None if there are no comments or
    no replies under the most upvoted one.
    """
    comments = client.retrieve_comments(post_id, 1)
    if not comments:
        return None

    # Retrieve the most upvoted comment and expand it
    most_upvoted_comment_id = comments[0].id
    replies = client.expand_comment(most_upvoted_comment_id, 1)

    return replies[0] if replies else None


def run():
    client = reddit_client.RedditServer()
    print("-------------- Get Post --------------")
    print(str(retrieve_post(client, "post1")))
    print("-------------- Get Most Upvoted --------------")
    print(str(retrieve_most_upvoted_comments(client, "post1", 2)))
    print("-------------- Expand most upvoted --------------")
    print(expand_most_upvoted(client, "post1", 2))
    print("-------------- Get Single most upvoted --------------")
    print(most_upvoted_subcomment(client, "post1"))
    
if __name__ == "__main__":
    run()
