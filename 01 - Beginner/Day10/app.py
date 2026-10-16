import my_math
import art

print(art.logo)

operations = {
    "+": my_math.add,
    "-": my_math.subtract,
    "*": my_math.multiply,
    "/": my_math.divide
}

def calculator():
    running = True
    first_num = float(input("What is the first number?: "))

    while running:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        second_num = float(input("What is the next number?: "))


        result = operations[operation_symbol](first_num, second_num)

        print(f"{first_num} {operation_symbol} {second_num} = {result}")

        cont = input(f"Type y to continue calculating with {result}, or type 'n' to start over, or anything else to end program: ")

        if cont == 'n':
            calculator()
        elif cont == 'y':
            first_num = result

    
        if cont != 'n' and cont != 'y':
            running = False

calculator()