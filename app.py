import os
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


# ---------------- START BOT ----------------
def start_bot():
    application = run_bot_app()

    # SAFE blocking call (DO NOT use asyncio here)
    application.run_polling(drop_pending_updates=True)


# ---------------- MAIN ----------------
if __name__ == "__main__":
    import threading

    # Run bot in background thread
    bot_thread = threading.Thread(target=start_bot)
    bot_thread.daemon = True
    bot_thread.start()

    # Run Flask normally
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
