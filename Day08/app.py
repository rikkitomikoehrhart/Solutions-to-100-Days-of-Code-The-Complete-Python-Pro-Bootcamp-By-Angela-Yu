import art
import letters
import sys

print(art.logo)

def caesar(text, shift):
    output_text = ""

    for letter in text:
        if letter not in letters.ch:
            output_text += letter
        else:
            shifted_position = letters.ch.index(letter) + shift
            shifted_position %= len(letters.ch)
            output_text += letters.ch[shifted_position]
    print(f"Here is the result: {output_text}")

running = True
while running:
    direction = input("Type 'encode' to encode, 'decode' to decode, or anything else to exit:\n").lower()
    if direction != "encode" and direction != "decode":
        sys.exit()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "decode":
        shift *= -1

    caesar(text, shift)

    restart = input("They 'yes' to continue or anything else to end the program:\n").lower()

    if restart != "yes":
        running = False

print("Thank you! Have a Great Day!")



