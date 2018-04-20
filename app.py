from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'




@app.route('/welcome/<name>')
def get_welcome(name):
    """

    :param name:
    :return: message based on daytime
    """
    # current hour of the day
    hour = datetime.now().hour

    greeting = ""
    if (0 <= hour < 6):
        greeting = "Good night"
    elif (6 <= hour < 10):
        greeting = "Good morning"
    elif (10 <= hour < 14):
        greeting = "Good mid-day"
    elif (14 <= hour < 18):
        greeting = "Good afternoon"
    elif (18 <= hour < 24):
        greeting = "Good evening"

    greeting = greeting + " " + name
    print(greeting)

    return greeting


if __name__ == '__main__':
    app.run()
