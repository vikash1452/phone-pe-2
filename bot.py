import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Configuration
TELEGRAM_LINK = os.getenv('TELEGRAM_LINK', "https://t.me/+BvjTA1I2Jt81YzM1")
INSTAGRAM_LINK = os.getenv('INSTAGRAM_LINK', "https://www.instagram.com/bhavesh_z_10x/")
BLACK_DRIVE_LINK = os.getenv('BLACK_LINK', "https://drive.google.com/file/d/11tD_AaZrxshxEq-ek-8qB8_28zzXI6Jh/view?usp=drivesdk")
WHITE_DRIVE_LINK = os.getenv('WHITE_LINK', "https://drive.google.com/file/d/11xD3LnpxZ_0Bhv5qZ8pxD8JF6KWD2P5r/view?usp=drivesdk")
BOT_TOKEN = os.getenv('BOT_TOKEN', "YOUR_BOT_TOKEN")
PORT = int(os.getenv('PORT', 8443))
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("📱 PHONE PE DARK MODE", callback_data='black')],
        [InlineKeyboardButton("📱 PHONE PE LIGHT MODE", callback_data='white')]
    ]
    update.message.reply_text(
        "🌟 BHAVESH BOT ME APKA SWAGAT HE 🌟\n\nKripya apna mode chune:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ... (पूरा कोड जैसा मैंने पहले भेजा था)

if __name__ == '__main__':
    main()
