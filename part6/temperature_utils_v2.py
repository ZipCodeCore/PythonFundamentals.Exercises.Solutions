from typing import Iterable, Tuple


def f_to_c(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """
    return round((fahrenheit_temp - 32) * (5/9), 2)


def c_to_f(celsius_temp: float) -> float:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    return round(celsius_temp * (9/5) + 32, 2)


def c_to_k(celsius_temp: float) -> float:
    return round(celsius_temp + 273.15, 2)


def k_to_c(kelvin_temp: float) -> float:
    return round(kelvin_temp - 273.15, 2)


def f_to_k(fahrenheit_temp: float) -> float:
    return round(((fahrenheit_temp - 32) / 1.8) + 273.15, 2)


def k_to_f(kelvin_temp: float) -> float:
    return round(((kelvin_temp - 273.15) * 1.8) + 32, 2)


def temperature_tuple(temperatures: Iterable, in_uom: str, out_uom: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the out_uom parameter.

    :param temperatures: An iterable containing temperatures
    :param in_uom: The unit a measure to use to convert the values in the temperatures parameter
    :param out_uom: The unit of measure to 
    :return: A tuple of tuples
    """
    result = []
    for item in temperatures:
        if in_uom == "f" and out_uom == "c":
            result.append((float(item), float(f_to_c(item))))
        elif in_uom == "f" and out_uom == "k":
            result.append((float(item), float(f_to_k(item))))
        elif in_uom == "c" and out_uom == "f":
            result.append((float(item), float(c_to_f(item))))
        elif in_uom == "c" and out_uom == "k":
            result.append((float(item), float(c_to_k(item))))
        elif in_uom == "k" and out_uom == "c":
            result.append((float(item), float(k_to_c(item))))
        elif in_uom == "k" and out_uom == "f":
            result.append((float(item), float(k_to_f(item))))
        else:
            return tuple()
    return tuple(result)
