def exponentiate(a: int, b: int) -> int:
    """
    This function takes two integers (a and b) and returns the value of int a raised to the power of b.
    """
    return a ** b


square = lambda x: exponentiate(x, 2)
cube = lambda x: exponentiate(x, 3)


def raise_to_fourth_power(x: int) -> int:
    """
    Given an integer, this function will raise it to the 4th power
    """
    return exponentiate(x, 4)


print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))
