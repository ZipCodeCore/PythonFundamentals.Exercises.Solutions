import unittest
import exception_practice


class ExceptionPracticeTest(unittest.TestCase):

    def test_single_handler(self):
        with self.assertLogs() as cm:
            exception_practice.single_handler()
            self.assertEqual(type(FileNotFoundError()), type(cm.records[0].msg))

    def test_multi_handler(self):
        with self.assertLogs() as cm:
            pass
