Name= str(input("Enter the name of your appliance: "))
ApplianceCost= float(input("Enter the cost of your appliance: "))
Warranty = ApplianceCost * 0.1 if ApplianceCost > 1000 else ApplianceCost * 0.05
Total= ApplianceCost + Warranty
print("Name of Appliance: ", Name)
print("Cost of Appliance: $", ApplianceCost)
print("Cost of Warranty: $", Warranty)
print("Total Cost: $", Total)