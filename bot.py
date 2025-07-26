import os
import logging
from datetime import datetime
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
        # Initialize application with job queue support
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
        
        # Setup job queue
        if self.application.job_queue:
            self.application.job_queue.run_repeating(
                self.monitor_tasks,
                interval=300.0,
                first=10.0
            )
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send welcome message with debug info"""
        debug_info = f"""
        Bot Status Report:
        • Webhook: {Config.WEBHOOK_URL}
        • Token: {Config.BOT_TOKEN[:5]}...{Config.BOT_TOKEN[-5:]}
        • Jobs Running: {len(self.application.job_queue.jobs()) if self.application.job_queue else 0}
        • Server Time: {datetime.now()}
        """
        await update.message.reply_text(f"🚀 Bot is operational!\n{debug_info}")
    
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send help message"""
        await update.message.reply_text("ℹ️ Available commands:\n/start - Check bot status\n/help - Show this message")
    
    async def monitor_tasks(self, context: ContextTypes.DEFAULT_TYPE):
        """Background task that runs periodically"""
        logger.info("✅ Performing scheduled monitoring...")
        try:
            # Your monitoring logic here
            pass
        except Exception as e:
            logger.error(f"Monitoring error: {e}")
    
    def start_bot(self):
        """Start the bot with proper webhook configuration"""
        webhook_url = f"{Config.WEBHOOK_URL}/{Config.BOT_TOKEN}"
        logger.info(f"🔗 Setting webhook to: {webhook_url}")
        
        try:
            self.application.run_webhook(
                listen="0.0.0.0",
                port=Config.PORT,
                url_path=Config.BOT_TOKEN,
                webhook_url=webhook_url,
                drop_pending_updates=True
            )
        except Exception as e:
            logger.error(f"Webhook failed: {e}\n🔄 Falling back to polling...")
            self.application.run_polling()

if __name__ == "__main__":
    bot = CryptoAlertBot()
    bot.start_bot()
