""" Python Calculator Program

Course: CS 30
Period: 3
Date created: March 12, 2019
Date completed: March 14, 2019
By: Andrew Li

This is a program that calculates math operations
"""

# import module math for square roots
import math


class operation:
    """ class that houses operator methods """
    def addition(self, x, y):

        """ addition method """

        return (y + x)

    def subtraction(self, x, y):

        """ subtraction method """

        return (x - y)

    def multiplication(self, x, y):

        """ multiplication method """

        return (y * x)

    def division(self, x, y):

        """ division method """

        # check for denominator is 0
        if (y == 0):
            return ("Cannot divide by zero")

        return (x / y)

    def longDivision(self, x, y):

        """ exact division method """

        # check for denominator is 0
        if (y == 0):
            return ("Cannot divide by zero")

        return (math.floor(x / y), x % y)


def main():

    # main call function

    # welcome text

    print("Hello user, and welcome to the calculator app on terminal\n")
    print("To start this program, enter the number(must be an integer)")
    working = True

    # if errors occur, loop
    while working:
        working = foo()

    # end note
    print("\nThanks for using Andrew's Calculator")


def foo():
    """ input functions """
    print("If you wish to quit, type \"q\" or \"quit\" and press enter")

    # grabs first integer input as str with end and start whitespace removed
    firstNumber = str(input("First Integer: ")).strip()

    # test if q or quit have been pressed
    if (firstNumber == "q" or firstNumber == "quit"):
        return 0

    # test if input is number
    try:
        firstNumber = int(firstNumber)

    # if input is not number, loop through the whole function (continue)
    except:
        print("The input is not a valid integer")
        return 1

    # options for operators
    print("Now summit the operator given the following options:")
    print("Enter \"+\" for addition")
    print("Enter \"-\" for addition")
    print("Enter \"*\" for multiplication")
    print("Enter \"/\" for division")
    print("Enter \"rem /\" for division with remainder")

    # get operator input
    operator = str(input("Operator: ")).strip()

    operatorList = ["+", "-", "*", "/", "rem /"]

    # test if input is an operator
    try:
        test = (operator in operatorList)
        if (not test):
            raise Exception("not an operator")

    # else contine through function
    except:
        print("Not a specified operator, please try again\n")
        return 1

    # shortened class call
    op = operation()

    print("Now input the second number (must be integer) to operate on")

    # grab second integer input
    secondNumber = str(input("Second Integer: ")).strip()

    # check if input is an integer
    try:
        secondNumber = int(secondNumber)

    except:
        print("The input is not a valid integer")
        return 1

    print("The answer is: ")

    # switch statements to figure out which operations to do
    if (operator == "+"):
        result = op.addition(firstNumber, secondNumber)
    elif (operator == "-"):
        result = op.subtraction(firstNumber, secondNumber)
    elif (operator == "*"):
        result = op.multiplication(firstNumber, secondNumber)
    elif (operator == "/"):
        result = op.division(firstNumber, secondNumber)
        if (result == "Cannot divide by zero"):
            print("Cannot divide by zero")
            return 1
    elif (operator == "rem /"):
        result = op.longDivision(firstNumber, secondNumber)
        if (result == "Cannot divide by zero"):
            print("Cannot divide by zero")
            return 1

    # special case for long division
    if (operator == "rem /"):
        if (result == "Cannot divide by zero"):
            print(result)
        elif (result[1] == 0):
            print(str(result[0]))
        else:
            print(str(result[0]) + " & a remainder of " + str(result[1]))
    else:
        print(result)

    print("\nNext operation \n")
    return 1


def multipleList(foo):

    """ multiples lists for answer to square root functions """

    result = 1
    for x in foo:
        result = result * x

    return result

# system calls name
if __name__ == "__main__":
    main()
