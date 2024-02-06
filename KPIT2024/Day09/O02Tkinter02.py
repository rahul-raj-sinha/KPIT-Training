
import tkinter as tk
from tkinter import *

win = tk.Tk()
win.title("KPIT")
lbl = Label(win, text="Welcome to TKinter", fg = "red", font=("Arial", 18))
lbl.place(x=60, y=50)
# geometru - width, height, xpos, ypos
win.geometry("300x200+10+20")
win.mainloop()