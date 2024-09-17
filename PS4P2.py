Purchase_Price_Of_Stock = float(input("Enter the purchase price of stock: "))
CurrentStockPrice = float(input("Enter the current price of stock: "))
QuantityOfStock = float(input("Enter the quantity of stock: "))
IncreaseInValue = (CurrentStockPrice - Purchase_Price_Of_Stock) * QuantityOfStock
DecreaseInValue = (Purchase_Price_Of_Stock - CurrentStockPrice) * QuantityOfStock
if (CurrentStockPrice > Purchase_Price_Of_Stock):print(f"Congratulations you have made a profit of {IncreaseInValue}")
if (CurrentStockPrice < Purchase_Price_Of_Stock):print(f"Unfortunately you have lost {DecreaseInValue}")