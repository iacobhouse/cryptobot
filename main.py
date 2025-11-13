from flask import Flask, request
import telebot
import os
import json
import time

app = Flask(__name__)

# ⚠️ SOSTITUISCI CON IL TUO TOKEN
TOKEN = "8548138805:AAE8JNgxiwz3ZifOpSIH0UfiszuPz6X1hG8"  # Es. 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
bot = telebot.TeleBot(TOKEN)

# Comandi
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, """🚀 CRYPTO KING SIGNALS 🚀
    
🔥 Segnali GRATIS ogni 4 ore
🎰 Bonus 500€ senza deposito

Clicca /segnali per il prossimo!""")
    print(f"DEBUG: Messaggio /start ricevuto da {message.from_user.first_name}")  # Log per debug

@bot.message_handler(commands=['segnali'])
def segnali(message):
    bot.reply_to(message, """⚡ SEGNALE LIVE ⚡
    
🪙 $BONK
📈 ENTRA ORA a 0.000028
🎯 TP1: 0.000042 (+50%)
🎯 TP2: 0.000056 (+100%)
🛑 SL: 0.000024

💰 Gioca QUI (bonus 500€):
🔗 https://stake.com/?c=TUOCODICE""")
    print(f"DEBUG: Messaggio /segnali ricevuto")  # Log per debug

# Webhook endpoint
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    try:
        print("DEBUG: POST request ricevuto da Telegram")  # Log arrivo
        if request.headers.get('content-type') == 'application/json':
            json_string = request.get_data().decode('utf-8')
            print(f"DEBUG: JSON ricevuto: {json_string[:200]}...")  # Log JSON parziale
            update = telebot.types.Update.de_json(json_string)
            if update:
                bot.process_new_updates([update])
                print("DEBUG: Update processato con successo")
            else:
                print("DEBUG: Errore parsing JSON")
        else:
            print(f"DEBUG: Content-Type sbagliato: {request.headers.get('content-type')}")
        return '', 200
    except Exception as e:
        print(f"DEBUG: Errore nel webhook: {str(e)}")  # Log errori
        return 'Errore interno', 500

@app.route('/')
def home():
    return "Bot online! 🚀 Webhook pronto."

# Avvia il bot
if __name__ == "__main__":
    print("DEBUG: Avvio app...")
    time.sleep(5)  # Pausa per init
    print("DEBUG: Rimuovo webhook vecchio...")
    bot.remove_webhook(drop_pending_updates=True)  # Pulisce pending updates!
    time.sleep(2)
    webhook_url = f"https://cryptobot-phqq.onrender.com//{TOKEN}"  # ← SOSTITUISCI 'crypto-bot' se nome diverso
    print(f"DEBUG: Setto webhook su {webhook_url}")
    bot.set_webhook(url=webhook_url, drop_pending_updates=True)  # Pulisce di nuovo
    print("DEBUG: Webhook settato! App in ascolto.")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
