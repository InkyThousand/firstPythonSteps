## Functions Partition
 
def getListOfNumbersFromUser():
    listOfNumbers = []
    continueToAdding = True
    while continueToAdding:
        shouldContinue = input("Add number to list? Input any number or any symbol to skip: ")
        try:
            listOfNumbers.append(int(shouldContinue))
        except ValueError:
            print("You are skip adding  numbers")
            continueToAdding = False
    return listOfNumbers

# 15. Word Counter

userInput = input(" Give me a sentence to count the number of words in it: ")
print("{} words in your sentence".format(len(userInput.split())))

exit()

print("====================")



# 14. Temperature Converter
def temperatureConverter(temperature, unit):
    unit = unit.lower()
    if unit == "c":
        result = (temperature * 9/5) + 32
        return f"{temperature} degrees Celsius is {result:.2f} degrees Fahrenheit"
    elif unit == "f":
        result = (temperature - 32) * 5/9
        return f"{temperature} degrees Fahrenheit is {result:.2f} degrees Celsius"
    else:
        return "Invalid unit. Please use 'C' or 'F'."

try:
    temperature = float(input("Input temperature: "))
    unit = input("Convert to (C or F): ")
    print(temperatureConverter(temperature, unit))
except ValueError:
    print("Please enter a valid number for temperature.")

print("====================")

# 13. Average Calculator
def avarageCalculator (listOfNumbers):
    if len(listOfNumbers) == 1:
        return print("The list contains only one number: {}".format(listOfNumbers[0]))
    if len(listOfNumbers) >= 2:
        return print("Avarage in your list is - {}".format(sum(listOfNumbers) / len(listOfNumbers)))
    else:
        return print("The list is empty, please add numbers to the list.")


avarageCalculator(getListOfNumbersFromUser())

print("====================")
# 12. Max and Min Finder
def maxAndMinFinder(listOfNumbers):
    if len(listOfNumbers) == 1:
        return print("The list contains only one number: {}".format(listOfNumbers[0]))
    if len(listOfNumbers) >= 2:
        minVal = min(listOfNumbers)
        maxVal = max(listOfNumbers)
        return print("Minimal number is {}, Maximal is - {}".format(minVal, maxVal))
    else:
        return print("The list is empty, please add numbers to the list.")

maxAndMinFinder(getListOfNumbersFromUser())

print("======================")


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
def simpleInterestCalculator(principal, rate, time):
    return (principal * rate * time) / 100

principalAmount = float(input("Please enter the principal amount: "))
interestRate = float(input("Please enter the rate of interest: "))
yearsAmount = float(input("Please enter the time in years: "))
interest = simpleInterestCalculator(principalAmount, interestRate, yearsAmount)
print("The simple interest is: {:.2f}".format(interest))

print("======================")


    
