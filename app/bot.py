import os
from telegram.ext import Application
from config import Config

# Initialize application directly (no create_app function)
application = Application.builder().token(Config.BOT_TOKEN).build()

# Register handlers
from app.handlers import whale, liquidation
application.add_handler(CommandHandler("whale", whale.handler))
application.add_handler(CommandHandler("liquidation", liquidation.handler))

if __name__ == "__main__":
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        webhook_url=Config.WEBHOOK_URL
    )
