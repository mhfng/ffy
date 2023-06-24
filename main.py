from flask import Flask

import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase app
cred = credentials.Certificate('dddy-e3783-firebase-adminsdk-33t56-6782f9d539.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'dddy-e3783.appspot.com'})

app = Flask(__name__)

@app.route('/write-file')
def write_file():
    # Get a reference to the file you want to write to
    bucket = storage.bucket()
    file_blob = bucket.blob('a.txt')

    # Write content to the file
    file_blob.upload_from_string('Hello, world!', content_type='text/plain')

    return 'File uploaded successfully.'

if __name__ == '__main__':
    app.run()
