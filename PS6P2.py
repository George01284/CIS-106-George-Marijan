Part_Number = int(input("Enter your two digit part number: 10, 20, 30, etc."))  
Quantity = float(input("Enter the quantity of parts that you have"))
Unit_Cost= 5.00
if Part_Number == 10:
   Unit_Cost= 1.00
elif Part_Number == 55:
   Unit_Cost= 1.00
if Part_Number == 99: 
   Unit_Cost= 2.00
if Part_Number == 70: 
   Unit_Cost= 3.00
elif Part_Number == 80: 
   Unit_Cost= 3.00
Total_Cost = Unit_Cost * Quantity
CostPerUnit = Unit_Cost
print("Your part number is: ", Part_Number)
print("Your cost per unit is: ", CostPerUnit)
print("Your total is: ", Total_Cost)