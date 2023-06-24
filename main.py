from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    # Generate a random number
    import random
    random_number = random.randint(1, 100)
    
    # Set up the result data
    result = f"The random number is: {random_number}"
    
    # Save the result to the provided URL
    url = 'https://rentry.co/gasfwqfqwf'
    data = {'result': result}
    response = requests.post(url, data=data)
    
    # Handle the response
    if response.status_code == 200:
        return 'Result saved successfully!'
    else:
        return 'An error occurred while saving the result.'

if __name__ == '__main__':
    app.run()
