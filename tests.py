import unittest
from code.logic import TuringMachine

class TestTuringMachine(unittest.TestCase):

    def test_correct_input(self):
        tm = TuringMachine({0, 1}, {"a", "b", "c"}, [0, 1, 0, 1], [(("a", 1), ("b", 0, "R"))], "a", "c")
        self.assertTrue(tm.check_input())
