last_Names = ["Smith", "Jones", "Johnson", "Kevin", "Ricardo", "William", "Jordan", "Samuel", "Jackson", "Richardson"]
exam_Scores = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
print("Names and Scores in Original Order:")
for i in range(len(last_Names)):
    last_name = last_Names[i]
    exam_score = exam_Scores[i]
    print(f"{last_name}: {exam_score}")
print("\nNames and Scores in Reverse Order:")
for i in range(len(last_Names)):
    last_name = last_Names[len(last_Names) - 1 - i]
    exam_score = exam_Scores[len(exam_Scores) - 1 - i]
    print(f"{last_name}: {exam_score}")
