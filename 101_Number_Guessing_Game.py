# 99. Number Guessing Game: Write a Python program that generates a random number between 1 and 100 and lets the user guess the number. Use a while loop, break when the correct number is guessed, and continue to keep prompting the user until they guess correctly.

import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    print("I have generated a number between 1 and 100. Try to guess it!")

    while True:
        try:
            # Take user input
            guess = int(input("Enter your guess: "))

            # Check if the guess is correct
            if guess == target_number:
                print("Congratulations! You've guessed the number correctly.")
                break  # Exit the loop if the guess is correct
            elif guess < target_number:
                print("Too low! Try again.")
                continue  # Prompt the user to guess again
            else:
                print("Too high! Try again.")
                continue  # Prompt the user to guess again

        except ValueError:
            print("Please enter a valid integer.")

# Run the game
number_guessing_game()
