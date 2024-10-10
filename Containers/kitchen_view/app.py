from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def frontpage():
    """
    Defines a route for the home page of a Flask application.
    'Flask is a Python web framework used to build web applications'.
    """
    print('Loading front page', flush=True)
    return "<strong><h1 style='text-align: center; color: green; background-color: orange;'>Here is the kitchen view!</h1></strong>"

@app.route('/buy/<burger_name>', methods=['GET'])
def buy(burger_name):
    """
    Defines a function called 'buy'.
    Takes an argument and prints an order confirmation for a hamburger.
    Lists all options.
    """
    print('One ' + burger_name + ' ordered with the following options:')
    add_ingredients = request.args.getlist('add')
    remove_ingredients = request.args.getlist('remove')
    
    if add_ingredients:
        print('Added ingredients:')
        for ingredient in add_ingredients:
            print(' - ' + ingredient)
    
    if remove_ingredients:
        print('Removed ingredients:')
        for ingredient in remove_ingredients:
            print(' - ' + ingredient)
    
    return "ok"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
