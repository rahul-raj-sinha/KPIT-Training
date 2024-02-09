


import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

win = tk.Tk()
win.title("KPIT")
lbl = Label(win, text="Welcome to tkiter", fg="blue", font=("Harlow Solid Italic", 36))
lbl.place(x=60, y=50)

txtfld = Entry(win, font=("Arial", 22))
txtfld.place(x=85, y=100)

btn = Button(win, text="Exit", font=("Arial", 36),command=quit)
btn.place(x = 100, y = 200)
img = ImageTk.PhotoImage(Image.open("C:\Training\PycharmProjects\KPITBatch02\Day09\Macaw.jpg"))
panel = Label(win, image=img)
panel.place(x = 100, y=100)
win.geometry("600x500+10+20")
win.mainloop()