from redditClient import reddit_client



def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    client = reddit_client.RedditServer()
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
