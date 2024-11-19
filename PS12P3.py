last_Names = ["Smith", "Jones", "Johnson", "Kevin", "Ricardo", "William", "Jordan", "Samuel", "Jackson", "Richardson"]
Scores = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
with open('data.txt', 'w') as file:
    for i in range(len(last_Names)):
        file.write(last_Names[i]) + ',' + str(Scores[i]) + '\n')
read_names = []
read_scores = []
with open('data.txt', 'r') as file:
    for line in file:
        name, score = line.strip().split(',')
        read_names.append(name)
        read_scores.append(int(score))
def display_names_and_scores(names, scores):
    for i in range(len(names)):
        print(names[i] + ": " + str(scores[i]))
print("Names and Scores:")
display_names_and_scores(read_names, read_scores)
def find_highest_score(names, scores):
    high_var = 0
    high_index = 0
    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
    return names[high_index], high_var
def find_lowest_score(names, scores):
    low_var = 999
    low_index = 0
    for i in range(len(scores)):
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i
    return names[low_index], low_var
highest_name, highest_score = find_highest_score(read_names, read_scores)
print("\nHighest Score: " + highest_name + " with a score of " + str(highest_score))
lowest_name, lowest_score = find_lowest_score(read_names, read_scores)
print("\nLowest Score: " + lowest_name + " with a score of " + str(lowest_score))
