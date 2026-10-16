import random

EASY_GUESSES = 10
HARD_GUESSES = 5

def get_random_number():
    return random.randint(1, 100)

def num_guesses(difficulty):
    if difficulty == "easy":
        return EASY_GUESSES
    elif difficulty == "hard":
        return HARD_GUESSES
    else:
        return 0

def check_guess(winning_number, guess):
    if winning_number > guess:
        print("TOO LOW!")
        return False
    elif winning_number < guess:
        print("TOO HIGH!")
        return False
    else:
        print("EXACTLY!")
        return True
