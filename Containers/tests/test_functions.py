"""Automated tests"""

import pytest
from ./burger_orderer import *

def test_getBurgers():
    burgers = getBurgers()

    assert(len(burgers) == 3)