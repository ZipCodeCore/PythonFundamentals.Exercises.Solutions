def language_input():
    print("Please choose a language: ")
    print("1 - English")
    print("2 - Spanish")
    print("3 - Portuguese")
    return int(input())


def name_input(lang_choice):

    prompt = None

    if lang_choice == 2:
        prompt = "¿Cómo te llamas?\n"
    elif lang_choice == 3:
        prompt = "Qual é o seu nome?\n"
    else:
        prompt = "What is your name?\n"

    return input(prompt)


def greet(name, lang_choice):

    greeting = None

    if lang_choice == 2:
        greeting = "Hola " + name
    elif lang_choice == 3:
        greeting = "Olá " + name
    else:
        greeting = "Hello " + name
    
    print(greeting)


lang_choice = language_input()
name = name_input(lang_choice)
greet(name, lang_choice)
