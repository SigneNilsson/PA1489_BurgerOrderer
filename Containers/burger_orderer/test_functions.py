"""Automated test for getBurgers"""

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
    return staticBurgers


def test_getBurgers():
    """Test get burgers as to assert there are three burgers"""
    burgers = getBurgers()
    assert(len(burgers) == 3)