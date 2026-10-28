# Duplicate Element Removal Using Sets
# Topics: strings, split, lists, sets, membership, and for loop.
# This keeps the first occurrence of each number in the output.

values = input("Enter numbers separated by spaces: ").split()
seen = set()
unique_values = []

for value in values:
    if value not in seen:
        seen.add(value)
        unique_values.append(value)

print("Unique numbers:", " ".join(unique_values))
