from flask import Flask, request, redirect
import os 
import requests

app = Flask(__name__)

staticBurgers= [
    {
        'name': "Mostafaburgare",
        "ingredients": ["bread", "plantbeef", "sauce", "onion", "salad", "tomato", "cucumber"]
    },
    {
        'name': "Signeburgare",
        "ingredients": ["bread", "halloumi", "sauce", "onion", "salad", "avocado"]
    },
    {
        'name': "Eidamburgare",
        "ingredients": ["bread", "meat", "cheddar", "pickle", "ranch mayo", "portabello mushroom"]
    }
]


def getBurgers():
    return staticBurgers


def renderFrontpage():
    """
    Renders the main page of the burger_orderer project
    """
    pg = "<h1>Welcome to BurgerOrderer</h1>"
    pg += "<P><UL>"
    
    for b in getBurgers():
        pg += "<LI>" + b['name']

    pg += "</UL>"
    pg += f"<form action='' method='GET'>"

    for burgers in getBurgers():
        pg += f"<label for='{burgers['name']}'>{burgers['name']}</label>"
        pg += f"<input type='radio' name='burgers' value='{burgers['name']}'><br><br>"

    pg += "<input type='submit' value='Submit'>"
    #pg += f"<button type='button' onClick''>forwarding test</button>"
    
    sendToKitchen(request.args.get('burgers', '0'), ['pickle', 'bread'])
    pg += "</form>"
    if request.args.get('burgers', '0') == '0':
        pg += "<strong>Please choose a burger.</strong>"

    return pg

def renderOrderingPage(burgerName, args):
    """
    Confirmation that the customers burger order has been made and what they ordered.
    """
    return 'ordered ' + burgerName + ' without following toppings: ' + (', '.join(str(arg) for arg in args))
    
@app.route('/')
def frontpage():
    """
    Calls the frontpage function and prints the frontpage
    """
    return renderFrontpage()

#baseURL='http://' + os.getenv('KITCHENVIEW_HOST', 'localhost:5000')
baseURL = 'http://localhost:5000'

def makeURL(burgerName):
    """
    creates a REST API URL to prepare communication with the kitchen view
    """
    return baseURL + '/buy/' + burgerName

def addOptions(url, args):
    if 0!=len(args):
        url += '?'
        for arg in args:
            url += arg + '&'
    return url

def sendToKitchen(burgerName, args):
    if burgerName != "0":
        requrl = makeURL(burgerName)
        requrl = addOptions(requrl, args)
        #redurl = addOptions('http://localhost:8000/buy/' + burgerName, args)

        print('Using KitchenView URL: ' + requrl)
        requests.get(requrl)
        
        return
    return print("Please choose a burger.")


@app.route('/buy/<burgerName>', methods=['get'])
def buy(burgerName):
    print('Placing an order on ' + burgerName)
    sendToKitchen(burgerName,  '')
    return renderOrderingPage(burgerName, request.args)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
