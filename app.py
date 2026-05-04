import os
import asyncio
from flask import Flask, request, jsonify

from trading.master_engine import execute_trade
from bot.bot import run_bot_app  # IMPORTANT CHANGE

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


async def start_bot():
    bot_app = run_bot_app()
    await bot_app.initialize()
    await bot_app.start()
    await bot_app.updater.start_polling()
    await bot_app.updater.idle()


if __name__ == "__main__":

    # run bot safely in event loop
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
