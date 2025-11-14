import telebot
import time
import random
import os
import threading
from flask import Flask, request

app = Flask(__name__)

TOKEN = "8548138805:AAE8JNgxiwz3ZifOpSIH0UfiszuPz6X1hG8"
CHANNEL = "@CryptoKing_Signalss"
PRESALE_ACTIVE = False  # ← Cambia in True quando hai il MINT
SOL_MINT = "Launching_in_24h..."  # ← Placeholder

bot = telebot.TeleBot(TOKEN)

# ================== FOMO MESSAGES (10 tipi) ==================
FOMO_MESSAGES = [
    """COUNTDOWN TO $KING PRESALE

Only 24 hours left!
1 SOL = 100,000 $KING
100x guaranteed on Raydium

First 100 buyers → 500k BONUS

Get ready...""",

    """WHALE ALERT

A 50+ SOL whale just joined the waitlist!
They know what's coming...

$KING presale drops in <18h""",

    """LAST CHANCE TO JOIN

Presale spots: 73/100 filled
Once gone → NO BONUS

$KING = next 100x gem""",

    """DEV JUST LOCKED LP

100% fair launch
No rug, no dump
Presale live in 12h""",

    """EARLY BIRD BONUS

First 50 buyers get:
+500k $KING extra
+ VIP pump group access

Clock is ticking...""",

    """$KING ON DEXSCREENER SOON

Chart loading...
Volume incoming...
Presale in <10h""",

    """COMMUNITY IS HEATING UP

500+ members in 2 hours
FOMO is real

Presale drops TONIGHT""",

    """$KING AIRDROP FOR HOLDERS

Hold 50k $KING at launch → get 10k extra FREE

Presale in 8 hours""",

    """DEV DOXXED ON TWITTER

Follow @CryptoKingPump
Live AMA in 6 hours

Presale starts right after""",

    """FINAL WARNING

Presale ends in 4 hours
After that → public price +50%

Secure your bag NOW"""
]

# ================== INVIO FOMO RANDOM ==================
def send_fomo():
    text = random.choice(FOMO_MESSAGES)
    try:
        bot.send_message(CHANNEL, text)
        print(f"FOMO inviato: {text.splitlines()[0]}")
    except Exception as e:
        print(f"Errore FOMO: {e}")

# ================== FOMO LOOP (ogni 30–90 min) ==================
def fomo_loop():
    while not PRESALE_ACTIVE:
        send_fomo()
        # Random tra 30 e 90 minuti
        delay = random.randint(1800, 5400)
        time.sleep(delay)

threading.Thread(target=fomo_loop, daemon=True).start()

# ================== PRIMO POST SUBITO ==================
@app.route('/')
def home():
    send_fomo()
    return "FOMO MODE ACTIVATED – Presale coming!"

# ================== WEBHOOK ==================
@app.route('/webhook', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'OK', 200

if __name__ == "__main__":
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(url=f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/webhook")
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
