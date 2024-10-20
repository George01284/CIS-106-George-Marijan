import os
TotalExtPrice = 0
if os.path.exists("TotalExtPrice.txt"):
    with open("TotalExtPrice.txt", "r") as file:
        TotalExtPrice = float(file.read())
def total(quantity, price):
    total_amount = quantity * price
    if total_amount > 10000:
        discount = total_amount * 0.10
        total_amount = total_amount - discount
    return total_amount
while True:
    quantity = float(input("Enter the quantity of your item: "))
    price = float(input("Enter the price of your item: "))
    total_amount = total(quantity, price)
    TotalExtPrice = TotalExtPrice + total_amount
    print(f"Your quantity is: {quantity}")
    print(f"Your price is: ${price:.2f}")
    print(f"Your total is: ${total_amount:.2f}")
    print(f"Total extended price so far: ${TotalExtPrice:.2f}")
    another_item = input("Do you want to enter another item? (yes/no): ")
    if another_item not in ['yes', 'YES', 'Yes', 'Y', 'y']:
        break
with open("TotalExtPrice.txt", "w") as file:
    file.write(str(TotalExtPrice))
