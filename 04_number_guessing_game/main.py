secret_number = 7
attempts = 0
print("Guess the number between 1 and 10.")
while True:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You guessed in {attempts} attempt(s).")
        break