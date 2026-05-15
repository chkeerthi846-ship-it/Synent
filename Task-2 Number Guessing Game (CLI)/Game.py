import random

# Generate random number
number = random.randint(1, 100)
attempts = 0

print("🎯 Number Guessing Game")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > number:
        print("📉 Too high!")
    elif guess < number:
        print("📈 Too low!")
    else:
        print(f"🎉 Correct! You guessed in {attempts} attempts.")
        break
