INSERT INTO users (user_id) VALUES
('user1'),
('user2');

INSERT INTO posts (id, title, text, author, score, state, pub_date, video) VALUES
('post1', 'Title 1', 'Text of post 1', 'user1', 5, 0, '2021-01-01', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'),
('post2', 'Title 2', 'Text of post 2', 'user2', 3, 1, '2021-02-01'. 'https://www.youtube.com/watch?v=dQw4w9WgXcQ');

INSERT INTO comments (id, author, score, state, pub_date, parent_post_id, has_replies) VALUES
('comment1', 'user2', 2, 0, '2021-01-02', 'post1', True),
('comment2', 'user1', 3, 0, '2021-02-02', 'post1', False);
