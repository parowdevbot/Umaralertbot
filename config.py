import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL")
    PORT = int(os.getenv("PORT", 5000))
    RATE_LIMIT_SECONDS = 5
    LOG_FILE = "data/logs/bot.log"
    WHALE_THRESHOLD = 5000000
    LIQUIDATION_THRESHOLD = 50000000
    USDT_FLOW_THRESHOLD = 40000000
