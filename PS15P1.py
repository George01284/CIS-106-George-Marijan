class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def bonus(self, rate):
        b = float(rate) * float(self.pay)
        return b

class Manager(Employee):
    def long_term_bonus(self):
        return 0.40 * self.pay

empl1 = Employee('Frank', 'Alvino', 60000.00)
empl2 = Employee('John', 'Doe', 55000.00)

mgr1 = Manager('Jane', 'Doe', 80000.00)
mgr2 = Manager('Bob', 'Johnson', 95000.00)

print(f"Employee 1: {empl1.first} {empl1.last}")
print(f"Email: {empl1.email}")
print(f"Salary: {empl1.pay}")
print(f"Bonus (10%): {empl1.bonus(0.10)}")
print(f"Bonus (20%): {empl1.bonus(0.20)}")
print()

print(f"Employee 2: {empl2.first} {empl2.last}")
print(f"Email: {empl2.email}")
print(f"Salary: {empl2.pay}")
print(f"Bonus (10%): {empl2.bonus(0.10)}")
print(f"Bonus (20%): {empl2.bonus(0.20)}")
print()

print(f"Manager 1: {mgr1.first} {mgr1.last}")
print(f"Email: {mgr1.email}")
print(f"Salary: {mgr1.pay}")
print(f"Long-term Bonus (40%): {mgr1.long_term_bonus()}")
print()

print(f"Manager 2: {mgr2.first} {mgr2.last}")
print(f"Email: {mgr2.email}")
print(f"Salary: {mgr2.pay}")
print(f"Long-term Bonus (40%): {mgr2.long_term_bonus()}")
