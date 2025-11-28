from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8426449907:AAGJOf65O3a5jwbq6E1PidWaW0WYZorLybo"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("💰 Số dư của tôi")],
        [KeyboardButton("🛒 Rút code"), KeyboardButton("📮 MỜI BẠN BÈ")],
        [KeyboardButton("📄 Link Game"), KeyboardButton("📊 CSKH Hỗ Trợ")]
    ]

    reply = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Chọn chức năng:", reply_markup=reply)


async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "💰 Số dư của tôi":
        await update.message.reply_text("Số dư: 0đ")
    elif text == "🛒 Rút code":
        await update.message.reply_text("Nhập mã code muốn rút:")
    elif text == "📮 MỜI BẠN BÈ":
        await update.message.reply_text("Link mời: https://t.me/YourBot?start=ref123")
    elif text == "📄 Link Game":
        await update.message.reply_text("Link game: https:cpbank.club")
    elif text == "📊 CSKH Hỗ trợ":
        await update.message.reply_text("CSKH: @hotrocpbank")
    else:
        await update.message.reply_text("Không hiểu lệnh.")


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_buttons))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
