def calc_commissionandtarget(salesAmt):
    if salesAmt > 100000:
        commission = salesAmt * 0.10
    else:
        commission = salesAmt * 0.05
    nextyrstarget = salesAmt * 0.05
    return (commission, nextyrstarget)
def main():
    lastname = input("Enter the salesperson's last name: ")
    salesAmt = float(input("Enter the sales amount: "))
    commission, nextyrstarget = calc_commissionandtarget(salesAmt)
    print(f"Salesperson's Last Name: {lastname}")
    print(f"Commission: ${commission:.2f}")
    print(f"Next Year's Target: ${nextyrstarget:.2f}")
main()