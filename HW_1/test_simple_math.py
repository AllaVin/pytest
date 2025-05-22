import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pytest
from HW.HW_1.simple_math import SimpleMath

@pytest.fixture
def simple_math():
    return SimpleMath()

def test_positive_square(simple_math):
    assert simple_math.square(5) == 25

def test_positive_cube(simple_math):
    assert simple_math.cube(3) == 27

def test_positive_sum(simple_math):
    assert simple_math.sum(10, 2) == 12

def test_positive_diff(simple_math):
    assert simple_math.diff(16, 13) == 3

# Usage of markers. In Output it will be marked as 'skipped'.
# How to apply markers?
# Under the text you have to wright @pytest.mark.marker_name.
# Flag -m allow to run only tests with specific markers. Example '-m positive_test'

@pytest.mark.skip(reason="Test will be updated later")
def test_positive_avg(simple_math):
    assert simple_math.avg([1, 2, 3, 4, 5]) == 3