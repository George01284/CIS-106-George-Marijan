with open("employee_data.txt", "w") as file:
    file.write("Stevenson, 50000\n")
    file.write("Smith, 120000\n")
    file.write("Johnson, 75000\n")
    file.write("Conrad, 40000\n")
def get_bonus_rate(salary):
    if salary >= 100000:
        return 0.20
    elif salary == 50000:
        return 0.15
    else:
        return 0.10
total_bonuses = 0
with open("employee_data.txt", "r") as file:
    for line in file:
        lastName, salary = line.strip().split(", ")
        salary = float(salary)
        bonus_rate = get_bonus_rate(salary)
        bonus = salary * bonus_rate
        total_bonuses += bonus
        print(f"Employee: {lastName}, Salary: ${salary:.2f}, Bonus: ${bonus:.2f}")
print(f"\nTotal bonuses paid out: ${total_bonuses:.2f}")