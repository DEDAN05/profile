#! usr/bin/env python3
# Getting the name of the player.
import random

def number_guessing_game():
    # Ask for user's name
    name = input("Enter your name: ")
    
    # Pick a secret number between 1 and 50
    secret_number = random.randint(1, 50)
    
    attempts = 0
    max_attempts = 5
    won = False
    
    print(f"Hello {name}, I have picked a number between 1 and 50.")
    print(f"You have {max_attempts} attempts to guess it!")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess == secret_number:
            print("Correct! You guessed the number.")
            won = True
            break
        elif guess < secret_number:
            print("The secret number is HIGHER.")
        else:
            print("The secret number is LOWER.")
    
    # Summary
    print("\n--- Game Summary ---")
    print(f"Player Name: {name}")
    if won:
        print("Result: You WON!")
    else:
        print("Result: You LOST!")
        print(f"The secret number was {secret_number}.")
    print(f"Total Attempts: {attempts}")

# Run the game
number_guessing_game()



