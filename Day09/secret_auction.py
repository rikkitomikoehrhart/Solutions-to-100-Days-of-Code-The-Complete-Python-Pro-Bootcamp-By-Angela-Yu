import art

print("Welcome to the Secret Auction!")

bids = {}

running = True
while running:
    print(art.logo)
    name = input("What is your name?: ")
    price = float(input("What is your bid?: $"))

    bids[name] = price

    should_continue = input("Are there any other bidders? Type yes or anything else for no: ").lower()

    if should_continue != "yes":
        running = False



def find_highest_bidder(bidding_dictionary):
    winner = max(bidding_dictionary, key=bidding_dictionary.get)
    winning_bid = bidding_dictionary[winner]

    print(f"The winner is {winner}, with a bid of ${winning_bid:.2f}")

find_highest_bidder(bids)
