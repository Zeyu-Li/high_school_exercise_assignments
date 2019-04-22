""" Python Calculator Program

Course: CS 30
Period: 3
Date created: March 12, 2019
Date completed: March 14, 2019
Date last updated: March 26, 2019
By: Andrew Li

This is a program that calculates math operations
"""

# import module math for square roots
from math import floor


class operation:
    """ class that houses operator methods """

    def addition(self, x, y):
        """ addition method """

        return y + x

    def subtraction(self, x, y):
        """ subtraction method """

        return x - y

    def multiplication(self, x, y):
        """ multiplication method """

        return y * x

    def division(self, x, y):
        """ division method """

        # check for denominator is 0
        if y == 0:
            return "Cannot divide by zero"

        return x / y

    def longDivision(self, x, y):
        """ exact division method """

        # check for denominator is 0
        if y == 0:
            return "Cannot divide by zero"
        if y < 0 or x < 0:
            return "Only accepts positive non-zero integer inputs"

        return floor(x / y), x % y

    def squareRoot(self, x):
        """ square root method """

        # negative flag
        negative = False

        if x < 0:
            negative = True

        # x is the absolute value to not to cause errors
        x = abs(x)

        if x == 0 or x == 1:
            if negative:
                return "i"
            else:
                return x

        # the max number that needs to be checked
        max = floor(x**.5)+1

        # init variables
        check = False
        timesIn = 0
        array = []

        # loop through possible factors
        for index in range(2, max):

            # if index equals 0 or 1, skip b/c it has already been checked

            # loop through square numbers to see if it is divisible
            while (x % (index**2) == 0):
                x = int(x/(index**2))
                timesIn = timesIn + 1
                check = True

            if check:
                array.append(index**timesIn)
                timesIn = 0
                check = False

        wholeNumber = multipleList(array)

        # outputs
        if x == 1 and not negative:
            return wholeNumber
        elif x == 1 and negative:
            return str(wholeNumber) + "i"
        elif not negative:
            if wholeNumber == 1:
                return "√" + str(x)
            return str(wholeNumber) + "√" + str(x)
        else:
            return str(wholeNumber) + "i √" + str(x)


def foo():
    """ input functions """

    print("If you wish to quit, type \"q\" or \"quit\" and press enter")

    # grabs first integer input as str with end and start whitespace removed
    firstNumber = str(input("First Integer: ")).strip()

    # test if q or quit have been pressed
    if firstNumber == "q" or firstNumber == "quit":
        return 0

    # test if input is number
    try:
        firstNumber = int(firstNumber)

    # if input is not number, loop through the whole function (continue)
    except:
        print("The input is not a valid integer")
        return 1

    # options for operators
    print("""
    Now summit the operator given the following options:\n
    Enter \"+\" for addition
    Enter \"-\" for addition
    Enter \"*\" for multiplication
    Enter \"/\" for division
    Enter \"rem /\" for division with remainder
    Enter \"sqrt\" for exact square roots
    """)

    # get operator input
    operator = str(input("Operator: ")).strip()

    operatorList = ["+", "-", "*", "/", "rem /", "sqrt"]

    # test if input is an operator
    try:
        test = (operator in operatorList)
        if not test:
            raise Exception("not an operator")

    # else contine through function
    except:
        print("Not a specified operator, please try again\n")
        return 1

    # shortened class call
    op = operation()

    # special case for square root
    if operator == "sqrt":
        print(op.squareRoot(firstNumber))
        return 1

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
    if operator == "+":
        result = op.addition(firstNumber, secondNumber)
    elif operator == "-":
        result = op.subtraction(firstNumber, secondNumber)
    elif operator == "*":
        result = op.multiplication(firstNumber, secondNumber)
    elif operator == "/":
        result = op.division(firstNumber, secondNumber)
        if result == "Cannot divide by zero":
            print("Cannot divide by zero")
            return 1
    elif operator == "rem /":
        result = op.longDivision(firstNumber, secondNumber)
        if result == "Cannot divide by zero":
            print(result)
            return 1
        elif result == "Only accepts positive non-zero integer inputs":
            print(result)
            return 1

    # special case for long division
    if operator == "rem /":
        if result[1] == 0:
            print(str(result[0]))
        else:
            print(str(result[0]) + " & a remainder of " + str(result[1]))
    else:
        print(result)

    print("\nNext operation \n")
    return 1


def multipleList(foo):
    """ multiples lists for answer to square root functions """

    # sourced from:
    # Striver
    # March 13, 2019
    # Python | Multiply all numbers in the list
    # https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/
    result = 1
    for x in foo:
        result = result * x

    return result


def main():
    """ main function call """

    # welcome text

    print("Hello user, and welcome to the calculator app on terminal\n")
    print("To start this program, enter the number(must be an integer)")
    working = True

    # if errors occur, loop through the whole function again
    while working:
        working = foo()

    # end note
    print("\nThanks for using Andrew's Calculator")


# system calls name
if __name__ == "__main__":
    main()
