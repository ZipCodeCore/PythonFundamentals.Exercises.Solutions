from typing import Dict


modes_dict = {
    1: "User",
    2: "Admin",
}

admin_mode_options = {
    1: "Add language",
    2: "Edit greeting",
}

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {
    1: "English",
    2: "Spanish",
    3: "Portuguese",
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {
    1: 'What is your name?',
    2: '¿Cómo te llamas?',
    3: 'Qual é o seu nome?',
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {
    1: 'Hello',
    2: 'Hola',
    3: 'Olá',
}

##############################
# Control-flow functions
##############################

def print_dict(dict: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    :return: None
    """
    for key, value in dict.items():
        print(f'{key}: {value}')


def int_input() -> int:
    """
    This function prompts the user for a choice.

    :return: An integer representing the language choice made by the user
    """
    result = input()
    return int(result)


def choice_is_valid(dict_in: Dict[int, str], choice_in: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param dict_in: A dictionary
    :param choice_in: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    return dict_in.get(choice_in) is not None


def prompt_options(prompt: str, dict_in: Dict[int, str]) -> int:
    print(prompt)
    print_dict(dict_in)
    choice = int_input()
    while choice_is_valid(dict_in, choice) is False:
        print("Invalid selection. Try again.")
        choice = int_input()
    return choice


##############################
# Admin mode functions
##############################

def add_language(*args):
    print("adding language...")
    print("Enter a language id: ")
    new_lang_id = int_input()
    new_lang_desc = input("What is the name of the new language? ")
    new_lang_prompt = input(f"How do you ask for someone's name in {new_lang_desc}? ")
    new_lang_greeting = input(f"How do you say hello in {new_lang_desc}? ")
    
    lang_dict[new_lang_id] = new_lang_desc
    name_prompt_dict[new_lang_id] = new_lang_prompt
    greetings_dict[new_lang_id] = new_lang_greeting


def edit_greeting():
    print("editing greeting...")
    lang_to_edit = prompt_options("Please choose a language to edit: ", lang_dict)
    new_greeting = input("What should the new greeting be?")
    greetings_dict[lang_to_edit] = new_greeting


##############################
# User mode functions
##############################

def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    return name_prompt_options.get(lang_choice)


def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """
    return input(name_prompt)


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    greeting = f'{greetings_options.get(lang_choice)} {name}'
    print(greeting)


##############################
# Modes functions
##############################

def user_mode():
    print("Entering user mode...")
    chosen_lang = prompt_options("Please choose a language: ", lang_dict)
    selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    chosen_name = name_input(selected_prompt)
    greet(chosen_name, greetings_dict, chosen_lang)


def admin_mode():
    print("Entering admin mode...")
    chosen_action = prompt_options("Please choose an action.", admin_mode_options)

    if(chosen_action == 1):
        add_language()
    elif(chosen_action == 2):
        edit_greeting()


def home():
    chosen_mode = prompt_options("Please choose a mode: ", modes_dict)

    if(chosen_mode == 1):
        user_mode()
    elif (chosen_mode == 2):
        admin_mode()
    else: 
        print("Invalid mode...")

    home()


if __name__ == '__main__':
    home()
