# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reddit.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0creddit.proto\x12\x06reddit\"\x17\n\x04User\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"\x14\n\x06PostID\x12\n\n\x02id\x18\x01 \x01(\t\"\xef\x01\n\x04Post\x12\x1a\n\x02id\x18\n \x01(\x0b\x32\x0e.reddit.PostID\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x0f\n\x05video\x18\x03 \x01(\tH\x00\x12\r\n\x03img\x18\x04 \x01(\tH\x00\x12\x13\n\x06\x61uthor\x18\x05 \x01(\tH\x01\x88\x01\x01\x12\r\n\x05score\x18\x06 \x01(\x05\x12 \n\x05state\x18\x07 \x01(\x0e\x32\x11.reddit.PostState\x12\x10\n\x08pub_date\x18\x08 \x01(\t\x12$\n\tsubreddit\x18\t \x01(\x0b\x32\x11.reddit.SubredditB\x05\n\x03urlB\t\n\x07_author\"\xaf\x01\n\x11\x43reatePostRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x0f\n\x05video\x18\x03 \x01(\tH\x00\x12\r\n\x03img\x18\x04 \x01(\tH\x00\x12\x13\n\x06\x61uthor\x18\x05 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x08pub_date\x18\x08 \x01(\t\x12$\n\tsubreddit\x18\t \x01(\x0b\x32\x11.reddit.SubredditB\x05\n\x03urlB\t\n\x07_author\"\x17\n\tCommentID\x12\n\n\x02id\x18\x01 \x01(\t\"\xf4\x01\n\x07\x43omment\x12\x1d\n\x02id\x18\t \x01(\x0b\x32\x11.reddit.CommentID\x12\x0e\n\x06\x61uthor\x18\n \x01(\t\x12\r\n\x05score\x18\x01 \x01(\x05\x12#\n\x05state\x18\x02 \x01(\x0e\x32\x14.reddit.CommentState\x12\x10\n\x08pub_date\x18\x03 \x01(\t\x12&\n\x0eparent_post_id\x18\x04 \x01(\x0b\x32\x0c.reddit.PostH\x00\x12.\n\x11parent_comment_id\x18\x05 \x01(\x0b\x32\x11.reddit.CommentIDH\x00\x12\x12\n\nhasReplies\x18\x06 \x01(\x08\x42\x08\n\x06parent\"\xbf\x01\n\x14\x43reateCommentRequest\x12\x0e\n\x06\x61uthor\x18\x05 \x01(\t\x12\x10\n\x08pub_date\x18\x01 \x01(\t\x12#\n\x05state\x18\x02 \x01(\x0e\x32\x14.reddit.CommentState\x12&\n\x0eparent_post_id\x18\x03 \x01(\x0b\x32\x0c.reddit.PostH\x00\x12.\n\x11parent_comment_id\x18\x04 \x01(\x0b\x32\x11.reddit.CommentIDH\x00\x42\x08\n\x06parent\"I\n\x19MostUpvotedCommentRequest\x12\x1c\n\x04post\x18\x01 \x01(\x0b\x32\x0e.reddit.PostID\x12\x0e\n\x06number\x18\x02 \x01(\x05\"P\n\x1a\x45xpandCommentBranchRequest\x12\"\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x11.reddit.CommentID\x12\x0e\n\x06number\x18\x02 \x01(\x05\"`\n\tSubreddit\x12\x0c\n\x04name\x18\x04 \x01(\t\x12%\n\x05state\x18\x01 \x01(\x0e\x32\x16.reddit.SubredditState\x12\x10\n\x08pub_date\x18\x02 \x01(\t\x12\x0c\n\x04tags\x18\x03 \x03(\t*>\n\tPostState\x12\x0f\n\x0bNORMAL_POST\x10\x00\x12\x0f\n\x0bLOCKED_POST\x10\x01\x12\x0f\n\x0bHIDDEN_POST\x10\x02*6\n\x0c\x43ommentState\x12\x12\n\x0eNORMAL_COMMENT\x10\x00\x12\x12\n\x0eHIDDEN_COMMENT\x10\x01*S\n\x0eSubredditState\x12\x14\n\x10PUBLIC_SUBREDDIT\x10\x00\x12\x15\n\x11PRIVATE_SUBREDDIT\x10\x01\x12\x14\n\x10HIDDEN_SUBREDDIT\x10\x02\x32\xcb\x03\n\x06Reddit\x12\x37\n\nCreatePost\x12\x19.reddit.CreatePostRequest\x1a\x0c.reddit.Post\"\x00\x12.\n\x0c\x44ownvotePost\x12\x0e.reddit.PostID\x1a\x0c.reddit.Post\"\x00\x12,\n\nUpvotePost\x12\x0e.reddit.PostID\x1a\x0c.reddit.Post\"\x00\x12.\n\x0cRetrievePost\x12\x0e.reddit.PostID\x1a\x0c.reddit.Post\"\x00\x12@\n\rCreateComment\x12\x1c.reddit.CreateCommentRequest\x1a\x0f.reddit.Comment\"\x00\x12\x35\n\rUpvoteComment\x12\x11.reddit.CommentID\x1a\x0f.reddit.Comment\"\x00\x12\x37\n\x0f\x44ownvoteComment\x12\x11.reddit.CommentID\x1a\x0f.reddit.Comment\"\x00\x12H\n\rExpandComment\x12\".reddit.ExpandCommentBranchRequest\x1a\x0f.reddit.Comment\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reddit_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_POSTSTATE']._serialized_start=1212
  _globals['_POSTSTATE']._serialized_end=1274
  _globals['_COMMENTSTATE']._serialized_start=1276
  _globals['_COMMENTSTATE']._serialized_end=1330
  _globals['_SUBREDDITSTATE']._serialized_start=1332
  _globals['_SUBREDDITSTATE']._serialized_end=1415
  _globals['_USER']._serialized_start=24
  _globals['_USER']._serialized_end=47
  _globals['_POSTID']._serialized_start=49
  _globals['_POSTID']._serialized_end=69
  _globals['_POST']._serialized_start=72
  _globals['_POST']._serialized_end=311
  _globals['_CREATEPOSTREQUEST']._serialized_start=314
  _globals['_CREATEPOSTREQUEST']._serialized_end=489
  _globals['_COMMENTID']._serialized_start=491
  _globals['_COMMENTID']._serialized_end=514
  _globals['_COMMENT']._serialized_start=517
  _globals['_COMMENT']._serialized_end=761
  _globals['_CREATECOMMENTREQUEST']._serialized_start=764
  _globals['_CREATECOMMENTREQUEST']._serialized_end=955
  _globals['_MOSTUPVOTEDCOMMENTREQUEST']._serialized_start=957
  _globals['_MOSTUPVOTEDCOMMENTREQUEST']._serialized_end=1030
  _globals['_EXPANDCOMMENTBRANCHREQUEST']._serialized_start=1032
  _globals['_EXPANDCOMMENTBRANCHREQUEST']._serialized_end=1112
  _globals['_SUBREDDIT']._serialized_start=1114
  _globals['_SUBREDDIT']._serialized_end=1210
  _globals['_REDDIT']._serialized_start=1418
  _globals['_REDDIT']._serialized_end=1877
# @@protoc_insertion_point(module_scope)