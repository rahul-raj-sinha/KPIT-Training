

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


win = tk.Tk()
win.title("KPIT")
lbl = Label(win, text="Welcome to TKinter", fg = "red", font=("Arial", 18))
lbl.place(x=60, y=50)
txtfld = Entry(win)
txtfld.place(x=85, y=80)
btn = Button(win, text="Exit", command=quit)
btn.place(x=200, y=150)
img = ImageTk.PhotoImage(Image.open("C:\Training\PycharmProjects\KPIT2024\Day09\cat.png"))
panel = Label(win, image=img)
panel.place(x = 100, y = 100)

# geometru - width, height, xpos, ypos
win.geometry("300x200+10+20")
win.mainloop()