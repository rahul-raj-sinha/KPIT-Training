

import tkinter as tk
from tkinter import *
from tkinter import messagebox

win = tk.Tk()
win.title("KPIT")
win.geometry("600x500+25+25")


txt = Entry(win, width=50, borderwidth=2, font=("Arial", 22))
txt.pack(side= TOP)

# def disp(st):
#     txt.insert(20, st)

def disp():
    messagebox.showinfo("Hello", txt.get())

btn = Button(win, text="Click", command=disp)
btn.pack(pady=20)

win.mainloop()