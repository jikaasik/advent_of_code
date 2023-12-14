import pytest
from solution_1 import main as part_one
# from solution_2 import main as part_two


def test_part_one():
    response = part_one()
    assert len(response) == 2
    assert response[0][0] == 4361
    assert response[0][1] == 467835
    assert response[1][0] == 517021
    assert response[1][1] == 81296995