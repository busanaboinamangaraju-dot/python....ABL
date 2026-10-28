# Student Grade Calculator
# Topics: input/output, type conversion, lists, for loop, arithmetic,
# comparison operators, if-elif-else, and formatted strings.

marks = []

for subject in range(1, 6):
    mark = float(input("Enter marks for subject " + str(subject) + " (0-100): "))
    if mark < 0 or mark > 100:
        print("Invalid marks. Enter a value from 0 to 100.")
        break
    marks.append(mark)

if len(marks) == 5:
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "E"

    print(f"Total marks: {total:g}/500")
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", grade)
