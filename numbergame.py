import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("Can you guess it?")

# Initialize variables
attempts = 0
guessed_correctly = False

# Start the guessing loop
while not guessed_correctly:
    # Input: User's guess
    guess = int(input("Enter your guess: "))
    attempts += 1  # Count the attempt
    
    # Check the guess
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        guessed_correctly = True
