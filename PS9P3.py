def compute_mpg(miles_traveled, gallons_used):
    if gallons_used == 0:
        return "Error: Gallons used cannot be entered as zero."
    else:
        return miles_traveled / gallons_used
Num_Of_Trips = 0 
while True:
    City_Destination = input("Enter your city destination: ")
    Miles_Traveled = float(input("Enter the number of miles traveled: "))
    Gallons_Used = float(input("Enter the amount of gallons used for the trip: "))
    MPG = compute_mpg(Miles_Traveled, Gallons_Used)
    if isinstance(MPG, str): 
        print(MPG)
    else:
        Num_Of_Trips = Num_Of_Trips + 1
        print(f"Your city destination is: {City_Destination}")
        print(f"Your miles traveled: {Miles_Traveled}")
        print(f"Your mpg is: {MPG:.2f}")
        print(f"Number of trip destinations entered into the system: {Num_Of_Trips}")
        another_trip = input("Do you want to enter another trip? (yes/no): ")
    if another_trip not in ['yes', 'YES', 'Yes', 'Y', 'y']:
        break