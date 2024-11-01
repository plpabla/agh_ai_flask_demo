"""Unit tests for Calculator class."""

import pytest
from calculator import Calculator


def test_add():
    """Test the sum method of the Calculator class."""
    calculator = Calculator(1, 2)
    assert calculator.sum() == 3


def test_subtract():
    """Test the diff method of the Calculator class."""
    calculator = Calculator(1, 2)
    assert calculator.diff() == -1


def test_multiply():
    """Test the mul method of the Calculator class."""
    calculator = Calculator(1, 2)
    assert calculator.mul() == 2


def test_divide():
    """Test the div method of the Calculator class."""
    calculator = Calculator(1, 2)
    assert calculator.div() == pytest.approx(0.5, 0.001)


def test_divide_by_zero():
    """Test the div method of the Calculator class with division by zero."""
    calculator = Calculator(1, 0)
    with pytest.raises(ValueError):
        calculator.div()
