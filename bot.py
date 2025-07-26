import asyncio
from datetime import datetime, time
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

class CryptoAlertBot:
    def __init__(self):
        self._init_commands()
        self._init_monitoring()
    
    def _init_commands(self):
        """Register only implemented commands"""
        self.command_handlers = {
            'summary': self.summary,
            'usdtflow': self.usdtflow,
            'smartlist': self.smartlist,
            'log': self.show_log,
            'status': self.status,
            'silent': self.set_silent
        }
    
    def _init_monitoring(self):
        """Initialize monitoring modules"""
        self.whale_detector = WhaleDetector()
        self.liquidation_scraper = LiquidationScraper()
        self.usdt_tracker = USDTFlowTracker()
        self.nasdaq_monitor = NasdaqMonitor()
        
        # Schedule tasks
        self.scheduler.add_job(
            self._run_checks,
            'interval',
            minutes=30,
            next_run_time=datetime.now()
        )
    
    async def _run_checks(self):
        """Orchestrate all monitoring"""
        if self._should_skip():
            return
            
        results = await asyncio.gather(
            self.whale_detector.check_whales(),
            self.liquidation_scraper.get_clusters(),
            self.usdt_tracker.get_net_flow(),
            self.nasdaq_monitor.check_movers(),
            return_exceptions=True
        )
        self._process_results(results)
    
    # Command implementations
    async def summary(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show top 3 alerts"""
        alerts = self.alert_queue.get_top(3)
        await update.message.reply_text(
            "🔝 Top 3 Alerts:\n" + 
            "\n".join(f"{i+1}. {alert}" for i, alert in enumerate(alerts))
        )
    
    async def smartlist(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show smart wallets"""
        wallets = self.whale_detector.get_smart_wallets()
        await update.message.reply_text(
            "🏆 Smart Whales:\n" +
            "\n".join(f"{w['address']} ({w['success_rate']}%)" for w in wallets)
        )
