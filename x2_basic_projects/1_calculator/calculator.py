# A Simple Calculator using Python
import math


# defining the functions for operations:
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    # return a / b # This is not good
    if b == 0:
        return "Error : Division by Zero - not Possible "
    return a / b


def mod(a, b):
    return a % b


print("Calculator Using Python")
stopCalculator = False  # to perform multiple operation
while stopCalculator == False:
    # handling the user input :
    print("\nOperations:")
    print("1. Add (+)")
    print("2. Sub (-)")
    print("3. Mul (*)")
    print("4. Div (/)")
    print("5. Pow (^)")
    print("6. Mod (%)")
    print("7. Stop Calculator")
    operationList = ["1", "2", "3", "4", "5", "6"]
    # taking operation input
    operation = input("Enter Operation Number: (1/2/3/4/5/6/7): ")
    if operation in operationList:
        # taking operands input
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
    # performing the operation
    match operation:
        case "1":
            print("Output: ", add(num1, num2))
        case "2":
            print("Output: ", sub(num1, num2))
        case "3":
            print("Output: ", mul(num1, num2))
        case "4":
            print("Output: ", div(num1, num2))
        case "5":
            print("Output: ", pow(num1, num2))
        case "6":
            print("Output: ", mod(num1, num2))
        case "7":
            print("Calculator closed successfully...")
            stopCalculator = True
        case _:
            print("Please Enter Valid Operation.")
