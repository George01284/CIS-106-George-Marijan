LastName= str(input("Enter your lastname: "))
Dependents= float(input("Enter the number of dependents: "))
GrossIncome= float(input("Enter your gross income: "))
AdjGrossIncome= GrossIncome-Dependents*12000
Taxrate = 0.2 if AdjGrossIncome > 50000 else 0.10
IncomeTax= AdjGrossIncome*Taxrate
if IncomeTax < 0:
  IncomeTax= 100
print("Last Name: ", LastName)
print("Gross Income: $", GrossIncome)
print("Number of Dependents: ", Dependents)
print("Adjusted Gross Income: $", AdjGrossIncome)
print("Income Tax: $", IncomeTax)