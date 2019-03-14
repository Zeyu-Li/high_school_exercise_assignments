""" Python Calculator Program

Course: CS 30
Period: 3
Date created: March 12, 2019
Date completed: March 13, 2019
By: Andrew Li

This is a program that calculates math operations
"""

# import modules
import math


# operation class
class operation:
    def addition(self, x, y):

        return (y + x)

    def subtraction(self, x, y):

        return (x - y)

    def multiplication(self, x, y):

        return (y * x)

    def division(self, x, y):

        # check for denominator is 0
        if (y == 0):
            return ("Cannot divide by zero")

        return (x / y)

    def longDivision(self, x, y):

        if (y == 0):
            return ("Cannot divide by zero")
        return (math.floor(x / y), x % y)

    def squareRoot(self, x):

        negative = False

        if (x < 0):
            negative = True

        # x is the absolute value to not to cause errors
        x = abs(x)

        if (x == 0 or x == 1):
            if (negative == True):
                return "i"
            else:
                return x

        # init array
        array = []

        # the max number that needs to be checked
        max = math.floor(x**.5)

        # init variables
        check = False
        timesIn = 0

        # loop through possible factors
        for index in range(max):

            if (index == 0 or index == 1):
                continue

            while (x % (index**2) == 0):
                x = int(x/(index**2))
                timesIn = timesIn + 1
                check = True

            if (check):
                array.append(index**timesIn)
                timesIn = 0
                check = False

        wholeNumber = multipleList(array)

        if (x == 1 and negative == False):
            return wholeNumber
        elif (x == 1 and negative == True):
            return (str(wholeNumber) + "i")
        elif (negative == False):
            return (str(wholeNumber) + "√" + str(x))
        else:
            return (str(wholeNumber) + "i * √" + str(x))

        return "error unknown"


# main call function
def main():

    # welcome text

    print("Hello user, and welcome to the calculator app on terminal\n")
    print("To start this program, enter the number(must be an integer)")
    working = True

    # If errors occur, loop
    while working:
        working = foo()

    # end note
    print("\nThanks for using Andrew's Calculator")


# input functions
def foo():

    print("If you wish to quit, type \"q\" or \"quit\" and press enter")

    # grabs first integer input as str with end and start whitespace removed
    operator = str(input("First Integer: ")).strip()

    # test if q or quit have been pressed
    if (operator == "q" or operator == "quit"):
        return 0

    # test if input is number
    try:
        firstNumber = int(operator)

    # if input is not number, loop through the whole function (continue)
    except:
        print("The input is not a valid integer")
        return 1

    # options
    print("Now summit the operator given the following options")
    print("Enter \"+\" for addition")
    print("Enter \"-\" for addition")
    print("Enter \"*\" for multiplication")
    print("Enter \"/\" for division")
    print("Enter \"long /\" for long division")
    print("Enter \"sqrt\" for exact square roots")

    # get operator input
    operator = str(input("Operator: ")).strip()

    operatorList = ["+", "-", "*", "/", "long /", "sqrt"]

    # test if input is an operator
    try:
        test = (operator in operatorList)
        if (test == False):
            raise Exception("not an operator")

    # else contine through function
    except:
        print("Not a specified operator, please try again\n")
        return 1

    # shortened class call
    op = operation()

    # special case for square root
    if (operator == "sqrt"):
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
    elif (operator == "long /"):
        result = op.longDivision(firstNumber, secondNumber)
        if (result == "Cannot divide by zero"):
            print("Cannot divide by zero")
            return 1

    # special case for long division
    if (operator == "long /"):
        if (result == "Cannot divide by zero"):
            print(result)
        else:
            print(str(result[0]) + " & a remainder of " + str(result[1]))
    else:
        print(result)

    print("\nNext operation \n")
    return 1


# multiples lists for answer to square root functions
def multipleList(foo):

    result = 1
    for x in foo: 
         result = result * x  
    return result 

# system calls name
if __name__ == "__main__":
    main()
