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
        # Initialize application with job queue support
        self.application = Application.builder().token(Config.BOT_TOKEN).build()
        
        # Register command handlers (MUST match @BotFather commands exactly)
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("help", self.help))
        self.application.add_handler(CommandHandler("status", self.status))
        
        # Setup job queue for alerts
        if self.application.job_queue:
            self.application.job_queue.run_repeating(
                self.monitor_tasks,
                interval=300.0,
                first=10.0
            )

    # ===== COMMAND HANDLERS =====
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handler for /start command"""
        await update.message.reply_text(
            "🚀 Crypto Alert Bot Activated!\n"
            "Type /help for available commands"
        )

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handler for /help command"""
        await update.message.reply_text(
            "📝 Available Commands:\n"
            "/start - Start the bot\n"
            "/help - Show this message\n"
            "/status - Check bot status\n"
            "\nAlerts will be sent automatically"
        )

    async def status(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handler for /status command"""
        await update.message.reply_text(
            "✅ Bot is fully operational!\n"
            f"🔗 Webhook: {Config.WEBHOOK_URL}\n"
            f"⏱ Last check: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

    # ===== BACKGROUND TASKS =====
    async def monitor_tasks(self, context: ContextTypes.DEFAULT_TYPE):
        """Scheduled task that runs every 5 minutes"""
        try:
            # Your alert logic here
            logger.info("Running scheduled checks...")
            
            # Example alert (replace with your logic)
            if some_alert_condition:
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="🚨 New alert detected!"
                )
        except Exception as e:
            logger.error(f"Alert error: {e}")

    # ===== START METHOD =====
    def start_bot(self):
        """Start the bot in webhook mode"""
        try:
            self.application.run_webhook(
                listen="0.0.0.0",
                port=Config.PORT,
                url_path=Config.BOT_TOKEN,
                webhook_url=f"{Config.WEBHOOK_URL}/{Config.BOT_TOKEN}",
                drop_pending_updates=True
            )
        except Exception as e:
            logger.error(f"Webhook failed: {e}, switching to polling")
            self.application.run_polling()

if __name__ == "__main__":
    bot = CryptoAlertBot()
    bot.start_bot()
