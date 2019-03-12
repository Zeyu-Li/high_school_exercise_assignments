""" Times Table

Course: CS 30
Period: 3
Date created: February 8, 2019
Date completed: February 11, 2019
By: Andrew Li
Prints times table from the 0*0 to 12*12

"""


def main():

    # if i is 0, the print statement in loop will break because it is not
    # possible to step by 0, thus there is a differed case to print an
    # array of 13 zeros
    print([0]*13)

    # looping through the numbers 0 - 12
    for i in range(1, 13):

        # prints the multiplication table starting from 0 to the last number,
        # stepping by desired number to get multipies
        print(list(range(0, 13*i, i)))

# system calls name, thus will call main()
if __name__ == "__main__":
    main()
