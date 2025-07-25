class Config:
    # Telegram
    BOT_TOKEN = "8222743591:AAF6UrtttBrAJT_w6_NhS8Sp9m_Db9LBJj8"
    WEBHOOK_URL = "https://umaralertbot.onrender.com"
    
    # System
    RAM_LIMIT = 80  # Percentage
    MIN_SCRAPE_INTERVAL = 10  # Seconds
    MAX_RETRIES = 3
    RETRY_DELAY = 3600  # 1 hour in seconds
    
    # Timing
    SLEEP_START = 23  # 11 PM
    SLEEP_END = 7     # 7 AM
