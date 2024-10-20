NumOfPlyrs = 0 
while True:
    PlayerLN = input("Enter your last name: ")
    NumOfHits = int(input("Enter the number of hits you've made: "))
    NumOfBats = int(input("Enter the number of bats you've made: "))
    BattingAVG = NumOfHits / NumOfBats
    NumOfPlyrs = NumOfPlyrs + 1 
    print(f"Last name: {PlayerLN}")
    print(f"Your batting avg: {BattingAVG:.3f}") 
    print(f"Total number of players entered so far: {NumOfPlyrs}") 
    another_player = input("Do you want to enter another player? (yes/no): ")
    if another_player not in ['yes', 'YES', 'Yes', 'Y', 'y']:
        break