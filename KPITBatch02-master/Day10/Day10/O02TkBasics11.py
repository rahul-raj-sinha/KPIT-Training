
import tkinter as tk
from tkinter import *
from tkinter import messagebox

win  = tk.Tk()
win .title("KPIT")
win.geometry("600x500+10+20")

txt = Entry(win, width=150, borderwidth=2, font=("Arial", 26))
txt.pack(side=TOP)

def disp():
    messagebox.showinfo("KPIT", txt.get())

btn1 = Button(win, text="click", command=disp)
btn1.pack(pady=10)

win.mainloop()
