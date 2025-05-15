import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pytest
from simple_math import SimpleMath

@pytest.fixture
def simple_math():
    return SimpleMath()

def test_positive_square(simple_math):
    assert simple_math.square(5) == 25

def test_positive_cube(simple_math):
    assert simple_math.cube(3) == 27