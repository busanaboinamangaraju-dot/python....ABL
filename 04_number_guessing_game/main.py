# Number Guessing Game
# Topics: variables, input/output, type conversion, while loop,
# if-elif-else, comparisons, and incrementing a variable.
# The secret number is fixed to avoid using modules outside the syllabus.

secret_number = 7
attempts = 0
guess = -1

print("Guess the number between 1 and 10.")

while guess != secret_number:
    guess = int(input("Your guess: "))
    attempts = attempts + 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You guessed in {attempts} attempt(s).")
