from random import randrange


def generate_random_number():
    return randrange(10)


def ask_for_input():
    guess = input("Give me a number\n")
    return int(guess)


def evaluate(random_number, users_guess):
    if users_guess == random_number:
        print("You got it.")
    elif users_guess < random_number:
        print("Too low.")
    else:
        print("Too high.")


random_number = generate_random_number()
users_guess = ask_for_input()
evaluate(random_number, users_guess)
print("The random number was: " + str(random_number))
print("Your guess was: " + str(users_guess))

