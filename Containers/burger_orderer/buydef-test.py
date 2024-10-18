"""pytest"""
import pytest


def addOptions(url, args, prefix):
    if args:
        url += '?' if '?' not in url else '&'
        url += '&'.join([f'{prefix}={arg}' for arg in args])
    return url
#the function from burger_order being tested




def addOptions(url, args):
    """Adds query parameters to a given URL. The URL with the appended query parameters."""
    if 0 != len(args):
        url += '?'
        for arg in args:
            url += arg + '&'
    return url



def test_addOptions():
    """Testa addOptions-funktionen med pytest"""
    assert addOptions("http://example.com", ["param1=value1", "param2=value2"]) == "http://example.com?param1=value1&param2=value2&"
    assert addOptions("http://example.com", []) == "http://example.com"
    assert addOptions("http://example.com", ["param=value"]) == "http://example.com?param=value&"
    
    
if __name__ == "__main__":
    pytest.main()
