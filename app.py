import os
import threading
from flask import Flask, request, jsonify

from trading.master_engine import execute_trade
from bot.bot import run_bot

app = Flask(__name__)


# start telegram bot
def start_bot():
    run_bot()


threading.Thread(target=start_bot, daemon=True).start()


@app.route("/")
def home():
    return "Copy Trading System Active 🚀"


@app.route("/trade", methods=["POST"])
def trade():
    data = request.json

    return jsonify(execute_trade(
        data["symbol"],
        data["side"],
        data["entry"],
        data["sl"],
        data["tp"]
    ))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
