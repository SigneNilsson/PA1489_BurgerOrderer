from flask import Flask, request, redirect
#from flask_socketio import SocketIO, emit


app = Flask(__name__)
#socketio = SocketIO(app)

def index():
    """
    I tried to implement a Websocket to the project to make kitchen view update and show the order to the kitchen staff, as we are running out of time, i will keep the idea of the code here but not implement it in our final work.
    """
#    pg = "<head>"
#    pg += "<title>Kitchen View</title>"
#    pg += "<script src='https://cdn.socket.io/4.0.0/socket.io.min.js'></script>"
#    pg += "<script type='test/javascript'>"
#    pg += """document.addEventListener('DOMContentLoaded, function() {
#                var socket = io.connect('http://' + document.domain + ':' + location.port);
#                
#                socket.on('url_update', function(data) {
#                    console.log('New URL recieved:' data.new_url);
#                    window.location.href = data.new_url;    
#                });
#            });"""
#    pg += "</script>"
#    pg += "</head>"

    return "<strong><h1 style='text-align: center; color: green; background-color: orange;'>Here is the kitchen view!</h1></strong>"


@app.route('/')
def frontpage():
    """
    Defines a route for the home page of a Flask application.
    'Flask is a Python web framework used to build web applications'.
    """
    #new_url = request.args.get('url')
    #socketio.emit('url_update', {'new_url': new_url})
    print('Loading front page', flush=True)
    

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
        print('<br><br><strong>Added ingredients:</strong><br>')
        for ingredient in add_ingredients:
            print(' - ' + ingredient + '<br>')
    
    if remove_ingredients:
        print('<br><strong>Removed ingredients:</strong><br>')
        for ingredient in remove_ingredients:
            print(' - ' + ingredient + '<br>')
    print(f"one {burger_name} ordered with the following options:")
    return pg 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    #socketio.run(app, debug=True, host="0.0.0.0", port=5000)
