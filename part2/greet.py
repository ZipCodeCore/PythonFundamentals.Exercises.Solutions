def greet(name: str) -> None:
    """ 
    This function receives a name parameter and utilizes it to print a greeting. 
    """
    print("Hello " + name)


def name_input() -> str:
    """
    This function prompts the user for their name and returns the value provided by the user.
    """
    return input("What is your name?\n")


name = name_input()
greet(name)
