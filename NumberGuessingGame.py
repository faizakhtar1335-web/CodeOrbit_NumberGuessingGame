# Number Guessing Game in Python

import random

def play_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("\nI'm thinking of a number between 1 and 100.")

    while True:
        try:
            # Take user input
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check guess
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! The number was {number_to_guess}.")
                print(f"You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Error: Please enter a valid number.")

def main():
    print("=== Welcome to the Number Guessing Game ===")
    while True:
        play_game()
        # Ask if user wants to play again
        choice = input("\nDo you want to play again? (yes/no): ").lower()
        if choice != "yes":
            print("Thanks for playing! Goodbye 👋")
            break

# Run the game
if __name__ == "__main__":
    main()
