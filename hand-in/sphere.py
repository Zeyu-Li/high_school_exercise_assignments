""" Sphere's Volume

Course: CS 30
Period: 3
Date created: 3/04/19
Date completed: 3/04/19
By: Andrew Li
This program will print the volume of a sphere given the length of a side

"""

# import module math
import math


def main():

    print('This program will calculate the volume of a sphere given an int')

    # gets user input
    userInput = input('Number: ')

    try:

        # Calculates volume by calling math module, pow method
        volume = math.pow(int(userInput), 3) * (4/3) * math.pi
        print(f'The volume is {volume}')

    # prints error instead of using raising method
    except:

        print('Sorry, it appears your input is not a interger value')


# system calls name
if __name__ == "__main__":
    main()
