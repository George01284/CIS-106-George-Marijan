Quantity = float(input(" Enter your quantity widgets"))
Tax = 0.07
if Quantity >= 10000:
     Price = 10 
else: Price = 20
if Quantity < 5000:
     Price = 30
Extended_Price = Quantity * Price
Tax_Amount = Extended_Price * Tax
Total = Extended_Price + Tax_Amount
print("Your extended price is: ", Extended_Price)
print("Your Tax_Amount is: ", Tax_Amount)
print("Your total is: ", Total)   