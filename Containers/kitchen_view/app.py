from flask import Flask, request, redirect


app = Flask(__name__)

def index():
    return "<strong><h1 style='text-align: center; color: green; background-color: orange;'>Here is the kitchen view!</h1></strong>"


@app.route('/')
def frontpage():
    """
    Defines a route for the home page of a Flask application.
    'Flask is a Python web framework used to build web applications'.
    """
    print('Loading front page', flush=True)
    if request.args.get('url', '0') != '0':
        print("123")
        return redirect(request.args.get('url', 'url has not been sent'))
    return index()


@app.route('/buy/<burger_name>', methods=['GET'])   
def buy(burger_name):
    """
    Defines a function called 'buy'.
    Takes an argument and prints an order confirmation for a hamburger.
    Lists all options.
    """
     
    pg = index()
    pg += 'One ' + burger_name + ' ordered with the following options:'
    add_ingredients = request.args.getlist('add')
    remove_ingredients = request.args.getlist('remove')
    
    if add_ingredients:
        pg += '<br><br><strong>Added ingredients:</strong><br>'
        for ingredient in add_ingredients:
            pg += ' - ' + ingredient + '<br>'
    
    if remove_ingredients:
        pg += '<br><strong>Removed ingredients:</strong><br>'
        for ingredient in remove_ingredients:
            pg += ' - ' + ingredient + '<br>'
    
    return pg 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
