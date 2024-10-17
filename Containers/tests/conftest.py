import pytest
from burger_orderer.app import *

""" def buy2():
    return getBurgers()


@pytest.buy2
def buy2():
    assert buy2(getBurgers)"""
    
@pytest.fixture
def client():
    burgers = getBurgers()
    with burgers.test_client() as client:
        yield client
