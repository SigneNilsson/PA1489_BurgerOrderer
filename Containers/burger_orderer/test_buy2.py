import pytest
from app import buy2, getBurgers

""" def buy2():
    return getBurgers()


@pytest.buy2
def buy2():
    assert buy2(getBurgers)"""
    
    
def test_getBurgers():
    burgers = getBurgers()

    assert(len(burgers) == 3)
