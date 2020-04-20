def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * factorial(x - 1)


if __name__ == "__main__":
    print(factorial(0))
    print(factorial(1))
    print(factorial(2))
    print(factorial(3))
    print(factorial(4))
    print(factorial(5))
