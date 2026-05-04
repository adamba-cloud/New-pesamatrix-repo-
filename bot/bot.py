from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from database import cursor, conn
from config import BOT_TOKEN


# ---------------- COMMANDS ----------------
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


# ---------------- BOT FACTORY ----------------
def run_bot_app():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("status", status))

    print("Bot initialized...")

    return application
