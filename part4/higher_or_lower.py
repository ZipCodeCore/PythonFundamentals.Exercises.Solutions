from random import randrange


def generate_random_number():
    return randrange(10)


def ask_for_input():
    guess = input("Give me a number\n")
    return int(guess)


def evaluate(random_number, users_guess):
    result = False

    if users_guess == random_number:
        print("You got it.")
        result = True
    elif users_guess < random_number:
        print("Too low.")
    else:
        print("Too high.")

    return result


def play():
    users_guess = ask_for_input()
    result = evaluate(random_number, users_guess)
    return result


if __name__ == '__main__':
    random_number = generate_random_number()
    finished = False

    while finished is not True:
        finished = play()
