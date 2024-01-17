# Import Required Library
from tkinter import *
from tkinter import messagebox
import random

# Create Object
root = Tk()

# Set geometry
root.geometry("500x300")

# Set title
root.title("Rock Paper Scissors Game")

# Computer Value
computer_value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissors"
}


# Reset The Game


def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player              ")
    l3.config(text="Computer")



# Disable the Button


def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"


# If player selected rock


def isrock():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result = messagebox.showinfo('Draw','Draw... Rock v Rock')
    elif c_v == "Scissor":
        match_result = messagebox.showinfo('Victory', 'You won! Rock Crushes Scissors!')
    else:
        match_result =  messagebox.showinfo('Computer Wins','The Computer Won! Paper covers Rock.')
    l1.config(text="Rock            ")
    l3.config(text=c_v)
    button_disable()


# If player selected paper


def ispaper():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Paper":
        match_result = messagebox.showinfo('Draw','Draw... Paper v Paper')
    elif c_v == "Scissor":
        match_result =  messagebox.showinfo('Computer Wins','The Computer Won! Scissors Cut Paper!')
    else:
        match_result = messagebox.showinfo('Victory', 'You won! Paper covers rock!')
    l1.config(text="Paper           ")
    l3.config(text=c_v)
    button_disable()


# If player selected scissor


def isscissor():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result =  messagebox.showinfo('Computer Wins','The Computer Won! Rock SMASHES Scissors!')
    elif c_v == "Scissor":
        match_result = messagebox.showinfo('Draw','Draw... Scissor V Scissor')
    else:
        match_result = messagebox.showinfo('Victory','You won! Scissors Cut Paper!')
    l1.config(text="Scissor         ")
    l3.config(text=c_v)
    button_disable()


# Add Labels, Frames and Button
Label(root,
      text="Rock Paper Scissors",
      font="normal 20 bold",
      fg="red").pack(pady=20)

frame = Frame(root)
frame.pack()

l1 = Label(frame,
           text="Player              ",
           font=10)

l2 = Label(frame,
           text="VS             ",
           font="normal 10 bold")

l3 = Label(frame, text="Computer", font=10)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack(pady=15)

frame1 = Frame(root)
frame1.pack(pady=15)



b1 = Button(frame1, text="I Choose Rock!",
            font=10, width=15,
            command=isrock)

b2 = Button(frame1, text="I Choose Paper! ",
            font=10, width=15,
            command=ispaper)

b3 = Button(frame1, text="I Choose Scissors!",
            font=10, width=15,
            command=isscissor)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Button(root, text="Reset Game",
       font=10, fg="red",
       bg="black", command=reset_game).pack(pady=20)

# Execute Tkinter
root.mainloop()
