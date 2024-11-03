def calc_scores(exam1, exam2, exam3):
    totalpoints = exam1 + exam2 + exam3
    avgscore = totalpoints / 3
    return (totalpoints, avgscore)
def main():
    lastname = input("Enter the student's last name: ")
    exam1 = float(input("Enter the first exam score: "))
    exam2 = float(input("Enter the second exam score: "))
    exam3 = float(input("Enter the third exam score: "))
    total_points, avgscore = calc_scores(exam1, exam2, exam3)
    print(f"Student's Last Name: {lastname}")
    print(f"Total Points: {total_points}")
    print(f"Average Exam Score: {avgscore:.2f}")
main()