totalEmployeeCount = 0
totalGrossPay = 0
employeeCount = 0

print("Would you like to start this program?")
userResponse = input()

while userResponse.lower() in ["yes", "y"]:
    employeeCount += 1
    print("Great! Enter your lastname")
    lastName = input()
    print("Enter the total number of hours worked")
    numHrsWorked = float(input())
    print("Enter your pay rate by the hour")
    payRate = float(input())
    
    if numHrsWorked > 40:
        grossPay = 40 * payRate + (numHrsWorked - 40) * payRate * 1.5
    else:
        grossPay = numHrsWorked * payRate
    
    totalGrossPay += grossPay
    avgPay = totalGrossPay / employeeCount
    
    print("LastName: " + lastName)
    print("Your gross pay is: $" + str(grossPay))
    print("Employee Count: " + str(employeeCount))
    print("Would you like to perform another calculation?")
    userResponse = input()

print("The sum of the gross pays is: $" + str(totalGrossPay))
print("The average employee pay is: $" + str(avgPay))
print("Total Employee Count: " + str(employeeCount))
