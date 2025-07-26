import asyncio
import logging
import psutil
from datetime import datetime, time
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config import Config
from utils.whale_detector import WhaleDetector
from utils.liquidation_scraper import LiquidationScraper
from utils.usdt_flow import USDTFlowTracker
from utils.nasdaq_monitor import NasdaqMonitor
from utils.storage import AlertStorage

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Config.LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class CryptoAlertBot:
    def __init__(self):
        self.storage = AlertStorage()
        self.detectors = {
            'whale': WhaleDetector(),
            'liquidation': LiquidationScraper(),
            'usdt_flow': USDTFlowTracker(),
            'nasdaq': NasdaqMonitor()
        }
        
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        await update.message.reply_text(
            "🚀 Crypto Alert Bot Active!\n"
            "Monitoring:\n"
            "- Whale transfers (>$5M)\n"
            "- Liquidations (>$50M)\n"
            "- USDT flows (>$40M)\n"
            "- NASDAQ moves (>5%)\n\n"
            "Commands: /summary /usdtflow /smartlist"
        )

    async def summary(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show top 3 alerts"""
        alerts = self.storage.get_recent_alerts(3)
        response = "🔝 Top 3 Alerts:\n" + "\n".join(
            f"{i+1}. {a['type']} - {a['message']}" 
            for i, a in enumerate(alerts)
        )
        await update.message.reply_text(response)

    async def monitor_markets(self):
        """Main monitoring loop"""
        while True:
            try:
                if self._should_skip():
                    continue
                    
                alerts = await self._check_all_sources()
                await self._process_alerts(alerts)
                await asyncio.sleep(300)  # 5 minutes
                
            except Exception as e:
                logger.error(f"Monitoring error: {e}")
                await asyncio.sleep(600)  # Wait longer on errors

async def main():
    """Entry point"""
    bot = CryptoAlertBot()
    application = Application.builder().token(Config.BOT_TOKEN).build()
    
    # Register commands
    application.add_handler(CommandHandler("start", bot.start))
    application.add_handler(CommandHandler("summary", bot.summary))
    
    # Start tasks
    asyncio.create_task(bot.monitor_markets())
    
    # Start bot
    await application.run_webhook(
        listen="0.0.0.0",
        port=Config.PORT,
        url_path=Config.BOT_TOKEN,
        webhook_url=f"{Config.WEBHOOK_URL}/{Config.BOT_TOKEN}",
        drop_pending_updates=True
    )

if __name__ == "__main__":
    asyncio.run(main())
