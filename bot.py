import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from deep_translator import GoogleTranslator

TOKEN = "8510295431:AAEw1M3DoJlj2-CJ6ZQ5IK7uNfkYddEnF84"

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    translated = GoogleTranslator(source='auto', target='zh-CN').translate(text)
    await update.message.reply_text(translated)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))

app.run_polling()
