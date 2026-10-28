# Simple ATM Menu Simulation
# Topics: variables, input/output, type conversion, while loop,
# if-elif-else, arithmetic and comparison operators.

balance = 1000.0
choice = ""

while choice != "4":
    print("\n--- ATM MENU ---")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print(f"Available balance: Rs. {balance:.2f}")
    elif choice == "2":
        amount = float(input("Enter deposit amount: Rs. "))
        if amount > 0:
            balance = balance + amount
            print("Deposit successful.")
        else:
            print("Amount must be positive.")
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: Rs. "))
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance = balance - amount
            print("Withdrawal successful.")
    elif choice == "4":
        print("Thank you for using the ATM simulation.")
    else:
        print("Invalid choice. Select 1, 2, 3, or 4.")
