# Author: Adrian Schauer

def calculate(first_number, second_number, operator):
    "This function calculates the result of the given numbers and operator."
    # Check if the numbers are valid
    if first_number.isnumeric() == False or second_number.isnumeric() == False:
        return "Invalid number!"

    # Make sure the numbers are integers
    first_number = int(first_number)
    second_number = int(second_number)

    # Check if the operator is valid.
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        return first_number / second_number
    else:
        return "Invalid operator"
