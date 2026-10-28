items = []
prices = []
for number in range(1, 4):
    name = input(f"Enter name of item {number}: ")
    price = float(input(f"Enter price of {name}: Rs. "))
    if price < 0:
        print("Price cannot be negative.")
        raise SystemExit
    items.append(name)
    prices.append(price)
print("\n--- SHOPPING BILL ---")
for index in range(len(items)):
    print(f"{items[index]}: Rs. {prices[index]:.2f}")
print(f"Total: Rs. {sum(prices):.2f}")