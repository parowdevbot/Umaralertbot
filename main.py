import os
import logging
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)
from config import Config
from app.utils.logger import setup_logger
from app.utils.rate_limiter import RateLimiter
from app.handlers.whale import whale_handler
from app.handlers.liquidation import liquidation_handler
from app.handlers.usdtflow import usdtflow_handler

# Initialize logging first
setup_logger()
logger = logging.getLogger(__name__)

class CryptoAlertBot:
    def __init__(self):
        self.rate_limiter = RateLimiter()
        self.app = Application.builder() \
            .token(Config.BOT_TOKEN) \
            .post_init(self._init_webhook) \
            .build()

        # Register handlers
        self._register_handlers()

    def _register_handlers(self):
        """All command handlers from your modules"""
        self.app.add_handler(CommandHandler("start", self._start))
        self.app.add_handler(CommandHandler("whale", whale_handler))
        self.app.add_handler(CommandHandler("liquidation", liquidation_handler))
        self.app.add_handler(CommandHandler("usdtflow", usdtflow_handler))
        self.app.add_handler(CommandHandler("status", self._status))

    async def _init_webhook(self, app):
        """Critical for Render webhook setup"""
        await app.bot.set_webhook(
            f"{Config.WEBHOOK_URL}/{Config.BOT_TOKEN}",
            drop_pending_updates=True
        )
        logger.info("Webhook configured for Render")

    async def _start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """/start command"""
        await update.message.reply_text(
            "🚀 Crypto Alert Bot Active!\n\n"
            "Commands:\n"
            "/whale - Whale alerts\n"
            "/liquidation - Large liquidations\n"
            "/usdtflow - USDT movements\n"
            "/status - Bot health"
        )

    async def _status(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """/status command"""
        import psutil
        ram = psutil.virtual_memory().percent
        await update.message.reply_text(
            f"🤖 Bot Status:\n"
            f"• RAM Usage: {ram}%\n"
            f"• Alerts today: {self.rate_limiter.total_requests}"
        )

    def run(self):
        """Start the webhook server"""
        self.app.run_webhook(
            listen="0.0.0.0",
            port=Config.PORT,
            webhook_url=Config.WEBHOOK_URL,
            secret_token='WEBHOOK_SECRET'  # Optional security
        )

if __name__ == "__main__":
    bot = CryptoAlertBot()
    bot.run()
