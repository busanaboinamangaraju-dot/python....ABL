# Student Records Using Tuples
# Topics: tuples, lists, input/output, type conversion, for loop,
# and formatted strings.

records = []

for number in range(1, 4):
    roll_number = input("Enter roll number for student " + str(number) + ": ")
    name = input("Enter name for student " + str(number) + ": ")
    mark = float(input("Enter mark for " + name + " (0-100): "))

    if mark < 0 or mark > 100:
        print("Marks must be between 0 and 100.")
        break

    student = (roll_number, name, mark)
    records.append(student)

if len(records) == 3:
    print("\n--- STUDENT RECORDS ---")
    for roll_number, name, mark in records:
        print(f"Roll No: {roll_number} | Name: {name} | Mark: {mark:g}")
