"""
Sample tests
"""
from django.test import TestCase, SimpleTestCase
from .calc import add, subtract

class CalcTest(SimpleTestCase):

    def test_add_numbers(self):
        res = add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = subtract(6, 5)
        self.assertEqual(res, 1)