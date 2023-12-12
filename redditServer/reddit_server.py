"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
from enum import Enum

import argparse

import grpc
import reddit_pb2
import reddit_pb2_grpc
import datetime

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
            state       = reddit_pb2.PostState.NORMAL_POST,
            video       = request.video if request.video else None,
            img         = request.img if request.img else None,
            author      = request.author,
            pub_date    = str(datetime.datetime.now()),
        )

        # Insert the new post into the database
        conn = reddit_server_db.get_db()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO posts (id, title, text, video, img, author, pub_date, state)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (post_id, newPost.title, newPost.text, newPost.video, newPost.img, newPost.author, newPost.pub_date, 0)
        )
        conn.commit()
        conn.close()

        # Create and return the Post object
        return newPost
    
    def DownvotePost(self, request, context):
        post_id = request.id
        
        conn = reddit_server_db.get_db()
        cur = conn.cursor()
        cur.execute("UPDATE posts SET score = score - 1 WHERE id = ?", (post_id,))
        conn.commit()
        
        conn.close()
        
        return self.RetrievePost(request, context)
    
    def UpvotePost(self, request, context):
            post_id = request.id
            
            conn = reddit_server_db.get_db()
            cur = conn.cursor()
            cur.execute("UPDATE posts SET score = score + 1 WHERE id = ?", (post_id,))
            conn.commit()
            
            conn.close()
            
            return self.RetrievePost(request, context)
    
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
        # Generate a unique comment ID
        comment_id = str(uuid.uuid4())[:4] # take first four characters only - for demo purpose.

        # Extract other post data from the request
        newComment = reddit_pb2.Comment(
            id          = reddit_pb2.CommentID(id=comment_id),
            text        = request.text,
            author      = request.author,
            score       = 0,
            state       = reddit_pb2.CommentState.NORMAL_COMMENT,
            pub_date    = str(datetime.datetime.now()),
            parent_post_id = request.parent_post_id,
            parent_comment_id = request.parent_comment_id
        )

        # Insert the new post into the database
        conn = reddit_server_db.get_db()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO comments (id, text, author, score, state, pub_date, parent_post_id, parent_comment_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (comment_id, newComment.text, newComment.author, 0, 0,  
             newComment.pub_date, request.parent_post_id.id, request.parent_comment_id.id)
        )
        conn.commit()
        conn.close()

        # Create and return the Post object
        return newComment
    
    def UpvoteComment(self, request, context):
        return super().UpvoteComment(request, context)
    
    def DownvoteComment(self, request, context):
        return super().DownvoteComment(request, context)
    
    def ExpandComment(self, request, context):
        comment_id = request.comment.id
        num = request.number
        
        # First-level comments (children of this comment)
        conn = reddit_server_db.get_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM comments
            WHERE parent_comment_id = ?
            ORDER BY score DESC
            LIMIT ?
        """, (comment_id, num))
        top_comments = cur.fetchall()
        expanded_comments = []
        

        # Second-level comments for each of the top comments
        for top_comment in top_comments:
            top_comment_id = dict(top_comment)['id']  # Assuming the ID field is 'id'
            cur.execute("""
                SELECT * FROM comments
                WHERE parent_comment_id = ?
                ORDER BY score DESC
                LIMIT ?
            """, (top_comment_id, num))

            second_level_comments = cur.fetchall()
            expanded_comments += second_level_comments

        expanded_comments += top_comments
        conn.close()
        
        stateMap = {
            0 : reddit_pb2.CommentState.NORMAL_COMMENT,
            1 : reddit_pb2.CommentState.HIDDEN_COMMENT
        }
        
        print(str(expanded_comments))
        for comment in expanded_comments:
            commentDict = dict(comment)
            retObj = reddit_pb2.Comment(
                id = reddit_pb2.CommentID(id = commentDict["id"]),
                author=commentDict["author"],
                score=commentDict["score"],
                state=stateMap[commentDict["state"]],
                text=commentDict["text"],
                parent_comment_id=reddit_pb2.CommentID(id = commentDict["parent_comment_id"]),
                parent_post_id=reddit_pb2.PostID(id=commentDict["parent_post_id"]),
                hasReplies=commentDict["has_replies"]
            )
            yield retObj
            
                
    def RetrieveComments(self, request: reddit_pb2.RetrieveCommentRequest, context):
        post_id = request.post.id
        num_retrieve = request.number
        
        conn = reddit_server_db.get_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT comments.*
            FROM comments
            JOIN posts ON comments.parent_post_id = posts.id
            WHERE posts.id = ?
            ORDER BY comments.score DESC
            LIMIT ?
        """, (post_id, num_retrieve))
        top_comments = cur.fetchall()
        conn.close()
        
        stateMap = {
            0 : reddit_pb2.CommentState.NORMAL_COMMENT,
            1 : reddit_pb2.CommentState.HIDDEN_COMMENT
        }
        
        for comment in top_comments:
            commentDict = dict(comment)
            retObj = reddit_pb2.Comment(
                id = reddit_pb2.CommentID(id = commentDict["id"]),
                author=commentDict["author"],
                score=commentDict["score"],
                state=stateMap[commentDict["state"]],
                text=commentDict["text"],
                parent_comment_id=reddit_pb2.CommentID(id = commentDict["parent_comment_id"]),
                parent_post_id=reddit_pb2.PostID(id=commentDict["parent_post_id"]),
                hasReplies=commentDict["has_replies"]
            )
            yield retObj

def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reddit_pb2_grpc.add_RedditServicer_to_server(RedditService(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"Server started on port {port}")
    server.wait_for_termination()
    
if __name__ == '__main__':
    reddit_server_db.setup_db()
    parser = argparse.ArgumentParser(description='gRPC Server')
    parser.add_argument('--port', type=int, default=50051, help='The server port')
    args = parser.parse_args()

    serve(args.port)