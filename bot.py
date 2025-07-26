import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import Config

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Bot is working! Try /test")

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Test successful! Bot is functional")

def main():
    app = Application.builder().token(Config.BOT_TOKEN).build()
    
    # Register commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test", test))
    
    # Start webhook
    app.run_webhook(
        listen="0.0.0.0",
        port=Config.PORT,
        url_path=Config.BOT_TOKEN,
        webhook_url=f"{Config.WEBHOOK_URL}/{Config.BOT_TOKEN}",
        drop_pending_updates=True
    )

if __name__ == "__main__":
    main()
