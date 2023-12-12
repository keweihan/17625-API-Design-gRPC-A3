"""The Python implementation of the gRPC route guide client."""

from __future__ import print_function

import logging
import random

import grpc
from reddit_pb2 import *
import reddit_pb2_grpc

from typing import List

# Low level interface 
class RedditServer:
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = reddit_pb2_grpc.RedditStub(self.channel)
    
    # Call when done.
    def close(self):
        if self.channel:
            self.channel.close()
            
    def retrieve_comments(self, post_id: str, num: int) -> List[Comment]:
        arguments = RetrieveCommentRequest(post=PostID(id=post_id), number=num)
        comments = self.stub.RetrieveComments(arguments)
        return comments
            
    def retrieve_post(self, post_id: str) -> Post:
        response = self.stub.RetrievePost(PostID(id=post_id))
        return response
        
    def upvote_post(self, post_id: str) -> Post:
        response = self.stub.UpvotePost(PostID(id=post_id))
        return response
    
    def downvote_post(self, post_id: str) -> Post:
        response = self.stub.DownvotePost(PostID(id=post_id))
        return response
        
    def create_post(self, postReq :CreatePostRequest) -> Post:
        response = self.stub.CreatePost(postReq)
        return response

    def create_comment_post(self, content: str, post_id: str) -> Comment:
        response = self.stub.CreateComment(CreateCommentRequest(text=content, parent_post_id=PostID(id=post_id)))
        return response
    
    def create_comment_comm(self, content: str, comment_id: str) -> Comment:
        response = self.stub.CreateComment(CreateCommentRequest(text=content, parent_comment_id=CommentID(id=comment_id)))
        return response

    def expand_comment(self, comment_id: str, num: int) -> List[Comment]:
        arguments = ExpandCommentBranchRequest(comment = CommentID(id=comment_id), number=num)
        comments = self.stub.ExpandComment(arguments)
        return comments
        
    def upvote_comment(self, comment_id: str) -> Comment:
        response = self.stub.UpvoteComment(CommentID(id=comment_id))
        return response

    def downvote_comment(self, comment_id: str) -> Comment:
        response = self.stub.UpvoteComment(CommentID(id=comment_id))
        return response
    
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
    logging.basicConfig()
    run()
