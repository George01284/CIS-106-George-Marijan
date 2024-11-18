player_names = ["Smith", "Jones", "Johnson", "Kevin", "Ricardo", "Williams", "Jordan", "Samuel", "Jackson", "Richardson"]
batting_averages = [0.267, 0.300, 0.245, 0.280, 0.320, 0.275, 0.290, 0.305, 0.295, 0.310]
with open('players.txt', 'w') as file:
    for i in range(len(player_names)):
        file.write(player_names[i] + ',' + str(batting_averages[i]) + '\n')
read_names = []
read_averages = []
with open('players.txt', 'r') as file:
    for line in file:
        comma_index = line.find(',')
        name = line[:comma_index]
        average = line[comma_index + 1:]
        read_names.append(name)
        read_averages.append(float(average))
def display_player_data(names, averages):
    for i in range(len(names)):
        print(names[i] + ": " + str(averages[i]))
print("Player Names and Batting Averages:")
display_player_data(read_names, read_averages)
def search_player(names, averages):
    while True:
        search_name = input("Enter the last name to search (or type 'exit' to quit): ")
        if search_name.lower() == 'exit':
            break
        found = False
        for i in range(len(names)):
            if names[i].lower() == search_name.lower():
                print(f"Player: {names[i]}, Batting Average: {averages[i]}")
                found = True
                break
        if not found:
            print("Error: Name not found. Please try again.")
search_player(read_names, read_averages)
