import os

class Config:
    # Required settings with fallback values
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7822484786:AAET1gInNrtQTrpiuOaRlfJFNmzPyGArcng")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://umaralertbot.onrender.com")
    
    # Optional settings with defaults
    PORT = int(os.getenv("PORT", 5000))
    RATE_LIMIT_SECONDS = int(os.getenv("RATE_LIMIT_SECONDS", 5))
    LOG_FILE = os.getenv("LOG_FILE", "data/logs/bot.log")
    WHALE_THRESHOLD = int(os.getenv("WHALE_THRESHOLD", 5000000))
    LIQUIDATION_THRESHOLD = int(os.getenv("LIQUIDATION_THRESHOLD", 50000000))
    USDT_FLOW_THRESHOLD = int(os.getenv("USDT_FLOW_THRESHOLD", 40000000))
