marks = []
count = int(input("How many subjects? "))
if count <= 0:
    print("Enter a positive number of subjects.")
    raise SystemExit
for i in range(1, count + 1):
    mark = float(input(f"Enter mark {i} (0-100): "))
    if mark < 0 or mark > 100:
        print("Marks must be between 0 and 100.")
        raise SystemExit
    marks.append(mark)
print(f"Highest mark: {max(marks):g}")
print(f"Lowest mark: {min(marks):g}")
print(f"Average mark: {sum(marks) / len(marks):.2f}")