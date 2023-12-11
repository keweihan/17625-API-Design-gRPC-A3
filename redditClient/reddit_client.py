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

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = reddit_pb2_grpc.RedditStub(channel)
        print("-------------- GetFeature --------------")
        retrieve_post(stub, "1")
        print("-------------- ListFeatures --------------")
        # Todo
        print("-------------- RecordRoute --------------")
        # Todo
        print("-------------- RouteChat --------------")
        # Todo


if __name__ == "__main__":
    logging.basicConfig()
    run()
