import unittest
import day_04


class Test(unittest.TestCase):
    def test_has_two_adj_numbers(self):
        self.assertTrue(day_04.has_adj_numbers(22))
        self.assertFalse(day_04.has_adj_numbers(123234))
        self.assertTrue(day_04.has_adj_numbers(122345))
        self.assertFalse(day_04.has_adj_numbers(123234))

    def test_is_decreasing(self):
        self.assertFalse(day_04.is_decreasing(111123))
        self.assertFalse(day_04.is_decreasing(135679))
        self.assertTrue(day_04.is_decreasing(5356))
        self.assertTrue(day_04.is_decreasing(96326))


if __name__ == '__main__':
    unittest.main()
