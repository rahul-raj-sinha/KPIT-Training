
import  tkinter as tk
from tkinter import *
from tkinter import messagebox

win = tk.Tk()
win.title("KPIT")
win.geometry("600x500+10+20")

def click():
    messagebox.showinfo("KPIT", "Welcome to Tkinter.......")

def func(arg):
    messagebox.showinfo("KPIT", arg)

btn1 = Button(win, text="Yellow", command=click, font=("Arial", 26), activebackground="yellow", activeforeground="orange", pady=10)

btn2 = Button(win, text="green", command=lambda :func("Hello World"), font=("Arial", 26), activeforeground="blue", activebackground="pink", pady=10)

btn3 = Button(win, text="blue", font=("Arial", 26), activebackground="purple", activeforeground="red", pady=10)

btn4 = Button(win, text="red", font= ("Arial", 26),activeforeground="green",activebackground="white", pady=10 )

btn1.pack(side=LEFT)
btn2.pack(side=RIGHT)
btn3.pack(side =TOP)
btn4.pack(side=BOTTOM)

win.mainloop()