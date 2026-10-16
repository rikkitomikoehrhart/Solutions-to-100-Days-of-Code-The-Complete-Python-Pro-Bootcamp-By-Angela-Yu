import art
import utils

score = 0
playing = True
account_b = utils.get_person()

while playing:
    print(art.logo)

    account_a = account_b
    account_b = utils.get_person()
    while account_a == account_b:
        account_b = utils.get_person()

    print("Compare A: ")
    utils.format_person(account_a)
    print(art.vs)
    print("Against B:")
    utils.format_person(account_b)


    guess = input(f"Who has more followers? {account_a["name"]} (a) or {account_b["name"]} (b)? ").lower()

    if guess == "a" or guess == "b":
        result = utils.check_answer(guess, account_a["follower_count"], account_b["follower_count"])
        score += 1
    else:
        playing = False

    if result:
        print(f"You're right! Your current score is: {score}!!\n\n")
    else:
        print(f"Wrong! Your Final Score is: {score}")
        playing = False
