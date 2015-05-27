import unittest
from solve import *


class TestCleanPlates(unittest.TestCase):
    def test_clean_array_witt_one_empty_plate(self):
        result = clean_plates([0, ])
        self.assertEqual(result, [])

    def test_clean_array_with_various_plates(self):
        result = clean_plates([0, 1, 3, 9])
        self.assertEqual(result, [1, 3, 9])


class TestEstimatedFinish(unittest.TestCase):
    def test_empty_house(self):
        result = estimated_finish([])
        self.assertEqual(result, 0)

    def test_one_minute(self):
        result = estimated_finish([1])
        self.assertEqual(result, 1)

    def test_sample(self):
        result = estimated_finish([1, 2, 1, 2])
        self.assertEqual(result, 2)


class TestEstimatedFinishMoving(unittest.TestCase):
    def test_sample_pair(self):
        result = estimated_finish_moving([1, 4, 1, 2])
        self.assertEqual(result, 3)

    def test_sample_odd(self):
        result = estimated_finish_moving([1, 5, 1, 2])
        self.assertEqual(result, 4)

    def test_sample_odd_two_max(self):
        result = estimated_finish_moving([1, 5, 1, 2, 5])
        self.assertEqual(result, 6)


class TestClientsEat(unittest.TestCase):
    def test_clients_eat_one_pancake(self):
        result = clients_eat([1, 5, 1, 2])
        self.assertEqual(result, [0, 4, 0, 1])


class TestNormalMinute(unittest.TestCase):
    def test_clients_eat_one_pancake(self):
        result = normal_minute([1, 5, 1, 2])
        self.assertEqual(result, [4, 1])


class TestSpecialMinute(unittest.TestCase):
    def test_moving(self):
        result = special_minute([1, 5, 1, 2])
        self.assertEqual(result, [1, 3, 1, 2, 2])


class TestPassMinute(unittest.TestCase):
    def test_moving(self):
        result = pass_minute([1, 5, 1, 2])
        self.assertEqual(result, [1, 3, 1, 2, 2])

    def test_do_nothing(self):
        result = pass_minute([1, 2, 1, 2])
        self.assertEqual(result, [1, 1])


class TestMinutesToFinish_breakfast(unittest.TestCase):
    def test_sample_1(self):
        result = minutes_to_finish_breakfast([3, ])
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
