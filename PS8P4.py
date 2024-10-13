with open("order_data.txt", "w") as file:
    file.write("Item1, 3, 10.00\n")
    file.write("Item2, 5, 20.00\n")
    file.write("Item3, 2, 30.00\n")
    file.write("Item4, 4, 40.00\n")
total_extended_price = 0
order_count = 0
with open("order_data.txt", "r") as file:
    for line in file:
        item, quantity, price = line.strip().split(", ")
        quantity = int(quantity)
        price = float(price)
        extended_price = quantity * price
        total_extended_price += extended_price
        order_count += 1
        print(f"Item: {item}, Quantity: {quantity}, Price: ${price:.2f}, Extended Price: ${extended_price:.2f}")
average_order = total_extended_price / order_count if order_count else 0
print(f"\nTotal extended price: ${total_extended_price:.2f}")
print(f"Number of orders: {order_count}")
print(f"Average order value: ${average_order:.2f}")