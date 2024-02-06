
import tkinter as tk
from tkinter import *


win = tk.Tk()
win.title("KPIT")
win.geometry("600x500+25+25")

txt1 = Entry(win, font=("Arial", 14))
txt1.place(x=50, y=75)

txt2 = Entry(win, font=("Arial", 14))
txt2.place(x=50, y=250)

txt3 = Entry(win, font=("Arial", 14))
txt3.place(x= 50, y=  350 )

def sum():
    var1 = int(txt1.get())
    var2 = int(txt2.get())
    var3 = var1 + var2
    txt3.delete(0, 10)
    txt3.insert(INSERT, str(var3))

btn = Button(win, text = "Add", command=sum)
btn.place(x=150, y=200)

win.mainloop()

