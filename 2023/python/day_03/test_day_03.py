import pytest
from solution_1 import main as part_one
# from solution_2 import main as part_two


def test_part_one():
    response = part_one()
    assert len(response) == 2
    assert response[0] == 4361
    pass


# def test_part_two():
#     pass