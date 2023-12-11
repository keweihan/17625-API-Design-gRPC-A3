import sqlite3
import os

def execute_sql_file(cursor, file_path):
    with open(file_path, 'r') as sql_file:
        sql_script = sql_file.read()
    cursor.executescript(sql_script)

def get_absolute_path(relative_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, relative_path)

def reset_db():
    db_path = get_absolute_path('reddit.db')
    if os.path.exists(db_path):
        os.remove(db_path)
        
def setup_db():
    # Delete existing database. Create new one in same folder as this script.
    reset_db()
    conn = sqlite3.connect(get_absolute_path('reddit.db'))
    cur = conn.cursor()

    # Execute schema and data SQL files
    execute_sql_file(cur, get_absolute_path('schema.sql'))
    execute_sql_file(cur, get_absolute_path('data.sql'))

    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect(get_absolute_path('reddit.db'))
    conn.row_factory = sqlite3.Row
    return conn

def get_post_by_id(post_id):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
    post_data = cur.fetchone()

    conn.close()

    if post_data:
        # Convert the row to a dictionary (if row_factory is sqlite3.Row)
        return dict(post_data)
    else:
        return None  # Or handle the case where the post is not found


if __name__ == "__main__":
    print(get_post_by_id('post1'))
    