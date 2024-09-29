Principle_Amount= float(input("Enter the principle amount of your CD"))
Maturity_Year= float(input("Enter the number of years before your CD matures. Your options are 5 or 10 years. All other principle amounts and years will be calculated with a 2% interest rate"))
Interest_Rate= 0.02
if Principle_Amount > 100000 and Maturity_Year== 5: 
    Interest_Rate= 0.06
if Principle_Amount <=100000 and Maturity_Year== 10: 
    Interest_Rate= 0.05
elif Principle_Amount >= 50000 and Maturity_Year==10:
    Interest_Rate= 0.05
if Principle_Amount <=100000 and Maturity_Year==5: 
    Interest_Rate= 0.04
elif Principle_Amount >= 50000 and Maturity_Year==5:
    Interest_Rate= 0.04
Interest_Amount= Principle_Amount * Interest_Rate
Total= Principle_Amount + Interest_Rate
print("Your principle is: ", Principle_Amount)
print("Your principle earned for the first year is: ", Total)
print("Your first year interest rate is: ", Interest_Rate)
print("Your first year interest amount is: ", Interest_Amount)