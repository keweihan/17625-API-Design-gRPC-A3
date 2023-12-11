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
        
def setup_database():
    # Delete existing database. Create new one in same folder as this script.
    reset_db()
    conn = sqlite3.connect(get_absolute_path('reddit.db'))
    cur = conn.cursor()

    # Execute schema and data SQL files
    execute_sql_file(cur, get_absolute_path('schema.sql'))
    execute_sql_file(cur, get_absolute_path('data.sql'))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()