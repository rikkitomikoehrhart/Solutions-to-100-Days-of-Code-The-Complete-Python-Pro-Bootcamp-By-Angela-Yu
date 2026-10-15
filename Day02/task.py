print("Welcome to the Tip Calculator!")

subtotal_bill = float(input("Enter the total bill: $"))
tip_percentage = int(input("Enter the tip percentage (10, 12, or 15): %"))
people = int(input("Enter the total people who will split the bill: "))

total_bill = (subtotal_bill * (tip_percentage / 100)) + subtotal_bill

total_per_person = total_bill / people

final_amount = round(total_per_person, 2)

print(f"\n\nEach person should pay: ${final_amount:.2f}")