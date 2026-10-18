import utils

on = True
money = 0.00

while on:
    order = utils.order()

    match order:
        case 0:
            on = False
        case 1:
            utils.report(money)
        case _:
            if utils.check_resources(order):
                sale = utils.take_payment(order)
                money += sale
                utils.make_coffee(order)                
                utils.print_line()
                print(f"Here is your {order.capitalize()}")
                print("Have a nice day! \n\n\n")

