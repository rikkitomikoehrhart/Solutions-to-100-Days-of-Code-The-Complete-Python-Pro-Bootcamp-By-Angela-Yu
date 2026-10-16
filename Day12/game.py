import art
import utils

playing = True

while playing:
    guesses = 0
    winning_number = utils.get_random_number()

    print(art.logo)
    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100.\n\n")
    print(f"Psst... its {winning_number}...")

    guesses = utils.num_guesses(input("Choose a difficulty. Type 'easy' for 10 guesses, 'hard` for 5 or anything else to quit: ").lower())
    if guesses == 0:
        playing = False

    guess = 0

    while guesses != 0 and guess != winning_number:
        guess = int(input("Make a guess: "))
        result = utils.check_guess(winning_number, guess)
        guesses -= 1

        if result:
            playing = False
        elif not result and guesses > 0:
            print(f"You have {guesses} {"guess" if guesses == 1 else "guesses"} left.\n")
        elif not result and guesses == 0:
            playing = False
            print("\nGAME OVER")

