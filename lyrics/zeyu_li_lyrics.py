""" Lyrics Extracter -0.1

Course: CS 30
Period: 3
Date created: 
Date completed: 
By: Andrew Li
Extracting song lyrics from string and out outputting as a text file
"""

def main():

    with open('lyrics.txt', 'r') as fp:
        print(fp.readlines())
        with open('output.txt', 'w') as f:
            

# system calls name
if __name__ == "__main__":
    main()
