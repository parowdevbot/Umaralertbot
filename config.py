import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7822484786:AAET1gInNrtQTrpiuOaRlfJFNmzPyGArcng")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://umaralertbot.onrender.com")  # MUST match your Render URL exactly
    PORT = int(os.getenv("PORT", 5000))
