from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from database import cursor, conn
from config import BOT_TOKEN, ADMIN_ID


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    cursor.execute(
        "INSERT OR IGNORE INTO users (telegram_id) VALUES (?)",
        (user.id,)
    )
    conn.commit()

    await update.message.reply_text("Copy Trading Bot Active 🚀")


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("System Running ✅")


def run_bot():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    print("Bot started...")
    app.run_polling()
