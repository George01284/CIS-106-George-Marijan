MealCost = float(input("Enter the cost of the meal: "))
Tip1= 0.20
Tip2= 3.00
if MealCost > 25:
    Total1 = MealCost * Tip1 + MealCost
    print("The cost of your Meal is", MealCost)
    print(" Your Tip is", Tip1)
    print("Your Total is", Total1)
if MealCost<= 25:
    Total2 = MealCost + Tip2
    print("The cost of your meal is", MealCost)
    print("Your tip is: $", Tip2)
    print("Your total amount spent is: $", Total2)