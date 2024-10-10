"""Kitchen View"""

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def frontpage():
    """
    Defines a route for the home page of a Flask application.
    'Flask is a Python web framework used to build web applications'.
    """
       
    print('Loading front page', flush = True)
    return "<strong><h1 style='text-align: center; color: green; background-color: orange;'>Here is the kitchen view!</h1></strong>"

def buy(burger_name):
    
    """Defines a function called 'buy'.'
    Takes an argument and prints an order confirmation for a hamburger.
    lists all options."""
    print('One ' + burger_name + ' ordered with the following options:')
    for arg in request.args:
        print(' - ' + arg)
    return "ok"


if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)