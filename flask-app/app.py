from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, this is the flask app running on docker container.'

@app.route('/health')
def health():
    return 'Server is up and running'
