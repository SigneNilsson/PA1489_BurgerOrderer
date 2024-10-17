"""Module with functions used in burger_orderer app"""
import pytest

staticBurgers = [
    {
        'name': "Mostafaburger",
        "ingredients": ["Bread", "Plantbeef", "Sauce", "Onion", "Salad", "Tomato", "Cucumber"]
    },
    {
        'name': "Signeburger",
        "ingredients": ["Bread", "Halloumi", "Sauce", "Onion", "Salad", "Avocado"]
    },
    {
        'name': "Eidamburger",
        "ingredients": ["Bread", "Beef", "Cheddar", "Pickles", "Ranch mayo", "Portabello mushroom"]
    }
]

def getBurgers():
    """returns the burgers. At the moment the burger data is retrieved using the dictionary static_burgers. The plan is to incorporate the connection to
    the database and retrieve the data from the database instead"""
    """ try: 
        sql = connect_to_db()
        sql = sql.cursor()
        sql.execute('SELECT * FROM menu_item')
        return_val = sql.fetchall()
        print(return_val)
        sql.close()
        
    except Exception as err:
        print(err) """
    
    return staticBurgers

Burgers = getBurgers()
try:
    wrongBurgers = getBurgers("a")
except TypeError
    print("Not allowed")
    
