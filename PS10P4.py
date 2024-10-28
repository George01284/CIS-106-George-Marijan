def Calc_ticket_prce(miles):
    if miles >= 30:
        return 12
    elif miles >= 20:
        return 10
    elif miles >= 10:
        return 8
    else:
        return 5
def main():
    ttl_price = 0
    run_program = input("Would you like to start the program? (Yes/No): ")
    while run_program.lower() in ["yes", "y", "Y","YeS","yEs","ye", "Ye", "yeah"]:
        last_name = input("Enter your last name: ")
        miles = float(input("Enter the miles from downtown Chicago: "))
        Tkt_prce = Calc_ticket_prce(miles)
        ttl_price += Tkt_prce
        print(f"{last_name}, your train ticket price is: ${Tkt_prce:.2f}")
        run_program = input("Would you like to continue? (Yes/No): ")
    print(f"Total price of all tickets: ${ttl_price:.2f}")
main()