print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

import random
number_to_guess = random.randint(1, 10)

isGuessCorrect = False

# Loop until the user guesses the number correctly
while isGuessCorrect != True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number_to_guess:
        print("Your guess is too low. Try again.")
    elif guess > number_to_guess:
        print("Your guess is too high. Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        isGuessCorrect = True
print("Thank you for playing! Goodbye!")

