import telebot
import requests

# التوكن الخاص بك
TOKEN = '8788543988:AAEiDekcxixlVlCjXm5pJ_otluPiBpTr_QY'

bot = telebot.TeleBot(TOKEN)

# رسالة الترحيب عند كتابة /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🛡️ CS2 Market Guard is active!\nSend me the exact skin name to get the price.")

# استقبال اسم السكين وجلب سعره
@bot.message_handler(func=lambda message: True)
def get_price(message):
    item_name = message.text
    # رابط Steam API
    url = f"https://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name={item_name}"
    
    try:
        response = requests.get(url).json()
        if response.get("success"):
            price = response.get("lowest_price", "No price found")
            bot.reply_to(message, f"💰 Current Price: {price}")
        else:
            bot.reply_to(message, "❌ Item not found. Make sure the name is exact!")
    except:
        bot.reply_to(message, "⚠️ Steam is busy. Try again later.")

# تشغيل البوت
bot.polling()
