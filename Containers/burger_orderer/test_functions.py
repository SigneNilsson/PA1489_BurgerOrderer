"""Automated test for getBurgers"""

import pytest

def test_getBurgers():
    """Test get burgers as to assert there are three burgers"""
    burgers = getBurgers()
    assert(len(burgers) == 3)