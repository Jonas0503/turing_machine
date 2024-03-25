import unittest
from code.logic import TuringMachine

class TestTuringMachine(unittest.TestCase):

    def test_correct_input(self):
        tm = TuringMachine({0, 1}, {"a", "b", "c"}, [0, 1, 0, 1], [(("a", 1), ("b", 0, "R"))], "a", "c")
        self.assertTrue(tm.check_input())

    def test_start_state_not_in_states(self):
        tm = TuringMachine({0, 1}, {"a", "b", "c"}, [0, 1, 0, 1], [(("a", 1), ("b", 0, "R"))], "k", "c")
        self.assertFalse(tm.check_input())

    def test_end_state_not_in_states(self):
        tm = TuringMachine({0, 1}, {"a", "b", "c"}, [0, 1, 0, 1], [(("a", 1), ("b", 0, "R"))], "a", "k")
        self.assertFalse(tm.check_input())

    def test_wrong_tuple_size_in_instructions_1(self):
        tm = TuringMachine({0, 1}, {"a", "b", "c"}, [0, 1, 0, 1], [(("a"), ("b", 0, "R")), (("a", 1), ("b", 0, "R"))], "a", "c")
        self.assertFalse(tm.check_input())

    def test_wrong_tuple_size_in_instructions_2(self):
        tm = TuringMachine({0, 1}, {"a", "b", "c"}, [0, 1, 0, 1], [(("a", 1), ("b", 0, "R")), (("a", 1), (0, "R"))], "a", "c")
        self.assertFalse(tm.check_input())

    def test_state_not_in_states_1(self):
        tm = TuringMachine({0, 1}, {"a", "b", "c"}, [0, 1, 0, 1], [(("k", 1), ("b", 0, "R")), (("a", 1), ("b", 0, "R"))], "a", "c")
        self.assertFalse(tm.check_input())

    def test_state_not_in_states_2(self):
        tm = TuringMachine({0, 1}, {"a", "b", "c"}, [0, 1, 0, 1], [(("a", 1), ("b", 0, "R")), (("a", 1), ("k", 0, "R"))], "a", "c")
        self.assertFalse(tm.check_input())

    def test_symbol_not_in_alphabet_1(self):
        tm = TuringMachine({0, 1}, {"a", "b", "c"}, [0, 1, 0, 1], [(("a", 1), ("b", 0, "R")), (("a", 2), ("b", 0, "R"))], "a", "c")
        self.assertFalse(tm.check_input())

    def test_symbol_not_in_alphabet_2(self):
        tm = TuringMachine({0, 1}, {"a", "b", "c"}, [0, 1, 0, 1], [(("a", 1), ("b", "k", "R")), (("a", 1), ("b", 0, "R"))], "a", "c")
        self.assertFalse(tm.check_input())

    def test_wrong_direction_1(self):
        tm = TuringMachine({0, 1}, {"a", "b", "c"}, [0, 1, 0, 1], [(("a", 1), ("b", 0, "Right")), (("a", 1), ("b", 0, "R"))], "a", "c")
        self.assertFalse(tm.check_input())

    def test_wrong_direction_2(self):
        tm = TuringMachine({0, 1}, {"a", "b", "c"}, [0, 1, 0, 1], [(("a", 1), ("b", 0, "R")), (("a", 1), ("b", 0, "abc"))], "a", "c")
        self.assertFalse(tm.check_input())

    def test_wrong_symbol_on_tape(self):
        tm = TuringMachine({0, 1}, {"a", "b", "c"}, [0, 1, 4, 1], [(("a", 1), ("b", 0, "R")), (("a", 1), ("b", 0, "R"))], "a", "c")
        self.assertFalse(tm.check_input())




if __name__ == '__main__':
    unittest.main()
