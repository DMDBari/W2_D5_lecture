from unittest import TestCase

from whiteboard import solution

class MatchTestCase2(TestCase):
    def test_general1(self):
        self.assertEqual(solution("bitcoin take over the world maybe who knows perhaps"), 3)
    def test_general2(self):
        self.assertEqual(solution("turns out random test cases are easier than writing out basic ones"), 3)
    def test_general3(self):
        self.assertEqual(solution("lets talk about javascript the best language"), 3)
    def test_general4(self):
        self.assertEqual(solution("i want to travel the world writing code one day"), 1)