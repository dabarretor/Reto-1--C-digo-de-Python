"""This program is useful to do basic operations with two numbers
requested by the user and the user can choose between addition,
subtraction, multiplication and division or go out of the program"""

# This fuction is the list of the operations that the user can choose.
def options(): 
    print("--list of basic operations--")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Split")
    print("5. go out")
    print("-----------------------------")
    try:
        return int(input("Select an option: "))
    # This line prevents the program from crashing
    # if the user enters an invalid value. e.g. "abc", "_", "1.32".
    except ValueError: 
        return 0
   
# This function allows the user to enter any two numbers
# they want and avoids repeating the code in each operation.
def request_numbers(): 
    while True:
        try:
            num1 = float(input("write a number: "))
            break
        # This line prevents the program from crashing if
        # the user enters a non-numeric value. e.g. "abc", "_".
        except ValueError:
            print("Invalid input, please enter a valid number.")

    while True:
        try:
            num2 = float(input("write another number: "))
            break
        except ValueError:
            print("Invalid input, please enter a valid number.")
    return num1, num2

while True:
    # Store the value entered by the user in the option 
    # field for later use in comparisons.
    option = options()

    if option < 1 or option > 5:
        print("Invalid option. Please try again. ")
        continue

    if option == 5:
        print("Thanks for using the program :D")
        break

    num1, num2 = request_numbers()

    match option:
        case 1:
            print(f"the result is: {num1+num2}")
        case 2:
            print(f"the result is: {num1-num2}")
        case 3:
            print(f"the result is: {num1*num2}")
        case 4:
            # Retry if dividing by zero.
            while num2 == 0:
                print("You can not divide by zero")
                num2 = float(input("write another number: "))
            else:
                print(f"the result is: {num1/num2}")
