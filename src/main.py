import calculator

def Main():
    print("Welcome to the calculator!")
    print("Please enter the first number:")
    first_number = input()
    print("Please enter the second number:")
    second_number = input()
    print("Please enter the operator:")
    operator = input()
    print("The result is:")
    print(calculator.calculate(first_number, second_number, operator))

if __name__ == '__main__':
    Main()
