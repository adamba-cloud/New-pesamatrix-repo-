import os
import threading
from flask import Flask, request, jsonify

from trading.master_engine import execute_trade
from bot.bot import run_bot

app = Flask(__name__)


# ---------------- HOME ----------------
@app.route("/")
def home():
    return "Copy Trading System Active 🚀"


# ---------------- TRADE ENDPOINT ----------------
@app.route("/trade", methods=["POST"])
def trade():
    data = request.json

    result = execute_trade(
        data["symbol"],
        data["side"],
        data["entry"],
        data["sl"],
        data["tp"]
    )

    return jsonify(result)


# ---------------- RUN BOT IN BACKGROUND ----------------
def start_bot():
    run_bot()


if __name__ == "__main__":

    # Start Telegram bot in separate thread
    bot_thread = threading.Thread(target=start_bot)
    bot_thread.daemon = True
    bot_thread.start()

    # Start Flask server
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
