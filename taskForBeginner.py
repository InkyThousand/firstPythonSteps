### 3. Odd or Even Checker
userReply = input("Write a number between 1 and 100: ")
userReply = int(userReply)
if userReply % 2 == 0:
    print("The number you entered is even.");
else:
    print("The number is odd.")

print("======================")
### 4. FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

print("======================")
### 5. Password Validator
userPassword = input("Please enter a password: ")

checkedPassword = False 
while checkedPassword == False:
    if len(userPassword) < 8 :
        print("Password must be at least 8 characters long.")
        userPassword = input("Please enter a password: ")
    elif userPassword.isalpha():
        print("Password must contain at least one number.")
        userPassword = input("Please enter a password: ")
    elif userPassword.isdigit():
        print("Password must contain at least one letter.")
        userPassword = input("Please enter a password: ")
    else:
        print("Password is valid.")
        checkedPassword = True
    
print("======================")

## 6. Factorial Finder
def facrorialFunction(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * facrorialFunction(number - 1)

userNumber = int(input("Please enter a number: "))
print("The factorial of {} is {}".format(userNumber, facrorialFunction(userNumber)))

print("======================")

## 7. Prime Number Checker
def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
userReply = int(input("Please enter a number to check if it is prime: "))
if isPrime(userReply):
    print("{} is a prime number.".format(userReply))
else:
    print("{} is not a prime number.".format(userReply))

print("======================")
## 8. Palindrome Checker
def isPalindrome(word):
    return word == word[::-1]
userReply = input("Please enter a word to check if it is a palindrome: ")
if isPalindrome(userReply):
    print("{} is a palindrome.".format(userReply))
else:
    print("{} is not a palindrome.".format(userReply))

print("======================")

## 9. Basic Guessing Game
import random

numberToGuess = random.randint(1, 100)

def basicGuessingGame():
    isGuessCorrect = False
    # Loop until the user guesses the number correctly
    while isGuessCorrect != True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < numberToGuess:
            print("Your guess is too low. Try again.")
        elif guess > numberToGuess:
            print("Your guess is too high. Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            isGuessCorrect = True
    print("Thank you for playing! Goodbye!")

basicGuessingGame()
("======================")

## 10. Countdown Timer

import time
# This function takes a number of seconds and counts down to zero, printing each second.
def countdownTimer(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

userReply = int(input("Please enter a number of seconds to count down: "))
countdownTimer(userReply)

print("======================")

## 11. Simple Interest Calculator