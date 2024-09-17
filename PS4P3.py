BillAmount= float(input("Enter the Bill Amount for your food: "))
Tip_Percentage= float(input("Enter the tip percentage. your options are 15, 18,and 20%: "))
Tiptotal= BillAmount * (Tip_Percentage / 100)
Totalcost= BillAmount + Tiptotal
if Tip_Percentage > 20: print(f"Tip_Percentage {Tip_Percentage} is not valid")
if Tip_Percentage <=20: print(f" BillAmount is {BillAmount:.2f} Your tip is {Tiptotal:.2f} and your total cost is {Totalcost:.2f}")