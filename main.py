import requests

@app.route('/write_file')
def write_file():
    file_url = 'https://firebasestorage.googleapis.com/v0/b/dddy-e3783.appspot.com/o/a.txt?alt=media&token=e0c0ada9-a764-4ef8-a10a-1591be6b4ebe'
    text = 'This is the text to write to the file.'

    response = requests.put(file_url, data=text)

    if response.status_code == 200:
        return 'Text written to the file successfully.'
    else:
        return 'Error writing text to the file.'

