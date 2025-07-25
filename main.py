import os
import logging
import time
import psutil
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    filters
)
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
        self.updater = Updater(token=Config.BOT_TOKEN, use_context=True)
        self.dispatcher = self.updater.dispatcher
        
        # Command handlers
        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(CommandHandler("status", self.status))
        
        # Background tasks
        self.job_queue = self.updater.job_queue
        self.job_queue.run_repeating(self.monitor_ram, interval=300)

    def start(self, update: Update, context: CallbackContext):
        update.message.reply_text("🚀 Bot activated! Use /status to check system health.")

    def status(self, update: Update, context: CallbackContext):
        ram = psutil.virtual_memory().percent
        update.message.reply_text(f"🤖 System Status:\n• RAM: {ram}%\n• Active since: {time.ctime(storage.start_time)}")

    def monitor_ram(self, context: CallbackContext):
        if psutil.virtual_memory().percent > Config.RAM_LIMIT:
            logger.warning("High RAM usage detected!")

    def run(self):
        self.updater.start_webhook(
            listen="0.0.0.0",
            port=int(os.getenv("PORT", 5000)),
            url_path=Config.BOT_TOKEN,
            webhook_url=f"{Config.WEBHOOK_URL}/{Config.BOT_TOKEN}"
        )
        self.updater.idle()

if __name__ == "__main__":
    bot = CryptoAlertBot()
    bot.run()
