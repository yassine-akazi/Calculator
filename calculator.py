# import necessary modules from tkinter library
from tkinter import*
from tkinter import ttk 

# create a new instance of Tk and set window title
root = Tk()
root.title("calculator")

# prevent window from being resized
root.resizable(0,0)

# define function to handle button clicks
def insert(text):
    if text != "=":  # if not "=" button, add text to En
        En.insert(END , text)
    else:  # if "=" button, evaluate En contents and display result or error
        var = En.get()
        try:
            operation = eval(var)
            En.delete(0, "end")
            En.insert(0, "{}".format(operation))
        except: 
            En.delete(0, "end")
            E.insert(0 , "math error")

# define function to create buttons
def button(text , clmn , rw ):
    # create a new ttk button with specified text and command, and add to grid at specified column and row
    ttk.Button(root , text = text , command = lambda:insert(text)).grid(column = clmn , row = rw , ipady=6 , ipadx=1) 

# create a new Entry widget and add to grid
En = ttk.Entry(root , font="arial 15")
En.grid(column= 0 , row = 0 , columnspan= 5 , ipadx=4 , ipady=8 )

# create buttons for numbers and operators, using button function to add to grid
button("1", 0, 1)
button("2", 1, 1)
button("3", 2, 1)

button("4", 0, 2)
button("5", 1, 2)
button("6", 2, 2)

button("7", 0, 3)
button("8", 1, 3)
button("9", 2, 3)

button("+", 3, 1)
button("/", 3, 2)
button("-", 3, 3)
button("*", 3, 4)

button(".", 1, 4)
button("=", 2, 4)
button("0", 0, 4)

# start main event loop
root.mainloop()
