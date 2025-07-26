import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import Config

# Verify webhook URL before starting
if not Config.WEBHOOK_URL.startswith(('http://', 'https://')):
    raise ValueError("WEBHOOK_URL must start with http:// or https://")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is online!")

def main():
    app = Application.builder().token(Config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    logger.info(f"Starting webhook for: {Config.WEBHOOK_URL}")
    
    try:
        app.run_webhook(
            listen="0.0.0.0",
            port=Config.PORT,
            url_path=Config.BOT_TOKEN,
            webhook_url=f"{Config.WEBHOOK_URL}/{Config.BOT_TOKEN}",
            drop_pending_updates=True
        )
    except Exception as e:
        logger.error(f"Webhook failed: {e}")
        logger.info("Falling back to polling...")
        app.run_polling()

if __name__ == "__main__":
    main()
