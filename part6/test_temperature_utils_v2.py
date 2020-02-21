import unittest
import temperature_utils_v2


class TemperatureUtilsTest(unittest.TestCase):

    def test_f_to_c(self):
        test_cases = [
            (32, 0),
            (68, 20),
            (100, 37.78),
            (104, 40)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.f_to_c(temp_in))

    def test_c_to_f(self):
        test_cases = [
            (-17.7778, 0),
            (0, 32),
            (100, 212)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.c_to_f(temp_in))

    def test_c_to_k(self):
        test_cases = [
            (-17.7778, 255.37),
            (0, 273.15),
            (20, 293.15)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.c_to_k(temp_in))

    def test_k_to_c(self):
        test_cases = [
            (255.37, -17.78),
            (273.15, 0),
            (293.15, 20)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.k_to_c(temp_in))

    def test_f_to_k(self):
        test_cases = [
            (0, 255.37),
            (20, 266.48),
            (32, 273.15)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.f_to_k(temp_in))

    def test_k_to_f(self):
        test_cases = [
            (0, -459.67),
            (400, 260.33),
            (505.20, 449.69)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.k_to_f(temp_in))

    def test_temperature_tuple(self):
        temps_input = (32, 68, 100, 104)
        expected = ((32, 0.0), (68, 20.0), (100, 37.78), (104, 40.0))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "f", "c")
        self.assertEqual(expected, actual)

    def test2_temperature_tuple(self):
        temps_input = (-17.7778, 0, 100)
        expected = ((-17.7778, 0.0), (0, 32.0), (100, 212.0))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "c", "f")
        self.assertEqual(expected, actual)

    def test3_temperature_tuple(self):
        temps_input = (1, 2, 3)
        self.assertEqual(tuple(), temperature_utils_v2.temperature_tuple(temps_input, "a", "b"))
