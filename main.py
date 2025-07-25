import os
from telegram.ext import Application
from config import Config

async def post_init(app):
    await app.bot.set_webhook(f"{Config.WEBHOOK_URL}/{Config.BOT_TOKEN}")

def create_app():
    app = Application.builder() \
        .token(Config.BOT_TOKEN) \
        .post_init(post_init) \
        .build()
    
    # Register handlers here
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
        webhook_url=Config.WEBHOOK_URL
    )
