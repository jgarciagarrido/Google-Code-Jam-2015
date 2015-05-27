import unittest
from solve import *


class TestInviteFriends(unittest.TestCase):
    def test_sample_4(self):
        sample = "1"
        result = invite_friends(sample)
        self.assertEqual(result, 0)

    def test_sample_2(self):
        sample = "09"
        result = invite_friends(sample)
        self.assertEqual(result, 1)

    def test_sample_1(self):
        sample = "11111"
        result = invite_friends(sample)
        self.assertEqual(result, 0)

    def test_sample_3(self):
        sample = "110011"
        result = invite_friends(sample)
        self.assertEqual(result, 2)


class TestSolveStandingOvation(unittest.TestCase):
    def test_can_solve_the_problem(self):
        solve_standing_ovation("test")
        output_file = open("test.out")
        expected_content = "Case #1: 0\n"
        expected_content += "Case #2: 1\n"
        expected_content += "Case #3: 2\n"
        expected_content += "Case #4: 0\n"
        self.assertEqual(output_file.read(), expected_content)

if __name__ == '__main__':
    unittest.main()
