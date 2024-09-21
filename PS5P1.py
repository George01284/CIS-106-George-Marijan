Quantity = int(input("Enter the quantity of the item: "))
UnitPrice = 3.0 if Quantity >= 1000 else 5.0
ExtendedPrice = Quantity * UnitPrice
Tax = ExtendedPrice * 0.07
Total = ExtendedPrice + Tax
print(f"Quantity: {Quantity}")
print(f"Unit Price: ${UnitPrice:.2f}")
print(f"Extended Price: ${ExtendedPrice:.2f}")
print(f"Tax: ${Tax:.2f}")
print(f"Total: ${Total:.2f}")