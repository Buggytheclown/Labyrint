from tkinter import *  # for Python3 use import tkinter as tk
root = Tk()

def toggle_text():
    """toggle button text between Hi and Goodbye"""
    wid=iv.get()
    wid+=5
    iv.set(wid)
    button.config(width=wid)



iv=IntVar(value=15)

button = Button( text="Hi", command=toggle_text, width=15, bg = 'white')

root.title("Click the Button")

button.pack(padx=100, pady=10)
root.mainloop()
root.mainloop()