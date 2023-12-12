"""The Python implementation of the gRPC route guide client."""

from __future__ import print_function

import logging
import random

import grpc
from reddit_pb2 import *
import reddit_pb2_grpc

from typing import List, Dict

class RedditPost:
    def __init__(self, grpc_post=None, id=None, title=None, text=None, video=None, img=None, 
                 author=None, score=None, state=None, pub_date=None, subreddit=None):
        if grpc_post:
            # Construct from a gRPC Post object
            self.id = grpc_post.id.id if grpc_post.id else None
            self.title = grpc_post.title
            self.text = grpc_post.text
            self.video = grpc_post.video
            self.img = grpc_post.img
            self.author = grpc_post.author
            self.score = grpc_post.score
            self.state = grpc_post.state
            self.pub_date = grpc_post.pub_date
            self.subreddit = grpc_post.subreddit.name if grpc_post.subreddit else None
        else:
            # Construct from individual parameters
            self.id = id
            self.title = title
            self.text = text
            self.video = video
            self.img = img
            self.author = author
            self.score = score
            self.state = state
            self.pub_date = pub_date
            self.subreddit = subreddit
    
    def __str__(self):
        return (f"RedditPost(id={self.id}, title={self.title}, text={self.text}, video={self.video}, "
                f"img={self.img}, author={self.author}, score={self.score}, state={self.state}, "
                f"pub_date={self.pub_date}, subreddit={self.subreddit})")


class RedditComment:
    def __init__(self, grpc_comment=None, id=None, text=None, author=None, score=None, 
                 state=None, pub_date=None, parent_post_id=None, parent_comment_id=None, has_replies=None):
        if grpc_comment:
            # Construct from a gRPC Comment object
            self.id = grpc_comment.id.id if grpc_comment.id else None
            self.text = grpc_comment.text
            self.author = grpc_comment.author
            self.score = grpc_comment.score
            self.state = grpc_comment.state
            self.pub_date = grpc_comment.pub_date
            self.parent_post_id = grpc_comment.parent_post_id.id if grpc_comment.parent_post_id else None
            self.parent_comment_id = grpc_comment.parent_comment_id.id if grpc_comment.parent_comment_id else None
            self.has_replies = grpc_comment.hasReplies
        else:
            # Construct from individual parameters
            self.id = id
            self.text = text
            self.author = author
            self.score = score
            self.state = state
            self.pub_date = pub_date
            self.parent_post_id = parent_post_id
            self.parent_comment_id = parent_comment_id
            self.has_replies = has_replies
    
    def __str__(self):
        return (f"RedditComment(id={self.id}, text={self.text}, author={self.author}, "
                f"score={self.score}, state={self.state}, pub_date={self.pub_date}, "
                f"parent_post_id={self.parent_post_id}, parent_comment_id={self.parent_comment_id}, "
                f"has_replies={self.has_replies})")

# Low level interface 
class RedditServer:
    def __init__(self, port="50051"):
        self.channel = grpc.insecure_channel(f"localhost:{port}")
        self.stub = reddit_pb2_grpc.RedditStub(self.channel)
    
    # Call when done.
    def close(self):
        if self.channel:
            self.channel.close()
            
    def retrieve_comments(self, post_id: str, num: int) -> List[RedditComment]:
        arguments = RetrieveCommentRequest(post=PostID(id=post_id), number=num)
        comments = self.stub.RetrieveComments(arguments)
        redditComments = [RedditComment(grpc_comment=c) for c in comments]
        return redditComments
            
    def retrieve_post(self, post_id: str) -> RedditPost:
        response = self.stub.RetrievePost(PostID(id=post_id))
        return RedditPost(grpc_post=response)
        
    def upvote_post(self, post_id: str) -> RedditPost:
        response = self.stub.UpvotePost(PostID(id=post_id))
        return RedditPost(grpc_post=response)
    
    def downvote_post(self, post_id: str) -> RedditPost:
        response = self.stub.DownvotePost(PostID(id=post_id))
        return RedditPost(grpc_post=response)
        
    def create_post(self, postReq :CreatePostRequest) -> RedditPost:
        response = self.stub.CreatePost(postReq)
        return RedditPost(grpc_post=response)

    def create_comment_post(self, content: str, post_id: str) -> RedditComment:
        response = self.stub.CreateComment(CreateCommentRequest(text=content, parent_post_id=PostID(id=post_id)))
        return RedditComment(grpc_comment=response)
    
    def create_comment_comm(self, content: str, comment_id: str) -> RedditComment:
        response = self.stub.CreateComment(CreateCommentRequest(text=content, parent_comment_id=CommentID(id=comment_id)))
        return RedditComment(grpc_comment=response)

    def expand_comment(self, comment_id: str, num: int) -> List[RedditComment]:
        arguments = ExpandCommentBranchRequest(comment = CommentID(id=comment_id), number=num)
        comments = self.stub.ExpandComment(arguments)
        redditComments = [RedditComment(grpc_comment=c) for c in comments]
        return redditComments
        
    def upvote_comment(self, comment_id: str) -> RedditComment:
        response = self.stub.UpvoteComment(CommentID(id=comment_id))
        return RedditComment(grpc_comment=response)

    def downvote_comment(self, comment_id: str) -> RedditComment:
        response = self.stub.UpvoteComment(CommentID(id=comment_id))
        return RedditComment(grpc_comment=response)
    
def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    client = RedditServer()
    # print("-------------- GetFeature --------------")
    # client.retrieve_post("post1")
    # print("-------------- Upvote Post --------------")
    # client("post1")
    # print("-------------- Retrieve Comments --------------")
    # client.retrieve_comments("post1")
    print("-------------- Create Comments --------------")
    print(str(client.create_comment_comm("hello", "comment1")))
    # print("-------------- Expand Comment --------------")
    # client.expand_comment()
    # print("-------------- Upvote Comment --------------")
    # client.upvote_comment("comment1")


if __name__ == "__main__":
    run()
