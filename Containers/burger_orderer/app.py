from flask import Flask, request, url_for
import os 
import requests

app = Flask(__name__)

staticBurgers= [
    {
        'name': "Mostafaburgare",
        "ingredients": ["bread", "plantbeef", "sauce","onion", "salad", "tomato", "cucumber"]
    },
    {
        'name': "Signeburgare",
        "ingredients": ["bread", "halloumi","sauce", "onion", "salad", "avocado"]
    },
    {
        'name': "Eidamburgare",
        "ingredients": ["bread", "meat","cheddar", "pickle", "ranch mayo", "portabello mushroom"]
    }
]


def getBurgers():
    return staticBurgers


def renderFrontpage():
    pg = "<h1>Welcome to BurgerOrderer</h1>"
    pg += "<P><UL>"
    
    for b in getBurgers():
        pg += "<LI>" + b['name']
#request.form.get('burgers', '')
    pg += "</UL>"
    pg += f"<form action='' method='GET'>"

    for burgers in getBurgers():
        pg += f"<label for='{burgers['name']}'>{burgers['name']}</label>"
        pg += f"<input type='radio' name='burgers' value='{burgers['name']}'><br><br>"

    pg += "<input type='submit' value='Submit'>"
    #pg += f"<button type='button' onClick''>forwarding test</button>"
    {sendToKitchen(request.form.get('burgers', ''), ['pickle', 'bread'])}
    pg += "</form>"
    return pg

def renderOrderingPage(burgerName, args):
    return 'ordered ' + burgerName
    
@app.route('/')
def frontpage():
    return renderFrontpage()

#baseURL='http://' + os.getenv('KITCHENVIEW_HOST', 'localhost:5000')
baseURL = 'http://localhost:5000'

def makeURL(burgerName):
    return baseURL + '/buy/' + burgerName

def addOptions(url, args):
    print(url)
    if 0!=len(args):
        url += '?'
        for arg in args:
            url += arg + '&'
    return url

def sendToKitchen(burgerName, args):
    requrl = makeURL(burgerName)
    print(args)
    print("jag vill inte mer ")
    requrl = addOptions(requrl, args)

    print('Using KitchenView URL: ' + requrl)
    requests.get(requrl)
    return
   

@app.route('/buy/<burgerName>', methods=['get'])
def buy(burgerName):
    print('Placing an order on ' + burgerName)
    sendToKitchen(burgerName,  '')#requests.args
    return renderOrderingPage(burgerName, request.args)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
