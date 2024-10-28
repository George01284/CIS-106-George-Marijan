def get_forecast_percentage(month):
    if month in ["January", "February", "March"]:
        return 0.10
    elif month in ["April", "May", "June"]:
        return 0.15
    elif month in ["July", "August", "September"]:
        return 0.20
    elif month in ["October", "November", "December"]:
        return 0.25
    else:
        return 0
def Calc_Nxt_Mon_Sales(month, sales):
    forecast_percentage = get_forecast_percentage(month)
    Next_Mon_Sales = sales * (1 + forecast_percentage)
    return Next_Mon_Sales
def main():
    run_program = input("Would you like to start this program? (Yes/No): ")
    while run_program.lower() in ["yes", "y", "Y", "YeS", "yEs", "ye", "Ye", "yeah"]:
        last_name = input("Enter your last name: ")
        month = input("Enter the month: ")
        sales = float(input("Enter the sales amount: "))
        Next_Mon_Sales = Calc_Nxt_Mon_Sales(month, sales)
        print(f"{last_name}, next month's sales forecast for {month} is: {Next_Mon_Sales:.2f}")
        run_program = input("Would you like to continue? (Yes/No): ")
main()