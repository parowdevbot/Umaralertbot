import os
from telegram.ext import Application, CommandHandler
from config import Config
from app.handlers.whale import whale_handler
from app.handlers.liquidation import liquidation_handler
from app.handlers.usdtflow import usdtflow_handler

async def post_init(app):
    await app.bot.set_webhook(f"{Config.WEBHOOK_URL}/{Config.BOT_TOKEN}")

def main():
    app = Application.builder() \
        .token(Config.BOT_TOKEN) \
        .post_init(post_init) \
        .build()
    
    app.add_handler(CommandHandler("whale", whale_handler))
    app.add_handler(CommandHandler("liquidation", liquidation_handler))
    app.add_handler(CommandHandler("usdtflow", usdtflow_handler))
    
    app.run_webhook(
        listen="0.0.0.0",
        port=Config.PORT,
        webhook_url=Config.WEBHOOK_URL,
        drop_pending_updates=True
    )

if __name__ == "__main__":
    main()
