password = input("Enter a password to check: ")
has_digit = False
has_upper = False
for character in password:
    if character.isdigit():
        has_digit = True
    if character.isupper():
        has_upper = True
if len(password) >= 8 and has_digit and has_upper:
    print("Password meets the basic rules.")
else:
    print("Password needs improvement.")
    print("Use at least 8 characters, one digit, and one uppercase letter.")