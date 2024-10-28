def get_assessed_value_per(county):
    if county.lower() == "cook":
        return 0.90
    elif county.lower() == "dupage":
        return 0.80
    elif county.lower() == "mchenry":
        return 0.75
    elif county.lower() == "kane":
        return 0.60
    else:
        return 0.70
def calc_assessed_value(county, market_value):
    assessed_value_percentage = get_assessed_value_per(county)
    assessed_value = market_value * assessed_value_percentage
    return assessed_value
def main():
    ttl_market_value = 0
    ttl_assessed_value = 0
    run_program = input("Would you like to start the program? (Yes/No): ")
    while run_program.lower() in ["yes", "y", "Y","YeS","yEs", "Ye", "ye", "yeah"]:
        county = input("Enter the county: ")
        market_value = float(input("Enter the market value of the home: "))
        assessed_value = calc_assessed_value(county, market_value)
        ttl_market_value += market_value
        ttl_assessed_value += assessed_value
        print(f"The assessed value for the home in {county} is: ${assessed_value:.2f}")
        run_program = input("Would you like to continue? (Yes/No): ")
    print(f"Total market value of all homes: ${ttl_market_value:.2f}")
    print(f"Total assessed value of all homes: ${ttl_assessed_value:.2f}")
main()