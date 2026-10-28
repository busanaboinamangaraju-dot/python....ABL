# Student Marks Analysis
# Topics: lists, input/output, type conversion, for loop,
# arithmetic, comparisons, max/min, and formatted output.

marks = []
count = int(input("How many subjects? "))

if count <= 0:
    print("Enter a positive number of subjects.")
else:
    valid = True
    for number in range(1, count + 1):
        mark = float(input("Enter mark " + str(number) + " (0-100): "))
        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            valid = False
            break
        marks.append(mark)

    if valid:
        highest = max(marks)
        lowest = min(marks)
        average = sum(marks) / len(marks)
        print(f"Highest mark: {highest:g}")
        print(f"Lowest mark: {lowest:g}")
        print(f"Average mark: {average:.2f}")
