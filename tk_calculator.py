from tkinter import *


def add():
    a1 = e1.get()
    a2 = e2.get()
    if a1 =='' or a2 == '':
        err.set("Error: No Input")
    else:
        try:
            x = int(a1)
            y = int(a2)
            z = x+y
            res.set(str(z))
        except ValueError:
            err.set("Error: Invalid Input")
        return

def sub():
    s1 = e1.get()
    s2 = e2.get()
    if s1 == '' or s2 == '':
        err.set("Error: No Input")
    else:
        try:
            x = int(s1)
            y = int(s2)
            z = x - y
            res.set(str(z))
        except ValueError:
            err.set("Error: Invalid Input")
        return
def mul():
    m1 = e1.get()
    m2 = e2.get()
    if m1 == '' or m2 == '':
        err.set("Error: No Input")
    else:
        try:
            x = int(m1)
            y = int(m2)
            z = x * y
            res.set(str(z))
        except ValueError:
            err.set("Error: Invalid Input")
        return
def div():
    d1 = e1.get()
    d2 = e2.get()
    if d1 == '' or d2 == '':
        err.set("Error: No Input")
    else:
        try:
            x = int(d1)
            y = int(d2)
            z = x / y
            res.set(str(z))
        except ValueError:
            err.set("Error: Invalid Input")
        return

window = Tk()

err = StringVar()
res = StringVar()

l1 = Label(window, text = "Entry Input", font = 'Times 15')
e1 = Entry(window, font ='Times 15')
e2 = Entry(window, font ='Times 15')
b1 = Button(window, text = '+', font = 'Times 15', command = add, height = 1, width = 2)
b2 = Button(window, text = '-', font = 'Times 15', command = sub, height = 1, width = 2)
b3 = Button(window, text = '*', font = 'Times 15', command = mul, height = 1, width = 2)
b4 = Button(window, text = '/', font = 'Times 15', command = div, height = 1, width = 2)
e3 = Entry(window, font ='Times 15', textvariable = res)
l2 = Label(window, textvariable = err, font = 'Times 15', fg = 'red')

l1.grid(row = 0, column = 0)
e1.grid(row = 1, column = 0)
e2.grid(row = 2, column = 0)
b1.grid(row = 0, column = 1)
b2.grid(row = 1, column = 1)
b3.grid(row = 2, column = 1)
b4.grid(row = 3, column = 1)
e3.grid(row = 3, column = 0)
l2.grid(row = 4, column = 0)

window.mainloop()

