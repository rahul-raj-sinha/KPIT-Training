
import tkinter as tk
from tkinter import *
from tkinter import messagebox

win = tk.Tk()
win.geometry("600x500+25+25")
win.title("KPIT")

def click():
    messagebox.showinfo("Hello", "Welcome to Tkinter....")

def func(args):
    messagebox.showinfo("Hello", args)

btn1 = Button(win, text = "yellow", command=click, font=("Arial", 18), activeforeground='yellow', activebackground="orange", pady=10)

btn2 = Button(win, text = "green",
            command= lambda: func("Hello World"),
              font=("Comics San MS", 18), activeforeground='blue', activebackground="pink", pady=10)

btn3 = Button(win, text = "red", font=("TimesnewRoman", 18), activeforeground='green', activebackground="white", pady=10)
btn4 = Button(win, text = "blue", font=("Harlow Solid Italic", 18), activeforeground='red', activebackground="purple", pady=10)

btn1.pack(side= LEFT)
btn2.pack(side= RIGHT)
btn3.pack(side= TOP)
btn4.pack(side= BOTTOM)

win.mainloop()
