def pay_rate(job_code):
    if job_code in ['L', 'l']:
        return 25
    elif job_code in ['A', 'a']:
        return 30
    elif job_code in ['J', 'j']:
        return 50
    else:
        return 0
Total_gross_pay = 0  
while True:
    employee_ln = input("Enter your employee last name: ")
    job_code = input("Enter your job code (Use L, A, J): ")
    hrs_worked = float(input("Enter your total amount of hours worked: "))
    rate = pay_rate(job_code)
    if rate == 0:
        print("Invalid job code entered.")
    else:
        if hrs_worked > 40:
            normal_pay = 40 * rate
            overtime_pay = (hrs_worked - 40) * (rate * 1.5)
            Gross_pay = normal_pay + overtime_pay
        else:
            Gross_pay = hrs_worked * rate
            Total_gross_pay = Total_gross_pay + Gross_pay  
        print(f"Employee last name: {employee_ln}")
        print(f"Your gross pay: ${Gross_pay:.2f}")
        print(f"Total gross pay for all employees: ${Total_gross_pay:.2f}")
    another_employee = input("Would you like to run this program again? (Yes/No): ")
    if another_employee not in ['yes', 'YES', 'Yes', 'Y', 'y']:
        break