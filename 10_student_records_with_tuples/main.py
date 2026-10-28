records = []
for number in range(1, 4):
    roll_number = input(f"Enter roll number for student {number}: ")
    name = input(f"Enter name for student {number}: ")
    mark = float(input(f"Enter mark for {name} (0-100): "))
    if mark < 0 or mark > 100:
        print("Marks must be between 0 and 100.")
        raise SystemExit
    records.append((roll_number, name, mark))
print("\n--- STUDENT RECORDS ---")
for roll_number, name, mark in records:
    print(f"Roll No: {roll_number} | Name: {name} | Mark: {mark:g}")