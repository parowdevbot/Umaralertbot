import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL", "")
    PORT = int(os.getenv("PORT", 5000))
