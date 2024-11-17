# Start of PS13P1
def problem_1():
    num_of_items = int(input("Enter the number of items in your list: "))

    item_lists = []

    for i in range(num_of_items):
        item = int(input(f"Enter item {i + 1}: "))
        item_lists.append(item)

    print(f"Your list of items is: {item_lists}")

# End of problem 1
# Start of Problem 2
def problem_2():
    num_of_items = int(input("Enter the number of items in your list: "))

    item_lists = []

    for i in range(num_of_items):
        item = int(input(f"Enter item {i + 1}: "))
        item_lists.append(item)
    item_lists.insert(100, 100)
    print(f"Your updated list of items is: {item_lists}")
# End of problem 2
# Start of Problem 3
def problem_3():
    num_of_items = int(input("Enter the number of items in your list: "))

    item_lists = []

    for i in range(num_of_items):
        item = int(input(f"Enter item {i + 1}: "))
        item_lists.append(item)
    item_lists = [100 if x == 99 else x for x in item_lists]
    print(f"Your updated list of items is: {item_lists}")
#End of problem 3
# Start of Problem 4
def problem_4():
    num_of_items = int(input("Enter the number of items in your list: "))
    item_lists = []

    for i in range(num_of_items):
        item = int(input(f"Enter item {i + 1}: "))
        item_lists.append(item)

    second_list = [500, 600, 700, 800, 900]

    for value in range(500, 1000, 100):
        print(value, end=' ')
    print() 

    item_lists.extend(second_list)

    print(f"Your updated list of items is: {item_lists}")
# End of Problem 4
#Start of Problem 5
def problem_5():
    num_of_items = int(input("Enter the number of items in your list: "))
    item_lists = []

    for i in range(num_of_items):
        item = int(input(f"Enter item {i + 1}: "))
        item_lists.append(item)

    second_list = [500, 600, 700, 800, 900]

    for value in range(500, 1000, 100):
        print(value, end=' ')
    print() 

    item_lists.extend(second_list)

    if 800 in item_lists:
        item_lists.remove(800)

    print(f"Your updated list of items is: {item_lists}")
# End of Problem 5
# Start of problem 6
def problem_6():
    num_of_items = int(input("Enter the number of items in your list: "))
    item_lists = []

    for i in range(num_of_items):
        item = int(input(f"Enter item {i + 1}: "))
        item_lists.append(item)

    second_list = [500, 600, 700, 800, 900]

    for value in range(500, 1000, 100):
        print(value, end=' ')
    print() 

    item_lists.extend(second_list)

    if 800 in item_lists:
        item_lists.remove(800)

    if len(item_lists) >= 3:
        item_lists.pop(2) 

    print(f"Your updated list of items is: {item_lists}")
# End of Problem 6
# Start of Problem 7
def problem_7():
    grades = ["A", "B", "C", "A", "A", "C"]

    print(f"The list of grades is: {grades}")
#End of Problem 7
#Start of Problem 8
def problem_8():
    grades = ["A", "B", "C", "A", "A", "C"]

    print(f"The list of grades is: {grades}")

    count_A = grades.count("A")

    print(f"The number of 'A' grades is: {count_A}")
# End of Problem 8
# Start of Problem 9
def problem_9():
    grades = ["A", "B", "C", "A", "A", "C"]

    print(f"The list of grades is: {grades}")

    count_A = grades.count("A")
    print(f"The number of 'A' grades is: {count_A}")

    index_B = grades.index("B")
    print(f"The index of the first 'B' grade is: {index_B}")
#End of Problem 9
# Start of Problem 10
def problem_10():
    grades = ["A", "B", "C", "A", "A", "C"]

    print(f"The list of grades is: {grades}")

    count_A = grades.count("A")
    print(f"The number of 'A' grades is: {count_A}")

    index_B = grades.index("B")
    print(f"The index of the first 'B' grade is: {index_B}")

    if "F" not in grades:
        print("The grade 'F' is not a part of the list.")
# End of Problem 10
# Start of Problem 11
def problem_11():
    num_of_items = int(input("Enter the number of items in your list: "))
    item_lists = []

    for i in range(num_of_items):
        item = int(input(f"Enter item {i + 1}: "))
        item_lists.append(item)

    second_list = [500, 600, 700, 800, 900]

    for value in range(500, 1000, 100):
        print(value, end=' ')
    print()  

    item_lists.extend(second_list)

    if 800 in item_lists:
        item_lists.remove(800)

    if len(item_lists) >= 3:
        item_lists.pop(2) 

    second_list.clear()

    print(f"The cleared second list is: {second_list}")
# End of Problem 11
# Started of Problem 12
def problem_12():
    num_of_items = int(input("Enter the number of items in your list: "))
    item_lists = []

    for i in range(num_of_items):
        item = int(input(f"Enter item {i + 1}: "))
        item_lists.append(item)

    second_list = [500, 600, 700, 800, 900]

    for value in range(500, 1000, 100):
        print(value, end=' ')
    print()  

    item_lists.extend(second_list)

    if 800 in item_lists:
        item_lists.remove(800)

    if len(item_lists) >= 3:
        item_lists.pop(2)  

    second_list.clear()

    print(f"The cleared second list is: {second_list}")

    del second_list

    try:
        print(f"The second list is: {second_list}")
    except NameError:
        print("The second list does not exist.")
# End of Problem 12
# Start of Problem 13
def problem_13():
    players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

    print(f"The list of players is: {players}")
# End of Problem 13
# Start of Problem 14
def problem_14():
    players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

    players.sort()

    print(f"The sorted list of players is: {players}")
#End of Problem 14
# Start of Problem 15
def problem_15():
    players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

    players.sort()

    print(f"The sorted list of players is: {players}")

    players_2 = players.copy()

    print(f"The copied list of players (players_2) is: {players_2}")
# End of Problem 15
# Start of Problem 16
def problem_16():
    players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

    players.sort()

    print(f"The sorted list of players is: {players}")

    players_2 = players.copy()

    print(f"The copied list of players (players_2) is: {players_2}")

    players_2.reverse()

    print(f"The reversed list of players (players_2) is: {players_2}")
# End of Problem PS13P16
