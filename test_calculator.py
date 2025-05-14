from .calculator import Calculator
import pytest
# import sys

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.skip
def test_positiv_number(calculator):
    assert calculator.sum(4, 5) == 9

@pytest.mark.positive_test
def test_positiv_division(calculator):
    assert calculator.divide(4, 5) == 0.8

@pytest.mark.skipif(condition="sys.version_info < (3, 8)", reason="Требуется Python 3.8 или выше")
def test_positiv_subtraction(calculator):
    assert calculator.subtract(4, 5) == -1