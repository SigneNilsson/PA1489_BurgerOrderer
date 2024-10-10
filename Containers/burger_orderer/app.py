from flask import Flask, request
import os 
import requests

app = Flask(__name__)

staticBurgers = [
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
        pg += "<LI>" + b['name'] + " - "
        for items in b["ingredients"]:
            pg += items + ", " 

    pg += "</UL>"
    pg += f"<form action='' method='GET'>"

    for burgers in getBurgers():
        pg += f"<label for='{burgers['name']}'>{burgers['name']}</label>"
        pg += f"<input type='radio' name='burgers' value='{burgers['name']}'><br><br>"

    pg += "<h3>Choose ingredients to add or remove:</h3>"
    all_ingredients = set(item for burger in getBurgers() for item in burger['ingredients'])
    pg += "<strong>Add ingredients of your choice.</strong><br>"
    for ingredient in all_ingredients:
        pg += f"<input type='checkbox' name='add_ingredients' value='{ingredient}'> Add {ingredient}<br>"

    
    pg += "<strong>Remove ingredients from your burger.</strong><br>"
    for ingredient in all_ingredients:
        pg += f"<input type='checkbox' name='remove_ingredients' value='{ingredient}'> Remove {ingredient}<br>"
        

    pg += "<input type='submit' value='Submit'>"
    #pg += f"<button type='button' onClick''>forwarding test</button>"
    
    pg += "</form>"
    if request.args.get('burgers', '0') == '0':
        pg += "<strong>Please choose a burger.</strong>"
    else:
        burger_name = request.args.get('burgers')
        add_ingredients = request.args.getlist('add_ingredients')
        remove_ingredients = request.args.getlist('remove_ingredients')
        sendToKitchen(burger_name, add_ingredients, remove_ingredients)
    return pg


def renderOrderingPage(burgerName, add_ingredients, remove_ingredients):
    """
    Confirmation that the customers burger order has been made and what they ordered.
    """
    return f'Ordered {burgerName} with added ingredients: {", ".join(add_ingredients)} and without: {", ".join(remove_ingredients)}'
    
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

def addOptions(url, args, prefix):
    if args:
        url += '?' if '?' not in url else '&'
        url += '&'.join([f'{prefix}={arg}' for arg in args])
    return url

def sendToKitchen(burgerName, add_ingredients = None, remove_ingredients = None):
    if burgerName != "0":
        requrl = makeURL(burgerName)
        if add_ingredients:
            requrl = addOptions(requrl, add_ingredients, 'add')
        if remove_ingredients:
            requrl = addOptions(requrl, remove_ingredients, 'remove')

        print('Using KitchenView URL: ' + requrl)
        requests.get(requrl)
        
        return 
    return print("Please choose a burger.")


@app.route('/buy/<burgerName>', methods=['get'])
def buy(burgerName):
    add_ingredients = request.args.getlist('add')
    remove_ingredients = request.args.getlist('remove')
    print(f'Placing an order on {burgerName} with additions: {add_ingredients} and removals: {remove_ingredients}')
    sendToKitchen(burgerName, add_ingredients, remove_ingredients)
    return renderOrderingPage(burgerName, add_ingredients, remove_ingredients)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)