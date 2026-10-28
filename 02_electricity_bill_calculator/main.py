# Electricity Bill Calculator
# Topics: input/output, type conversion, arithmetic, comparisons, if-elif-else.

units = float(input("Enter electricity units consumed: "))

if units < 0:
    print("Units cannot be negative.")
elif units <= 100:
    bill = units * 1.50
    print(f"Electricity bill: Rs. {bill:.2f}")
elif units <= 200:
    bill = 100 * 1.50 + (units - 100) * 2.50
    print(f"Electricity bill: Rs. {bill:.2f}")
else:
    bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
    print(f"Electricity bill: Rs. {bill:.2f}")
