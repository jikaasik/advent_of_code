import pytest
from solution import get_input

def test_get_input():
    try:
        txt = get_input("input_demo.txt")
        assert txt == "This is some demo input text"
    except:
        import pdb; pdb.set_trace()
