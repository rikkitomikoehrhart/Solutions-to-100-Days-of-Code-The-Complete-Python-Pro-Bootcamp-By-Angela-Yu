import random
import art
import words

print(art.logo)
print("Welcome to Hangman!")

lives = 6

word = random.choice(words.word_list)
display = ""
correct_letters = []
remaining_letters = words.letters

for letter in word:
    display += "_"

print(display)

playing = True
while playing:
    guess = input("Guess a letter: ")
    placeholder = ""

    if guess in correct_letters or guess not in remaining_letters:
        print(f"You've already guessed: {guess}")
    else:
        if guess in remaining_letters:
            remaining_letters.remove(guess)
        if guess not in word:
            lives -= 1
            if lives == 0:
                playing = False
                print(f"Word was: {word}. You LOSE!")

    for letter in word:
        if letter == guess:
            placeholder += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            placeholder += letter
        else:
            placeholder += "_"
            

    print(art.stages[lives])
    print(remaining_letters)
    print(placeholder)
            
    if "_" not in placeholder:
        playing = False
        print("You WIN!")