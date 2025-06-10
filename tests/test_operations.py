import pytest # type: ignore
from app.operations import addition, subtraction, multiplication, division

def test_addition():
    assert addition(1, 1) == 2

def test_subtraction():
    assert subtraction(1, 1) == 0

def test_multiplication():
    assert multiplication(2, 3) == 6

def test_division():
    assert division(4, 2) == 2

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)