def pay_rate(CreditHrs, DistrictCode):
    if DistrictCode in ['I', 'i']:
        return CreditHrs * 250
    elif DistrictCode in ['O', 'o']:
        return CreditHrs * 550
    else:
        return 0
TotalTuitionOwed = 0 
while True:
    Student_ln = input("Enter your student last name: ")
    CreditHrs = int(input("Enter the amount of school credit hours taken: "))
    DistrictCode = input("Enter your district code (Type I for in and O for out): ")
    print("Invalid district code entered.")
    TuitionOwed = pay_rate(CreditHrs, DistrictCode)
    TotalTuitionOwed = TotalTuitionOwed + TuitionOwed
    print(f"Student last name: {Student_ln}")
    print(f"Your total tuition owed is: ${TuitionOwed:.2f}")
    print(f"Total tuition owed for all students so far: ${TotalTuitionOwed:.2f}")
    another_student = input("Do you want to enter another student? (Yes/No): ")
    if another_student not in ['yes', 'YES', 'Yes', 'Y', 'y']:
        break