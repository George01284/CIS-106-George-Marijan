Last_Name= str(input("Enter your lastname"))
Salary= float(input("Enter your salary"))
Job_Level= int(input("Enter your job level"))
Bonus_Rate=0.10
if Job_Level >=10: 
    Bonus_Rate= 0.25
elif Job_Level== 5:
    Bonus_Rate= 0.20
elif Job_Level== 6:
    Bonus_Rate=0.20
elif Job_Level== 7:
    Bonus_rate=0.20
elif Job_Level==8:
    Bonus_rate=0.20
elif Job_Level==9:
    Bonus_Rate=0.20
Bonus= Salary * Bonus_Rate
print("Employee last name: ",Last_Name)
print("Employee bonus: ",Bonus)