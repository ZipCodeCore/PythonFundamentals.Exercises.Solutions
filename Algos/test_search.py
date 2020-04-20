import unittest
import search
import logging

logging.basicConfig(level=logging.INFO)


class SearchTest(unittest.TestCase):

    def test_binary_search(self):

        first_list = [x for x in range(1, 11)]
        second_list = [x for x in range(1, 101)]

        tests = [
            (first_list, 5, 4),
            (first_list, 10, 9),
            (first_list, 11, None),
            (second_list, 100, 99),
            (second_list, 33, 32)
        ]

        for list_in, item, expected in tests:
            with self.subTest(""):
                actual = search.binary_search(list_in, item)
                self.assertEqual(expected, actual)
