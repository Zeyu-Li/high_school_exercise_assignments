""" 
Passcode program, by Andrew Li 
Version 3.0 Working
This program will be a simple user-password program
"""

# all modules needed for secure databases
import bleach                       # cleans inputs
import json                         # writes to json | Might switch to SQL
from argon2 import PasswordHasher   # hashes passwords
import os                           # reads from system files

# logins to account
def login(user, foo):

    # input passcode
    passcode = bleach.clean(input('Password: '))

    # checks passcode

    try:
        data = json.loads()

    # if fails, try again
    except:

        print('Password does not match the username, try again')
        return 1

# creates user
def createUser(user, foo):

    newPasscode = bleach.clean(input('New password: '))

    if (len(newPasscode) < 1): # temp change
        print('Length of password is too short. \nThe passwork has to be at least 8 characters long')
        return 1

    retypedPasscode = bleach.clean(input('Retype password: '))

    if (newPasscode == retypedPasscode):

        #insert some hash and salt function with argon2

        hashedPassword = PasswordHasher().hash(retypedPasscode)

        # retrieves data from json and appends

        with open('passwords.json') as fp:
            data = json.load(fp)

        # dumps password into json file
        with open('passwords.json', 'w') as fp:

            data[str(user)] = hashedPassword
            
            json.dump(data, fp)

        print('Account created')
        return 0

    else:

        print('Passwords do not match. Try again.')
        return 1

# gets username
def username():

    lengthCondition = True

    # input and clean username
    while lengthCondition:
        name = bleach.clean(input('Username: '))

        if (len(name) >= 5):
            lengthCondition = False
        else:
            print('Username must be at least 5 characters long\n')

    return [checkUsername(name), name]

###### File checks #######

# checks username
def checkUsername(username):

    # does json file exist
    isFile()

    # does user exist
    return checkUser(username)

# check if username exists
def checkUser(username):

    with open('passwords.json', 'r') as fp:
        try: 
            json.load(username in fp)
            return True
        except:
            return False

# checks if file exists
def isFile():

    # creates json if none exists
    if (os.path.isfile('passwords.json') == False):

        # inits json file
        with open('passwords.json', 'w') as fp:
            json.dumps('')

# main calls entire system
def main():

    # print('This is The Passcode Program \n Please enter your username')

    with open('passwords.json', 'r') as fp:
    
        try: 
            thing = json.load("sadder" in fp)
            print('is in thing')
            print(thing)

        except:
            print('is not in it')
            print(json.load("sadder" in fp))

    # namedUser = username()

    # # redo this

    # if (namedUser[0] == False):

    #     print('Welcome new user!\n')

    #     foo = True

    #     while foo:
    #         foo = createUser(namedUser[1], foo)

    # else: 

    #     foo = True

    #     while foo:
    #         foo = login(namedUser[1], foo)

    print("Done operations!")


# system calls name which triggers main
if __name__ == "__main__":
    main()
