""" *title

Course: CS 30
Period: 3
Date created: 
Date completed: 
By: Andrew Li
*description

"""

import tkinter as tk

def main():
    win = tk.Tk()

    win.title("Soupcan")

    tk.Label( win, text="soup is love").pack()

    win.mainloop()

if __name__ == "__main__":
    main()
