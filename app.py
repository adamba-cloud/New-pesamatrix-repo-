import os
from flask import Flask, request, jsonify

from trading.master_engine import execute_trade
from bot.bot import run_bot

app = Flask(__name__)


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
    # START TELEGRAM BOT FIRST (NO THREAD)
    run_bot()

    # THEN START FLASK
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
