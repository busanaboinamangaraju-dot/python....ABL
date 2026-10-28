values = input("Enter numbers separated by spaces: ").split()
unique_values = sorted(set(values), key=int)
print("Unique numbers:", " ".join(unique_values))