
import requests
from config import BOT_TOKEN, ADMIN_ID

def send_alert(trade):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    message = f"""
🚨 NEW TRADE ALERT

📊 Symbol: {trade['symbol']}
📈 Side: {trade['side']}
💰 Entry: {trade['entry']}
🛑 SL: {trade['sl']}
🎯 TP: {trade['tp']}
"""

    try:
        requests.post(url, json={
            "chat_id": ADMIN_ID,
            "text": message
        })
    except Exception as e:
        print("Telegram alert error:", e)
