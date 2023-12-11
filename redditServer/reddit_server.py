"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import argparse

import grpc
import reddit_pb2
import reddit_pb2_grpc


# RedditService provides an implementation of the methods of the RedditServicer service.
class RedditService(reddit_pb2_grpc.RedditServicer):
    
    def CreatePost(self, request, context):
        return super().CreatePost(request, context)
    
    def DownvotePost(self, request, context):
        return super().DownvotePost(request, context)
    
    def UpvotePost(self, request, context):
        return super().UpvotePost(request, context)
    
    def RetrievePost(self, request, context):
        # Create a PostID object
        post_id = reddit_pb2.PostID(id="bruh")

        # Create a Subreddit object if needed
        subreddit = reddit_pb2.Subreddit(name="exampleSubreddit", state=reddit_pb2.SubredditState.PUBLIC_SUBREDDIT)

        # Create and return the Post object
        return reddit_pb2.Post(
            id=post_id, 
            title="Hello", 
            text="World",
            author="Jim",
            score=10,
            state=reddit_pb2.PostState.NORMAL_POST,
            pub_date="2021-01-01",
            subreddit=subreddit
        )
    
    def CreateComment(self, request, context):
        return super().CreateComment(request, context)
    
    def UpvoteComment(self, request, context):
        return super().UpvoteComment(request, context)
    
    def DownvoteComment(self, request, context):
        return super().DownvoteComment(request, context)
    
    def ExpandComment(self, request, context):
        return super().ExpandComment(request, context)
    
    pass

def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reddit_pb2_grpc.add_RedditServicer_to_server(RedditService(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"Server started on port {port}")
    server.wait_for_termination()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='gRPC Server')
    parser.add_argument('--port', type=int, default=50051, help='The server port')
    args = parser.parse_args()

    serve(args.port)