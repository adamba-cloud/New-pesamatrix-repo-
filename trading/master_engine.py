from database import cursor, conn
from bot.alerts import send_alert
from trading.copy_engine import copy_trade
from trading.risk_manager import check_risk
from datetime import datetime


def execute_trade(symbol, side, entry, sl, tp):

    trade = {
        "symbol": symbol,
        "side": side,
        "entry": entry,
        "sl": sl,
        "tp": tp,
        "timestamp": str(datetime.now())
    }

    if not check_risk(trade):
        return {"status": "rejected", "reason": "risk failed"}

    cursor.execute("""
        INSERT INTO trades (symbol, side, entry, sl, tp, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (symbol, side, entry, sl, tp, trade["timestamp"]))

    conn.commit()

    send_alert(trade)
    copy_trade(trade)

    return {"status": "success", "trade": trade}
