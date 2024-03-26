import unittest
from test.tests import TestTuringMachine

test = unittest.TestLoader().loadTestsFromTestCase(TestTuringMachine)
unittest.TextTestRunner().run(test)
