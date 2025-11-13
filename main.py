from flask import Flask, request
import telebot
import os

app = Flask(__name__)

# ⚠️ SOSTITUISCI CON IL TUO TOKEN
TOKEN = "8548138805:AAE8JNgxiwz3ZifOpSIH0UfiszuPz6X1hG8"  # ← IL TUO TOKEN QUI
bot = telebot.TeleBot(TOKEN)

# Comandi
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, """🚀 CRYPTO KING SIGNALS 🚀
    
🔥 Segnali GRATIS ogni 4 ore
🎰 Bonus 500€ senza deposito

Clicca /segnali per il prossimo!""")

@bot.message_handler(commands=['segnali'])
def segnali(message):
    bot.reply_to(message, """⚡ SEGNALE LIVE ⚡
    
🪙 $BONK
📈 ENTRA ORA a 0.000028
🎯 TP1: 0.000042 (+50%)
🎯 TP2: 0.000056 (+100%)
🛑 SL: 0.000024

💰 Gioca QUI (bonus 500€):
🔗 https://stake.com/?c=abc123""")

# Webhook per Telegram
Webhook_URL = f"https://cryptobot-phqq.onrender.com/8548138805:AAE8JNgxiwz3ZifOpSIH0UfiszuPz6X1hG8"

@app.route('/')
def home():
    return "Bot online! 🚀"

@app.route(f'/8548138805:AAE8JNgxiwz3ZifOpSIH0UfiszuPz6X1hG8', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    else:
        return 'Forbidden', 403

# Avvia il bot
if __name__ == "__main__":
    import time
    time.sleep(2)
    print("Setting webhook...")
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(url=Webhook_URL)
    print(f"Webhook set to: {Webhook_URL}")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
