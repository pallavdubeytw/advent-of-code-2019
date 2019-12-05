import unittest
from main import *


class MainTest(unittest.TestCase):

    def test_get_total_digits_count(self):
        self.assertEqual(get_total_digits_count(123), 3)
        self.assertEqual(get_total_digits_count(76432), 5)

    def test_get_nth_digit(self):
        self.assertEqual(get_nth_digit(1002, 1), 2)
        self.assertEqual(get_nth_digit(1002, 2), 0)
        self.assertEqual(get_nth_digit(1002, 3), 0)
        self.assertEqual(get_nth_digit(1002, 4), 1)
        self.assertEqual(get_nth_digit(1002, 5), None)
        self.assertEqual(get_nth_digit(2, 3), None)


if __name__ == '__main__':
    unittest.main()
