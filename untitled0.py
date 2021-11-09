# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 15:57:11 2020

@author: Kazım Yıldız PC
"""
import tkinter
from tkinter import messagebox

#callback function
def do_something():
    #the following line of code show messagebox
    messagebox.showinfo('Response', 'You have clicked the button')

def main():
    # Create a root window
    root = tkinter.Tk()
    # create a button widget
    button = tkinter.Button(root, text="Click Me", command = do_something)
    button.pack()
    # Call the event loop
    root.mainloop()

# Call the function main
main()

