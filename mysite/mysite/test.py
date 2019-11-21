from django.test import TestCase

from mysite.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test that two numbers are subtracted and returned"""
        self.assertEqual(subtract(8, 3), 5)
