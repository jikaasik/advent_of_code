import pytest
from solution_1 import main as part_one
from solution_2 import main as part_two


def test_part_one():
    response = part_one()
    assert response[0] == 142
    assert response[1] == 55538

def test_part_two():
    response = part_two()
    assert response[0] == 281