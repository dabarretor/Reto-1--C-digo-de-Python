"""This program generates a list of random integers 
and then creates a new list containing only 
the prime numbers from the original list."""

import random # Allows us to generate random numbers.

while True:
    try:
        quantity = int(input("¿How many numbers do you want? "))
        if quantity <= 0:
            print("Please enter a valid integer greater than 0.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer.")

while True:
    try:
        range_numbers = int(input("¿What is the range of the numbers? (from 1 to...): "))
        if range_numbers <= 0:
            print("Please enter a valid integer greater than 0.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer.")

list_numbers = []

def prime_number(num):
    # Discard 0, 1 and negative numbers because they are not prime.
    if num <= 1:
        return False
    # I try divisions with 2, 3, 4...
    for test_diviser in range (2, num):
         # If it leaves a remainder of 0, that number is not prime.
        if num % test_diviser == 0:
            return False
    return True
# Repeat the process the requested number of times.
for i in range(quantity):
    # Generates a random number between 1 and the range specified by the user.
    num = random.randint(1, range_numbers)
    # Generates a random number between 1 and the range specified by the user.
    list_numbers.append(num)
print(f"This is the list of integers: {list_numbers}")

prime_numbers=[]
for num in list_numbers:
    if prime_number(num):
        # Adds the generated number to the list of prime numbers.
        prime_numbers.append(num) 
print(f"This is the list of prime numbers, taking the previous list as reference: {prime_numbers}")
