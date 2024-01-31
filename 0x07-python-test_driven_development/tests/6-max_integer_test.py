#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
"""
Defines a class which tests for max_integer in
6-max_integer module.
"""


class TestMaxInteger(unittest.TestCase):
    """Defines multiple tests for function max_integer"""
    def test_max(self):
        """tests outputs for function"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1.66, -2.33, 3.77, 0.55]), 3.77)
        self.assertEqual(max_integer([1.66, -2.33, 2, 2.5]), 2.5)
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer("Magnus"), 'u')
        self.assertEqual(max_integer("He is a boy"), 'y')


if __name__ == '__main__':
    unittest.main()
