
def str_len(input: str) -> str:
    """
    Given a string parameter, this function should return the length of the parameter.
    """
    return len(input)


def first_char(input: str) -> str:
    """
    Given a string parameter, this function should return the first letter of the parameter.
    """
    return input[0]


def last_char(input: str) -> str:
    """
    Given a string parameter, this function should return the last letter of the parameter..
    """
    return input[-1]


def input_has_substring(string: str, substring: str) -> bool:
    """
    This function determines if the substring exists within the string. Returns True or False.
    """
    if string.find(substring) == -1:
        return False
    else: 
        return True


def substring(input: str, start: int, stop: int) -> str:
    """
    Returns the substring of a string.

    Keyword arguments:
    input -- the string in which to generate a substring from
    start -- starting position of the input parameter to start the substring (inclusive)
    stop -- stopping position of the input parameter to stop the substring (exclusive)
    """
    return input[start: stop]


def opposite_case(string: str) -> str:
    """
    Given a string parameter, this function returns the same string back with each letter having the opposite case.
    Example: 
    When input = "Roberto" the function returns "rOBERTO"
    """
    result = ""
    for letter in string:
        if(letter.isupper()):
            result += letter.lower()
        else:
            result += letter.upper()
    return result

