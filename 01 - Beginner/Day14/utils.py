import random
import game_data

def get_person():
    """
    Selects a random account from
    game_data.py
    """
    return random.choice(game_data.data)

def format_person(person):
    """
    Takes the account data and returns a 
    printable format
    """
    print(f"\n{person["name"]}")
    print(f"{person["description"]} from {person["country"]}")

def check_answer(user_guess, a_followers, b_followers):
    """
    Checks if user guess is correct (returns True) 
    or not (False)
    """
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
