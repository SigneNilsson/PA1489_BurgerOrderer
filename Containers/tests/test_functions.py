"""Automated tests"""

#import pytest
from app import getBurgers

def test_getBurgers():
    """  """
    burgers = getBurgers()
    assert(len(burgers) == 3)