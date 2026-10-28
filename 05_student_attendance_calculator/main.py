# Student Attendance Calculator
# Topics: input/output, type conversion, arithmetic, logical operators,
# comparisons, and if-else.

held = int(input("Enter total classes held: "))
attended = int(input("Enter classes attended: "))

if held <= 0 or attended < 0 or attended > held:
    print("Invalid attendance data.")
else:
    percentage = attended / held * 100
    print(f"Attendance: {percentage:.2f}%")

    if percentage >= 75:
        print("Eligible based on 75% rule.")
    else:
        print("Below 75% attendance.")
