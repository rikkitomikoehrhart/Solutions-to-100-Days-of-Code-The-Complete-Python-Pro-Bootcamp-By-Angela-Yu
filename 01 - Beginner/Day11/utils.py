import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw :/"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack :("
    elif user_score == 0:
        return "Win with a Blackjack!!!"
    elif user_score > 21:
        return "BUST!"
    elif computer_score > 21:
        return "Opponent went over. You win!!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose"
