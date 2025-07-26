import os
from telegram.ext import Application
from config import Config

def create_app():
    app = Application.builder().token(Config.BOT_TOKEN).build()
    
    # Register handlers
    from app.handlers import whale, liquidation, usdtflow
    app.add_handlers([
        CommandHandler("whale", whale.handler),
        CommandHandler("liquidation", liquidation.handler),
        CommandHandler("usdtflow", usdtflow.handler)
    ])
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        webhook_url=Config.WEBHOOK_URL,
        drop_pending_updates=True
    )
