#import module
from tkinter import *

#create root window
root = Tk()

#root window title & dim
root.title("Test Example GUI")
root.geometry('350x200')

#root window label
lbl = Label(root, text = "Hello my name is label")
lbl.grid()

def clicked():
    lbl.configure(text = "seriously")

#funct to display text w/ button is clicked
btn = Button(root, text = "dont click me" ,
             fg = "red", command=clicked)

btn.grid(column=1, row=0)

root.mainloop()