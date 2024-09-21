NumofBooks= float(input("Enter the number of books you want to order: "))
CostperBook= float(input("Enter the cost per book: "))
TotalCost= NumofBooks * CostperBook
ShippingCharge1=25.00
ShippingCharge2= 0
OrderTotal1= TotalCost + ShippingCharge1
OrderTotal2= TotalCost + ShippingCharge2
if TotalCost<= 50.00:
  TotalCost += ShippingCharge1
  print("Your Shipping Charge is: $", ShippingCharge1)
  print("Your order total is: $", OrderTotal1)
else:
  TotalCost += ShippingCharge2
  print("Your shipping charge is: $", ShippingCharge2)
  print("Your order total is: $", OrderTotal2)