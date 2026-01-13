import unittest
from calculator import calculate


class TestCalculator(unittest.TestCase):

    # Test addition
    def test_addition(self):
        self.assertEqual(calculate("5 + 3"), 8)

    # Test subtraction
    def test_subtraction(self):
        self.assertEqual(calculate("10 - 4"), 6)

    # Test multiplication
    def test_multiplication(self):
        self.assertEqual(calculate("6 * 2"), 12)

    # Test division
    def test_division(self):
        self.assertEqual(calculate("8 / 4"), 2)

    # Test division by zero
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate("5 / 0")

    # Test invalid operator
    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate("5 & 2")

    # Test invalid numbers
    def test_invalid_numbers(self):
        with self.assertRaises(ValueError):
            calculate("a + 2")

    # Test invalid input format
    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            calculate("5 +")


# This runs all test cases
if __name__ == "__main__":
    unittest.main()
