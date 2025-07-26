import os

class Config:
    # Telegram
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL", "")
    PORT = int(os.getenv("PORT", 5000))
    
    # Alert Thresholds
    WHALE_THRESHOLD = 5_000_000  # $5M
    LIQUIDATION_THRESHOLD = 50_000_000  # $50M
    USDT_FLOW_THRESHOLD = 40_000_000  # $40M
    NASDAQ_THRESHOLD = 5.0  # 5%
    
    # System
    LOG_FILE = "logs/bot.log"
    MAX_RAM_USAGE = 512  # MB
