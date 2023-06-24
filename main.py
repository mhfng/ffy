from flask import Flask, jsonify
import os
from telegram import Bot

app = Flask(__name__)



# Set up your Telegram bot token
bot_token = '5412336519:AAH-HGiiJJ-AZE3D5FF9457pJACcT-jbqQg'

# Create a bot instance
bot = Bot(token=bot_token)

@app.route('/')
def send_message():
    # Send a message to the chat
    chat_id = 'localipy'
    bot.send_message(chat_id=chat_id, text='Hello, world!')
    return 'Message sent!'


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
