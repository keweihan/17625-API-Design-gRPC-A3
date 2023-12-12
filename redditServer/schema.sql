PRAGMA FOREIGN_KEYS = ON;

CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS posts (
    id TEXT PRIMARY KEY,
    title TEXT,
    text TEXT,
    video TEXT,
    img TEXT,
    author TEXT,
    score INTEGER,
    state INTEGER,
    pub_date TEXT
);

CREATE TABLE IF NOT EXISTS comments (
    id TEXT PRIMARY KEY,
    author TEXT,
    text TEXT,
    score INTEGER,
    state INTEGER,
    pub_date TEXT,
    parent_post_id TEXT,
    parent_comment_id TEXT,
    has_replies BOOLEAN,
    FOREIGN KEY(parent_post_id) REFERENCES posts(id),
    FOREIGN KEY(parent_comment_id) REFERENCES comments(id)
);
