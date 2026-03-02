"""
Unit test for Calculator class
"""

import sys
import os
from calculator import Calculator

# absolute path setup
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_addition():
    """Test addition operation"""
    calc = Calculator()
    assert calc.add(5, 3) == 8
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0
    print("✓ Addition tests passed")


def test_subtraction():
    """Test subtraction operation"""
    calc = Calculator()
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(-3, -3) == 0
    print("✓ Subtraction tests passed")


def test_multiplication():
    """Test multiplication operation"""
    calc = Calculator()
    assert calc.multiply(4, 5) == 20
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 100) == 0
    print("✓ Multiplication tests passed")


def test_division():
    """Test division operation"""
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(7, 2) == 3.5

    # Test division by zero
    try:
        calc.divide(5, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

    print("✓ Division tests passed")


def test_history():
    """Test history functionality"""
    calc = Calculator()
    calc.add(1, 2)
    calc.multiply(3, 4)

    history = calc.get_history()
    assert len(history) == 2

    calc.clear_history()
    assert len(calc.get_history()) == 0
    print("✓ History tests passed")


if __name__ == "__main__":
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    test_history()

    print("\n✓ All tests passed successfully!")