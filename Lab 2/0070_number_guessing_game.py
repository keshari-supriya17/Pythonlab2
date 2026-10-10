store_secret_no = 30
print("Enter a guess :")
attempts = 0

print("Welcome to the Number Guessing Game")

while True:
    guess = int(input("Guess the number: "))
    attempts = attempts + 1

    if guess < store_secret_no:
        print("Try a larger number.")
    elif guess > store_secret_no:
        print("Try a smaller number.")
    else:
        print("Congratulations! You guessed correctly.")
        print("Number of attempts:", attempts)
        break