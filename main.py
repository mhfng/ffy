from flask import Flask, render_template, request
from google.cloud import storage

app = Flask(__name__)
client = storage.Client.from_service_account_json('dddy-e3783-firebase-adminsdk-33t56-6782f9d539.json')
bucket_name = 'dddy-e3783.appspot.com'
blob_name = 'a.txt'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_to_storage', methods=['POST'])
def send_to_storage():
    textbox_value = request.form.get('textbox')
    if textbox_value:
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_string(textbox_value)
        return 'Textbox value sent to storage successfully.'
    else:
        return 'Textbox value is empty.'

if __name__ == '__main__':
    app.run()
