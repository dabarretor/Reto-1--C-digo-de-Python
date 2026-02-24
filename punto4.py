import random

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
        range_numbers1 = int(input("¿What is the range of the numbers? (from ... to...): "))
        break
    except ValueError:
        print("Please enter a valid integer.")

while True:
    try:
        range_numbers = int(input(f"¿What is the range of the numbers? (from {range_numbers1} to...): "))
        if range_numbers < range_numbers1:
            print("The second number must be greater than or equal to the first number.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer.")

list_numbers = []

for i in range(quantity):
    num = random.randint(range_numbers1, range_numbers)
    list_numbers.append(num)

print(f"This is the list of integers: {list_numbers}")

def highest_consecutive_sum(list_numbers):
    sums=[]
    # The variable is declared with a very small value using '-inf' to ensure that any sum found will be larger.
    max_sum = float('-inf') 
    # The list is traversed from the first element to the last.
    for i in range(len(list_numbers) - 1):
        # The consecutive elements are added together.
        sum = list_numbers[i] + list_numbers[i + 1]  
        sums.append(sum)
        # It is checked if it is the largest sum found. 
        if sum > max_sum:
            # And if it's the largest sum found, we update max_sum.  
            max_sum = sum  
    return max_sum, sums

result, list_sums = highest_consecutive_sum(list_numbers)
print(f"This is the list of consecutive sums: {list_sums}")
# It is used to call the function and display the result.
print(f"The largest sum of consecutive elements is: {result}") 
