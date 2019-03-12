""" Python Calculator Program

Course: CS 30
Period: 3
Date created: March 12, 2019
Date completed: March TODO: date
By: Andrew Li

This is a program that calculates math operation
"""

# import modules


# class operation:
#     def addition(self):

        

#     def subtraction(self):

        

#     def multiplication(self):

        

#     def division(self):

        

#     def longDivision(self):



#     def squareRoot(self):

        

def main():

    print("If you wish to quit, type q or quit and press enter")

    operator = str(input("Integer: ")).strip()

    if (operator == "q" or operator == "quit"):
        return 0

    try:
        firstNumber = int(operator)
        
    except:
        print("The input is not a valid integer")
        return 1

    print("Now summit the operator given the following options")
    print("Enter \"+\" for addition")
    print("Enter \"-\" for addition")
    print("Enter \"*\" for multiplication")
    print("Enter \"/\" for division")
    print("Enter \"long /\" for long division")
    print("Enter \"sqrt\" for long division")

    operator = str(input("Operator: ")).strip()

    operatorList = ["+", "-", "*", "/", "long /", "sqrt"]

    # test statements

    try:
        test = (operator in operatorList) 
        print(test)
    except:
        print("Not a specified operator, please try again")
        return 1

    print("Now input the second number (must be integer) to operate on")

    secondNumber = str(input("Integer: ")).strip()
    try:
        secondNumber = int(operator)
        
    except:
        print("The input is not a valid integer")
        return 1

    # op = operation()

    # switch statements



# system calls name
if __name__ == "__main__":

    print("Hello user, and welcome to the calculator app on terminal\n")
    print("To start this program, enter the number(must be an integer)")

    working = True

    while working:
        working = main()

    print("\nThanks for using Andrew's Calculator")
