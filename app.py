import os
import asyncio
from flask import Flask, request, jsonify

from bot.bot import run_bot_app
from trading.master_engine import execute_trade

app = Flask(__name__)

# ---------------- FLASK ----------------
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


# ---------------- TELEGRAM BOT ----------------
async def start_bot():
    application = run_bot_app()

    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    await application.updater.idle()


# ---------------- MAIN ----------------
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
