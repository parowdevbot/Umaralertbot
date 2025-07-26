import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_TOKEN")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://umaralertbot.onrender.com")
    PORT = int(os.getenv("PORT", 5000))
    
    # Alert Thresholds
    WHALE_THRESHOLD = 5000000
    LIQUIDATION_THRESHOLD = 50000000
    USDT_FLOW_THRESHOLD = 40000000
    NASDAQ_THRESHOLD = 5.0
