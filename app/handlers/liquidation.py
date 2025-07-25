from telegram import Update
from telegram.ext import ContextTypes
from utils.rate_limiter import RateLimiter

rate_limiter = RateLimiter()

async def liquidation_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not rate_limiter.check_limit():
        await update.message.reply_text("Rate limit exceeded. Try again later.")
        return
    
    # Your liquidation logic here
    await update.message.reply_text("🔥 Liquidation alert processed")
