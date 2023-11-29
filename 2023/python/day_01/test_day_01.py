import pytest
from solution import get_input

def test_get_input():
    txt = get_input("input_demo.txt")
    assert txt == "This is some demo input text"
