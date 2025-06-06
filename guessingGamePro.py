    # Guessing Game Pro - A simple number guessing game
# 
# This game allows players to:
# - Guess a random number between 1-10
# - Get up to 3 attempts to guess correctly
# - Optionally receive "higher/lower" tips
# - Play multiple rounds
#
# Game Rules:
# 1. The game randomly generates a secret number between 1-10
# 2. Player gets 3 attempts to guess the correct number
# 3. After each guess, the game will:
#    - Indicate if guess is correct
#    - Tell if player ran out of attempts
#    - Optionally provide tips if number is higher/lower
# 4. Input validation ensures:
#    - Only valid numbers between 1-10 are accepted
#    - Non-numeric input is handled gracefully
#
# Functions:
# wannaPlay(tips=False): Main game logic
#   - tips: Boolean to enable/disable higher/lower hints
#   - Returns: None
#   - Handles the core game mechanics and user interaction
#
# Main game loop:
# - Asks if player wants tips enabled
# - Runs a game round
# - Offers to play again
# - Exits when player chooses to stop

import random

def wannaPlay(tips=False):

    guess = None
    secret_number = random.randint(1, 10)
    print(secret_number)
    numberMaxAttempts = 3

    while guess != secret_number:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempt += 1

            if guess < 1 or guess > 10:
                print("Number must be between 1 and 10.")
                continue
            if guess == secret_number:
                print(f"You guessed it in {attempt} tries!")
                return
            elif attempt == numberMaxAttempts:
                print(f"You lost! Correct number: {secret_number}!")
                return
            else:
                print("Try again!")
            if tips:
                if guess > secret_number:
                    print("Secret number is lower")
                else:
                    print("Secret number is bigger")
        except ValueError:
                print("Please enter a valid number.")

while True:
    if input("Do you want to play with tips? (yes/no): ").strip().lower() == "yes":
        wannaPlay(True)
    else:
        wannaPlay(False)
    if input("Play again? (yes/no): ").strip().lower() != "yes":
        print("Thanks for playing!")
        break