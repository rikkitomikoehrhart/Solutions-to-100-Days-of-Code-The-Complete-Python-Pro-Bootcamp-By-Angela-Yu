import random
import characters

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = ""

for ch in range(0, nr_letters):
    password += random.choice(characters.letters)

for ch in range(0, nr_symbols):
    password += random.choice(characters.symbols)

for ch in range(0, nr_numbers):
    password += random.choice(characters.numbers)

shuffled_password = "".join(random.sample(password, len(password)))

print(shuffled_password)