principalAmount = input("Please enter your principal amount (e.g., 10,000.00): ")
principalAmount = float(principalAmount.replace(",", ""))
interestRate = float(input("Enter your interest rate (as a decimal): "))
beginningBalance = principalAmount
Year = 0
MaxYear = 5
for i in range(MaxYear):
    Year += 1
    AnnualInterest = beginningBalance * interestRate
    EndingBalance = beginningBalance + AnnualInterest
    beginningBalance = EndingBalance
    print(f"Number of years: {Year}")
    print(f"Annual Interest: {AnnualInterest:.2f}")
    print(f"Beginning Balance: {beginningBalance:.2f}")
    print(f"Ending Balance: {EndingBalance:.2f}")
print(f"\nThe total number of years passed is: {Year}")
print(f"Your starting balance was: {principalAmount:.2f}")
print(f"Your final balance after {MaxYear} years is: {EndingBalance:.2f}")
