# Task: Prime Number Finder
# Write a Python script to:

# Display all the prime numbers between 1 to 250.
# Store the results in a results.txt file.
# Test the script. Verify that it produced the expected results in the results.txt file.
# Save the script and make a note of its location (absolute path) for future reference.

from pathlib import Path
import subprocess

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
        return True

# primeNumberList = []

# for i in range(1, 250):
#     # Check if the number is prime
#     if isPrime(i) == True:
#         primeNumberList.append(int(i))

# print(primeNumberList)

# Write the results to a file

filename = "primeNumbersResultFile.txt"

with open(filename, "w") as file:
    file.write("Prime numbers between 1 and 250:\n")
    file.write("-------------------------------\n")
    for i in range(1, 250):
        # Check if the number is prime
        if isPrime(i) == True:
            file.write(f"{i}\n")

# Absolute path of the file
filename = Path(filename)
absPath = filename.resolve()
print(f"File store in: {absPath}")

subprocess.run(["cat", filename])