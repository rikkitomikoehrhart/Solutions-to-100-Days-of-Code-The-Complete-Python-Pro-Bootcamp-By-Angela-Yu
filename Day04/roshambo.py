import hands
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:  "))

if (user_choice < 0 or user_choice > 2):
    user_choice = 0

computer_choice = random.randint(0, 2)

print("You chose: ")
print(hands.hands[user_choice])
print("The Computer chose: ")
print(hands.hands[computer_choice])

if (user_choice == (computer_choice - 1)) or (user_choice == 0 and computer_choice == 2):
    print("You win!")
elif (computer_choice == (user_choice - 1)) or (computer_choice == 0 and user_choice == 2):
    print("You lose!")
elif (computer_choice == user_choice):
    print("Its a draw!!")
else:
    print("!!Error!!")