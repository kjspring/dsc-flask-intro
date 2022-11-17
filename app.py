# import flask here
from flask import Flask

# create new flask app here
app = Flask(__name__)

# define routes for your new flask app
@app.route('/', methods=['GET'])
def index():
    return 'Hello, world!'

@app.route('/welcome', methods=['GET'])
def welcome():
    return 'Welcome to an amazing Flask App!'

@app.route('/goodbye', methods=['GET'])
def goodbye():
    return 'Thanks for looking around. Come back again soon!'
