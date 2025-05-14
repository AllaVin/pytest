import pytest
from .simple_math import SimpleMath

import sys

@pytest.fixture
def simple_math():
    return SimpleMath()

def test_positive_square(simple_math):
    assert simple_math.square(5) == 25

def test_positive_cube(simple_math):
    assert simple_math.cube(3) == 27