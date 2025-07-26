import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import Config
from utils.logger import setup_logger
from utils.rate_limiter import RateLimiter
from utils.storage import Storage

# Initialize core components
setup_logger()
logger = logging.getLogger(__name__)
storage = Storage()
rate_limiter = RateLimiter()

class CryptoAlertBot:
    def __init__(self):
        self.application = Application.builder().token(Config.BOT_TOKEN).build()
        # ... [rest of your initialization code] ...
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handler for /start command"""
        await update.message.reply_text('Bot started!')
    
    # ... [your other methods] ...
    
    def start_bot(self):
        """Start the bot in webhook or polling mode"""
        try:
            port = int(os.getenv("PORT", 5000))
            self.application.run_webhook(
                listen="0.0.0.0",
                port=port,
                url_path=Config.BOT_TOKEN,
                webhook_url=f"{Config.WEBHOOK_URL}/{Config.BOT_TOKEN}",
                drop_pending_updates=True
            )
        except Exception as e:
            logger.error(f"Webhook failed: {e}, falling back to polling")
            self.application.run_polling()

if __name__ == "__main__":
    bot = CryptoAlertBot()
    bot.start_bot()
