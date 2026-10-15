import pytest
from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -1) == -2


def test_subtract():
    assert subtract(5, 3) == 2


def test_subtract_negative():
    assert subtract(3, 5) == -2


def test_multiply():
    assert multiply(2, 4) == 8


def test_multiply_by_zero():
    assert multiply(5, 0) == 0


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)