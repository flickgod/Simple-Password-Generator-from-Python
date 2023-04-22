# For some reason, you need to close it completely to gen a new random password
# and sometimes with gen numbers it will not do any numbers so... idfk

from tkinter import  * # main tkinter import
from tkinter import messagebox # this is good because if you look at "Line 22" its used there and is needed
import tkinter as tk # needed? idk
import random  # Is the randomly generated strings
import string  # i have no fucking clue why this is needed, but it is so /shrug
# above is neccsasary imports for this to work

window = Tk(className="Password Generator")
window.geometry("400x200")
# window is the actual GUI of the whole thing
# className is the litte "text" at the top of the gui
# the window.geometry is the size of the gui

x = "Generated Password"
# this here is basically for the className of sorts,
# because in the way it works is it goes from top to bottom in a way
# so having something there first stops your gen password from being the className

q = (''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k = 8)))
# Above line is the randomly generated string of line *credit https://flexiple.com/python/generate-random-string-python/ *
# Also where it says "k = 8" if you change the 8 to what ever NUMBER it will change the amount
# of chatacters it will gen

def show_msg():
   messagebox.showinfo(x, q)
# This is basically the small GUI box that shows when the button is clicked
# the x and the q are the variables and the order it goes in, so goes x first then q

b1 = Button(
    window,
    text="Generate Password",
    command= show_msg,
    width=15,  # The width of the button
    height=2,  # the height of the button
    bg="pink", # The buttons "main" colour
    fg="white" # the buttons text colour
)
b1.pack()
# This is very important for the end of nay button statment

#-----------------------------------------------------------

# This next piece of code is basically the exact same as before
# but continue reading
i = "Number x Letters Passowrd"
o = (''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.digits, k = 8)))

def showGenNumPas():
   messagebox.showinfo(i, o)

b2 = Button(
    window,
    text="Generate Password with Numbers",
    command= showGenNumPas,
    width=25,
    height=2,
    bg="magenta",
    fg="white"
)
b2.pack(side = BOTTOM)
# The "side = BOTTOM" is basically the placement of the button

window.mainloop()
# the .mainloop is another vital part as it keeps the gui open for as long as you
# need it to, before you manually close it