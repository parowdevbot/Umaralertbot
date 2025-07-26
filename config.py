import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "8222743591:AAGbNsISPbPacxhLVQmuAUWuLgTMfPFf9o4")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://umaralertbot.onrender.com")  # MUST match your Render URL exactly
    PORT = int(os.getenv("PORT", 5000))
