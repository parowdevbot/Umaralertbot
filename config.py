import os

class Config:
    # Required configurations
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7822484786:AAET1gInNrtQTrpiuOaRlfJFNmzPyGArcng")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://umaralertbot.onrender.com")
    PORT = int(os.getenv("PORT", 5000))
    
    # Logging configuration
    LOG_FILE = os.getenv("LOG_FILE", "logs/bot.log")  # Add this line
    
    # Alert thresholds
    WHALE_THRESHOLD = int(os.getenv("WHALE_THRESHOLD", 5000000))
    LIQUIDATION_THRESHOLD = int(os.getenv("LIQUIDATION_THRESHOLD", 50000000))
    USDT_FLOW_THRESHOLD = int(os.getenv("USDT_FLOW_THRESHOLD", 40000000))
    NASDAQ_THRESHOLD = float(os.getenv("NASDAQ_THRESHOLD", 5.0))
