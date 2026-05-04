from database import cursor, conn

def create_trade_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT,
        side TEXT,
        entry REAL,
        sl REAL,
        tp REAL,
        timestamp TEXT
    )
    """)
    conn.commit()


def save_trade(trade):
    cursor.execute("""
        INSERT INTO trades (symbol, side, entry, sl, tp, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        trade["symbol"],
        trade["side"],
        trade["entry"],
        trade["sl"],
        trade["tp"],
        trade["timestamp"]
    ))
    conn.commit()


def get_trades():
    cursor.execute("SELECT * FROM trades")
    return cursor.fetchall()
