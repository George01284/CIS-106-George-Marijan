print("Ready to start?")
UserResponse = input()
while UserResponse.lower() in ["yes", "y"]:
    print("Great!")
    print("Let us start by entering your lastname")
    LastName = input("What is your lastname?: ")
    Examscoreone = float(input("Enter your first exam score: "))
    Examscoretwo = float(input("Enter your second exam score: "))
    AvgExamScore = (Examscoreone + Examscoretwo) / 2
    print("Lastname: " + LastName)
    print("Average score for both exams: " + str(AvgExamScore))
    print("Would you like to perform another calculation?")
    UserResponse = input()