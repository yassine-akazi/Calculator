from tkinter import* 
from tkinter import ttk 
root = Tk()
root.title("calculator")
root.resizable(0,0)
def insert(text):
    if text != "=":
        En.insert(END , text)
    else:
        var = En.get()
        try:
            operation = eval(var)
            En.delete(0, "end")
            En.insert(0, "{}".format(operation))
        except: 
            En.delete(0, "end")
            E.insert(0 , "math error")

def button(text , clmn , rw ):
    ttk.Button(root , text = text , command = lambda:insert(text)).grid(column = clmn , row = rw , ipady=6 , ipadx=1) 
    
En = ttk.Entry(root , font="arial 15")
En.grid(column= 0 , row = 0 , columnspan= 5 , ipadx=4 , ipady=8 )


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
button("x", 3, 4)

button(".", 1, 4)
button("=", 2, 4)
button("0", 0, 4)

root.mainloop()