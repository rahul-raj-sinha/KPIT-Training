
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox

win = tk.Tk()
win.title("KPIT")
win.geometry("600x500+10+20")

svar = StringVar()
svar.set("one")
data = ("one", "two", "three", "four")

cb = Combobox(win, values=data)
cb.place(x = 60, y =150)

lb = Listbox(win, height=5, selectmode="multiple")
for num in data:
    lb.insert(END, num)
lb.place(x=250, y=150)

V0 = IntVar()
V0.set(1)

r1 = Radiobutton(win, text="Male", variable=V0, value=1)
r2 = Radiobutton(win, text="Female", variable=V0, value=2)
r1.place(x = 100, y = 50)
r2.place(x= 180,  y= 50)

V1 = IntVar()
V2 = IntVar()
c1 = Checkbutton(win, text="Cicket", variable=V1)
c2 = Checkbutton(win, text="Hockey", variable=V2)
c1.place(x = 100, y = 100)
c2.place(x = 180, y = 100)
win.mainloop()
