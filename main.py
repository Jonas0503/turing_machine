import unittest
from tests import TestTuringMachine

test = unittest.TestLoader().loadTestsFromTestCase(TestTuringMachine)
unittest.TextTestRunner().run(test)
