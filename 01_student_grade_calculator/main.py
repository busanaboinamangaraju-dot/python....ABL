marks = []

for subject in range(1, 6):
    mark = float(input(f"Enter marks for subject {subject} (0-100): "))
    if mark < 0 or mark > 100:
        print("Invalid marks. Enter a value from 0 to 100.")
        raise SystemExit
    marks.append(mark)

total = sum(marks)
percentage = total / len(marks)

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
print(f"Grade: {grade}")
