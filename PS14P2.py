class Student:
    def __init__(self, first, last, district_code, credits):
        self.first = first
        self.last = last
        self.district_code = district_code.upper()  # Normalize district code to uppercase
        self.credits = credits
        self.email = first + '.' + last + '@school.edu'

    def compute_tuition(self):
        if self.district_code == 'I':
            tuition = self.credits * 250.00
        elif self.district_code == 'O':
            tuition = self.credits * 500.00
        else:
            raise ValueError("Invalid district code. Please use 'I' for in-district or 'O' for out-of-district.")
        return tuition

# Test the class by instantiating an object and adding data
student1 = Student('Jack', 'Smith', 'I', 15)

print(f"Email: {student1.email}")               
print(f"First Name: {student1.first}")               
print(f"Last Name: {student1.last}")                
print(f"Your district code is {student1.district_code} for in-district")       
print(f"Enrolled Credits: {student1.credits}")             
print(f"Tuition Owed: {student1.compute_tuition()}")  

student2 = Student('Robert', 'Jackson', 'O', 12)

print(f"Email: {student2.email}")               
print(f"First Name: {student2.first}")               
print(f"Last Name: {student2.last}")                
print(f"Your district code is {student2.district_code} for out-of-district")       
print(f"Enrolled Credits: {student2.credits}")             
print(f"Tuition Owed: {student2.compute_tuition()}")
