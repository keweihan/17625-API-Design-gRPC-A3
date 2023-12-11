"""The Python implementation of the gRPC route guide client."""

from __future__ import print_function

import logging
import random

import grpc
import reddit_pb2
import reddit_pb2_grpc

def retrieve_post(stub: reddit_pb2_grpc.RedditStub, post_id: str):
    response = stub.RetrievePost(reddit_pb2.PostID(id=post_id))
    print("Received post %s" % (response.title))
    
def upvote_post(stub: reddit_pb2_grpc.RedditStub, post_id: str):
    response = stub.UpvotePost(reddit_pb2.PostID(id=post_id))
    print(f"Received post {response.title} has {response.score} votes")
    
def create_empty_post(stub: reddit_pb2_grpc.RedditStub):
    response = stub.CreatePost(reddit_pb2.CreatePostRequest())
    print("Received post %s" % (response.id))

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = reddit_pb2_grpc.RedditStub(channel)
        print("-------------- GetFeature --------------")
        retrieve_post(stub, "post1")
        print("-------------- Empty Post --------------")
        create_empty_post(stub)
        print("-------------- Upvote Post --------------")
        upvote_post(stub, "post1")
        print("-------------- RouteChat --------------")
        # Todo


if __name__ == "__main__":
    logging.basicConfig()
    run()
