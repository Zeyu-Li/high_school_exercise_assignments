"""

Stuff

"""
import os


def main():
    for root, dirs, files in os.walk("../"):
        print(root)

if __name__ == "__main__":
    main()
