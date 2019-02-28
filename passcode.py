""" *title

Course: CS 30
Period: 3
Date created: 
Date completed: 
By: Andrew Li
*description

"""

import json
import hashlib

def main():
    
    print('This is Foo Inc.\n Please enter your username')

    foo = input('Username: ')

    with open('pass.json', 'r') as fp:
        try: 
            json.load(foo in fp)
            protect(foo)
        except:
            print('User not found')
        

def protect(foo):

    # Comparies to see if value is in json file
    if (True): 

        bar = input('Password: ')

        # if (bar == )

    else:

        print('Welcome new user!\n')
        bar = input('New password: ')

        zed = input('Retype password: ')

        if (bar == zed):

            #insert some hash function
            someHash = hashlib.sha1( ('$2%' + bar + 's9!').encode('utf-8') ).hexdigest()

            print(someHash)

            with open('pass.json', 'w') as fp:
                json.dump({foo: someHash}, fp)

            print('account created')

        else:

            print('Passwords do not match. Try again.')

if __name__ == "__main__":
    main()
