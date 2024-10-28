def get_discount(make, model, electricV_code):
    if electricV_code.upper() == "Y":
        return 0.30
    elif make == "Honda" and model == "Accord":
        return 0.10
    elif make == "Toyota" and model == "Rav4":
        return 0.15
    else:
        return 0.05
def calc_out_door_price(msrp, make, model, electricV_code):
    discount_prce = get_discount(make, model, electricV_code)
    discounted_prce = msrp * (1 - discount_prce)
    sales_tax = discounted_prce * 0.07
    final_price = discounted_prce + sales_tax
    return final_price
def main():
    ttl_msrp = 0
    ttl_final_prce = 0
    run_program = input("Would you like to start the program? (Yes/No): ")
    while run_program.lower() in ["yes", "y", "Y","YeS","yEs", "ye", "Ye", "yeah"]:
        make = input("Enter the make of the vehicle: ")
        model = input("Enter the model of the vehicle: ")
        electricV_code = input("Is it an electric vehicle? (Y/N): ")
        msrp = float(input("Enter the MSRP of the vehicle: "))
        ttl_msrp += msrp
        final_price = calc_out_door_price(msrp, make, model, electricV_code)
        ttl_final_prce += final_price
        print(f"The out-the-door price for the {make} {model} is: ${final_price:.2f}")
        run_program = input("Would you like to continue? (Yes/No): ")
    print(f"Total MSRP of all vehicles: ${ttl_msrp:.2f}")
    print(f"Total sales price of all vehicles: ${ttl_final_prce:.2f}")
main()