# Shopping Cart and Bill Calculator
# Topics: lists, for loop, input/output, type conversion,
# arithmetic, comparisons, and formatted strings.

items = []
prices = []

for number in range(1, 4):
    name = input("Enter name of item " + str(number) + ": ")
    price = float(input("Enter price of " + name + ": Rs. "))

    if price < 0:
        print("Price cannot be negative.")
        break

    items.append(name)
    prices.append(price)

if len(items) == 3:
    print("\n--- SHOPPING BILL ---")
    for index in range(len(items)):
        print(f"{items[index]}: Rs. {prices[index]:.2f}")

    total = sum(prices)
    print(f"Total: Rs. {total:.2f}")
