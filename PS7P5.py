print("Do you wish to run the program?")
UserResponse = input()

while UserResponse.lower() in ["yes", "y"]:
    quantity = float(input("Enter the quantity of items: "))
    price = float(input("Enter the price of your item(s): $"))
    
    ExtPrice = quantity * price

    if ExtPrice > 10000.0:
        DiscountAmt = ExtPrice * 0.25
        Total = ExtPrice - DiscountAmt
        print("You have a 25% discount which is: $" + str(DiscountAmt))
    else:
        DiscountAmt = ExtPrice * 0.1
        Total = ExtPrice - DiscountAmt
        print("You have a 10% discount which is: $" + str(DiscountAmt))
    
    print("Your new total is: $" + str(Total))
    print("Would you like to try another calculation?")
    UserResponse = input()
