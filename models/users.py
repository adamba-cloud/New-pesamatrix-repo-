from database import cursor, conn

def create_user_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()


def add_user(telegram_id):
    cursor.execute("""
    INSERT OR IGNORE INTO users (telegram_id)
    VALUES (?)
    """, (telegram_id,))
    conn.commit()


def get_all_users():
    cursor.execute("SELECT telegram_id FROM users")
    return cursor.fetchall()
