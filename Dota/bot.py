from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8483297084:AAFf98yAeJPgcHjkMPG_6bqgn1QWNIXp_s0"

# هندلر start به صورت async
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! DotaArenaBot آماده است 😎")

def main():
    # ساخت اپلیکیشن
    app = ApplicationBuilder().token(TOKEN).build()

    # اضافه کردن هندلر
    app.add_handler(CommandHandler("start", start))

    # اجرای بوت
    app.run_polling()

if __name__ == "__main__":
    main()
