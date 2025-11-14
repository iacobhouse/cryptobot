import telebot
import time
import random
import os
from flask import Flask, request

app = Flask(__name__)

TOKEN = "8548138805:AAE8JNgxiwz3ZifOpSIH0UfiszuPz6X1hG8"
CHANNEL = "@CryptoKing_Signalss"   # ← il tuo canale

bot = telebot.TeleBot(TOKEN)

# Test immediato
@ app.route('/')
def home():
    try:
        bot.send_message(CHANNEL, " BOT ONLINE SU RENDER – TEST " + time.strftime("%H:%M"))
        return "Post inviato nel canale!"
    except Exception as e:
        return str(e)

# Segnali ogni 4 ore
def auto_signals():
    while True:
        time.sleep(14400)
        coins = ["$BONK", "$PEPE", "$WIF", "$BRETT", "$MOG", "$FLOKI"]
        coin = random.choice(coins)
        entry = round(random.uniform(0.00001, 0.00042), 8)
        text = f"""PUMP SIGNAL

{coin}
ENTRY @{entry}
TP1 @{entry*1.5} (+50%)
TP2 @{entry*2.5} (+150%)

100x INCOMING!"""
        bot.send_message(CHANNEL, text)

# Avvia auto-segnale
import threading
threading.Thread(target=auto_signals, daemon=True).start()

# Webhook (Render richiede una route attiva)
@app.route('/webhook', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'OK', 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://cryptoking-bot.onrender.com/webhook")
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
