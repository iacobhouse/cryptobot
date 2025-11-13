from flask import Flask
import telebot
import os

app = Flask(__name__)
bot = telebot.TeleBot("8548138805:AAE8JNgxiwz3ZifOpSIH0UfiszuPz6X1hG8")  # ← Sostituisci con il tuo token

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, """🚀 CRYPTO KING SIGNALS 🚀
    
🔥 Segnali GRATIS ogni 4 ore
🎰 Bonus 500€ senza deposito

Clicca /segnali""")

@bot.message_handler(commands=['segnali'])
def segnali(message):
    bot.reply_to(message, """⚡ SEGNALE LIVE ⚡
$BONK entra ORA a 0.000028
🎯 TP1: +50% | TP2: +100%
🛑 SL: 0.000024

Gioca QUI (bonus 500€):
🔗 https://stake.com/?c=TUOCODICE""")

@app.route('/')
def home():
    return "Bot online!"

@app.route('/' + "IL_TUO_TOKEN_QUI", methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://crypto-bot.onrender.com/" + "IL_TUO_TOKEN_QUI")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
