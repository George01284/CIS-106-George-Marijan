with open("student_data.txt", "w") as file:
    file.write("Smith, 1, 12\n")
    file.write("Conrad, 2, 15\n")
    file.write("Williams, 1, 9\n")
    file.write("Johnson, 2, 18\n")
def get_cost_per_credit(district_code):
    if district_code == 1:
        return 250.00
    else:
        return 500.00
total_tuition = 0
student_count = 0
with open("student_data.txt", "r") as file:
    for line in file:
        last_name, district_code, credits_taken = line.strip().split(", ")
        district_code = int(district_code)
        credits_taken = int(credits_taken)
        cost_per_credit = get_cost_per_credit(district_code)
        tuition_owed = credits_taken * cost_per_credit
        total_tuition += tuition_owed
        student_count += 1
        print(f"Student: {last_name}, Credits Taken: {credits_taken}, Tuition Owed: ${tuition_owed:.2f}")
average_tuition = total_tuition / student_count if student_count else 0
print(f"\nTotal tuition owed: ${total_tuition:.2f}")
print(f"Number of students: {student_count}")
print(f"Average tuition per student: ${average_tuition:.2f}")