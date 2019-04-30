""" Reading External Files

Course: CS 30
Period: 3
Date created: April 30, 2019
Date completed: April 30, 2019
By: Andrew Li

This program reads external files
"""
# import modules


def main():

    with open('learning_python.txt', 'r') as fp:
        text = fp.read().replace('etc', '+ more')
        print(text)
        with open('learning_python.txt', 'w') as f:
            f.writelines(text)

# system calls name
if __name__ == "__main__":
    main()
