def computediscount(price, discount_rate):
    discountAmt = price * (discount_rate / 100)
    discountedprice = price - discountAmt
    return (discountAmt, discountedprice)
def main():
    qty = int(input("Enter the quantity: "))
    price = float(input("Enter the price per unit: "))
    discountRte = float(input("Enter the discount rate (as a percent): "))
    discountAmt, discountedprice = computediscount(price, discountRte)
    print(f"Quantity: {qty}")
    print(f"Price per unit: ${price:.2f}")
    print(f"Your discount rate is: {discountRte}%")
    print(f"Discount amount: ${discountAmt:.2f}")
main()