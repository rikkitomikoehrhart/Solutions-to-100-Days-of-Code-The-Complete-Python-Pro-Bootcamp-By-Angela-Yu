import data

def print_line():
    print("--------------------------------")

def print_menu():
    print_line()
    print("..... What would you like? .....")
    for item in data.MENU:
        dots = "." * (25 - len(item))
        print(f"{item.capitalize()} {dots} ${data.MENU[item]["cost"]:.2f}")
    print_line()

def order():
    print_menu()
    ordering = True
    while ordering:
        drink = input("What drink would you like?: ").lower()
        if drink == "off":
            return 0
        elif drink == "report":
            return 1
        elif drink not in data.MENU:
            print(f"Sorry, {drink} is not available. Please enter one from the menu.")
        else:
            ordering = False
            return drink

def report(money):
    print_line()
    print("------------ REPORT ------------")
    for item in data.resources:
        dots = "." * (25 - len(item))
        print(f"{item.capitalize()} {dots} {data.resources[item]} ml")

    print(f"Money {"." * (20)} ${money:.2f}")
    print_line()
    
def check_resources(drink):
    for ingredient in data.MENU[drink]["ingredients"]:
        if data.MENU[drink]["ingredients"][ingredient] > data.resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def take_payment(drink):
    total = data.MENU[drink]["cost"]

    try:
        for coin in data.coins:
            if total > 0:
                inserted = float(input(f"${total:.2f} remaining. Insert {coin.capitalize()}: "))
                inserted *= data.coins[coin]
                total -= inserted

    except ValueError as e:
        print("Please enter numeric number of coins only. Returning change, try again.")
        take_payment(drink)

    finally:

        if total > 0:
            print(f"Insufficient funds. ${total:.2f} remaining. Coins returned. Please try again. ")
            take_payment(drink)
        else:
            if total < 0:
                print(f"Too much money added. ${(total * -1):.2f} returned.")
        
        return data.MENU[drink]["cost"]
        
def make_coffee(drink):
    for item in data.MENU[drink]["ingredients"]:
        data.resources[item] -= data.MENU[drink]["ingredients"][item]
