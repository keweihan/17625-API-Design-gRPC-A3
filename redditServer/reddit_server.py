"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
from enum import Enum

import argparse

import grpc
import reddit_pb2
import reddit_pb2_grpc

import uuid
import reddit_server_db

# RedditService provides an implementation of the methods of the RedditServicer service.
class RedditService(reddit_pb2_grpc.RedditServicer):
    
    def CreatePost(self, request, context):
        # Generate a unique post ID
        post_id = str(uuid.uuid4())[:4] # take first four characters only - for demo purpose.

        # Extract other post data from the request
        newPost = reddit_pb2.Post(
            id          = reddit_pb2.PostID(id=post_id),
            title       = request.title,
            text        = request.text,
            video       = request.video if request.video else None,
            img         = request.img if request.img else None,
            author      = request.pub_date,
            pub_date    = request.pub_date,
        )

        # Insert the new post into the database
        conn = reddit_server_db.get_db()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO posts (id, title, text, video, img, author, pub_date)
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (post_id, newPost.title, newPost.text, newPost.video, newPost.img, newPost.author, newPost.pub_date)
        )
        conn.commit()
        conn.close()

        # Create and return the Post object
        return newPost
    
    def DownvotePost(self, request, context):
        return super().DownvotePost(request, context)
    
    def UpvotePost(self, request, context):
        return super().UpvotePost(request, context)
    
    def RetrievePost(self, request: reddit_pb2.PostID, context):
        post_id = request.id
        
        # Retrieve from database
        conn = reddit_server_db.get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
        post_data = cur.fetchone()
        conn.close()

        if not post_data:
            return reddit_pb2.Post()        
        
        retrievedData = dict(post_data)
        
        # Create and return the Post object
        # Special values
        post_id = reddit_pb2.PostID(id=retrievedData["id"])
        subreddit = reddit_pb2.Subreddit(name="stubSubreddit", state=reddit_pb2.SubredditState.PUBLIC_SUBREDDIT)
        stateMap = {
            0: reddit_pb2.PostState.NORMAL_POST,
            1: reddit_pb2.PostState.LOCKED_POST,
            2: reddit_pb2.PostState.HIDDEN_POST
        }
        state = stateMap[retrievedData["state"]]
        
        retObj = reddit_pb2.Post(
            id      = post_id, 
            title   = retrievedData["title"], 
            text    = retrievedData["text"],
            author  = retrievedData["author"],
            score   = retrievedData["score"],
            state   = state,
            video   = retrievedData["video"],
            img     = retrievedData["img"],
            pub_date= retrievedData["pub_date"],
            subreddit=subreddit
        )
        
        return retObj
    
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