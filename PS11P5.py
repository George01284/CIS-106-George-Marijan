total = 0
tax = 0
def calc_totalandtax(qty, unitprice):
    global total, tax
    total = qty * unitprice
    tax = total * 0.07
    return (total, tax)
def main():
    quantity = int(input("Enter the quantity of the item: "))
    unitprice = float(input("Enter the unit price of the item: "))
    calc_totalandtax(quantity, unitprice)
    print(f"Total: ${total:.2f}")
    print(f"Tax: ${tax:.2f}")
main()