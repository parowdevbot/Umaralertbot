import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
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
        # Initialize application with job queue
        self.application = (
            Application.builder()
            .token(Config.BOT_TOKEN)
            .concurrent_updates(True)
            .build()
        )
        
        self.silent_mode = False
        
        # Command handlers
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("help", self.help))
        
        # Job queue setup
        if self.application.job_queue is None:
            logger.error("Job queue is not available!")
        else:
            self.application.job_queue.run_repeating(
                self.monitor_tasks,
                interval=300.0,
                first=10.0
            )
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Bot is running!')
    
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Help information here')
    
    async def monitor_tasks(self, context: ContextTypes.DEFAULT_TYPE):
        try:
            # Your monitoring logic here
            logger.info("Running scheduled task...")
        except Exception as e:
            logger.error(f"Task error: {e}")
    
    def start_bot(self):
        port = int(os.getenv("PORT", 5000))
        self.application.run_webhook(
            listen="0.0.0.0",
            port=port,
            url_path=Config.BOT_TOKEN,
            webhook_url=f"{Config.WEBHOOK_URL}/{Config.BOT_TOKEN}",
            drop_pending_updates=True
        )

if __name__ == "__main__":
    bot = CryptoAlertBot()
    bot.start_bot()
