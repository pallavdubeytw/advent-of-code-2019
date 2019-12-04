import unittest
import day_04


class Test(unittest.TestCase):
    def test_has_two_adj_numbers(self):
        self.assertTrue(day_04.has_two_adj_numbers(12635633))
        self.assertFalse(day_04.has_two_adj_numbers(123234))
        self.assertTrue(day_04.has_two_adj_numbers(19346188))
        self.assertFalse(day_04.has_two_adj_numbers(123234))
