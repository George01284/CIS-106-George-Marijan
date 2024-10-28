def calc_wall_sqr_footage(length, width, height):
    wall_sqr_footage = 2 * height * (length + width)
    return wall_sqr_footage
def calc_gal_needed(sqr_footage):
    gal_needed = sqr_footage / 50
    return gal_needed
def main():
    run_program = input("Would you like to start the program? (Yes/No): ")
    while run_program.lower() in ["yes", "y", "Y","YeS","yEs", "ye", "Ye", "yeah"]:
        length = float(input("Enter the length of the room: "))
        width = float(input("Enter the width of the room: "))
        height = float(input("Enter the height of the room: "))
        wall_sqr_footage = calc_wall_sqr_footage(length, width, height)
        gal_needed = calc_gal_needed(wall_sqr_footage)
        print(f"You will need {gal_needed:.2f} gallons of paint.")
        run_program = input("Would you like to continue? (Yes/No): ")
main()
