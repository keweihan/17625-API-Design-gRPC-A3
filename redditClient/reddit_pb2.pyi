from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PostState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NORMAL_POST: _ClassVar[PostState]
    LOCKED_POST: _ClassVar[PostState]
    HIDDEN_POST: _ClassVar[PostState]

class CommentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NORMAL_COMMENT: _ClassVar[CommentState]
    HIDDEN_COMMENT: _ClassVar[CommentState]

class SubredditState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PUBLIC_SUBREDDIT: _ClassVar[SubredditState]
    PRIVATE_SUBREDDIT: _ClassVar[SubredditState]
    HIDDEN_SUBREDDIT: _ClassVar[SubredditState]
NORMAL_POST: PostState
LOCKED_POST: PostState
HIDDEN_POST: PostState
NORMAL_COMMENT: CommentState
HIDDEN_COMMENT: CommentState
PUBLIC_SUBREDDIT: SubredditState
PRIVATE_SUBREDDIT: SubredditState
HIDDEN_SUBREDDIT: SubredditState

class User(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class PostID(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class Post(_message.Message):
    __slots__ = ("id", "title", "text", "video", "img", "author", "score", "state", "pub_date", "subreddit")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    IMG_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUB_DATE_FIELD_NUMBER: _ClassVar[int]
    SUBREDDIT_FIELD_NUMBER: _ClassVar[int]
    id: PostID
    title: str
    text: str
    video: str
    img: str
    author: str
    score: int
    state: PostState
    pub_date: str
    subreddit: Subreddit
    def __init__(self, id: _Optional[_Union[PostID, _Mapping]] = ..., title: _Optional[str] = ..., text: _Optional[str] = ..., video: _Optional[str] = ..., img: _Optional[str] = ..., author: _Optional[str] = ..., score: _Optional[int] = ..., state: _Optional[_Union[PostState, str]] = ..., pub_date: _Optional[str] = ..., subreddit: _Optional[_Union[Subreddit, _Mapping]] = ...) -> None: ...

class CreatePostRequest(_message.Message):
    __slots__ = ("title", "text", "video", "img", "author", "pub_date", "subreddit")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    IMG_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    PUB_DATE_FIELD_NUMBER: _ClassVar[int]
    SUBREDDIT_FIELD_NUMBER: _ClassVar[int]
    title: str
    text: str
    video: str
    img: str
    author: str
    pub_date: str
    subreddit: Subreddit
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ..., video: _Optional[str] = ..., img: _Optional[str] = ..., author: _Optional[str] = ..., pub_date: _Optional[str] = ..., subreddit: _Optional[_Union[Subreddit, _Mapping]] = ...) -> None: ...

class CommentID(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ("id", "text", "author", "score", "state", "pub_date", "parent_post_id", "parent_comment_id", "hasReplies")
    ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUB_DATE_FIELD_NUMBER: _ClassVar[int]
    PARENT_POST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    HASREPLIES_FIELD_NUMBER: _ClassVar[int]
    id: CommentID
    text: str
    author: str
    score: int
    state: CommentState
    pub_date: str
    parent_post_id: PostID
    parent_comment_id: CommentID
    hasReplies: bool
    def __init__(self, id: _Optional[_Union[CommentID, _Mapping]] = ..., text: _Optional[str] = ..., author: _Optional[str] = ..., score: _Optional[int] = ..., state: _Optional[_Union[CommentState, str]] = ..., pub_date: _Optional[str] = ..., parent_post_id: _Optional[_Union[PostID, _Mapping]] = ..., parent_comment_id: _Optional[_Union[CommentID, _Mapping]] = ..., hasReplies: bool = ...) -> None: ...

class CreateCommentRequest(_message.Message):
    __slots__ = ("author", "pub_date", "state", "parent_post_id", "parent_comment_id")
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    PUB_DATE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PARENT_POST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    author: str
    pub_date: str
    state: CommentState
    parent_post_id: Post
    parent_comment_id: CommentID
    def __init__(self, author: _Optional[str] = ..., pub_date: _Optional[str] = ..., state: _Optional[_Union[CommentState, str]] = ..., parent_post_id: _Optional[_Union[Post, _Mapping]] = ..., parent_comment_id: _Optional[_Union[CommentID, _Mapping]] = ...) -> None: ...

class MostUpvotedCommentRequest(_message.Message):
    __slots__ = ("post", "number")
    POST_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    post: PostID
    number: int
    def __init__(self, post: _Optional[_Union[PostID, _Mapping]] = ..., number: _Optional[int] = ...) -> None: ...

class ExpandCommentBranchRequest(_message.Message):
    __slots__ = ("comment", "number")
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    comment: CommentID
    number: int
    def __init__(self, comment: _Optional[_Union[CommentID, _Mapping]] = ..., number: _Optional[int] = ...) -> None: ...

class RetrieveCommentRequest(_message.Message):
    __slots__ = ("post", "number")
    POST_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    post: PostID
    number: int
    def __init__(self, post: _Optional[_Union[PostID, _Mapping]] = ..., number: _Optional[int] = ...) -> None: ...

class Subreddit(_message.Message):
    __slots__ = ("name", "state", "pub_date", "tags")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUB_DATE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: SubredditState
    pub_date: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[SubredditState, str]] = ..., pub_date: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...
