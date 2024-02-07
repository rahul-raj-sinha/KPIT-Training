import pygame
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

root = tk.Tk()
root.title("KPIT")
root.geometry("600x500")
root.mainloop()


root = tk.Tk()
root.geometry("600x600")
img = ImageTk.PhotoImage(Image.open("Decrypt.png"))
panel = tk.Label(root, image=img)
panel.place(x=100, y=100)
root.mainloop()

win = tk.Tk()
win.title("KPIT")
win.geometry("600x500")

pygame.mixer.init()


def play():
    pygame.mixer.music.load("file_example_WAV_1MG.wav")
    pygame.mixer.music.play(loops=0)


lbl = Label(win, text="Music Player", bd=9, relief=GROOVE,
            font=("Comic Sans", 18), bg="white", fg="black")
lbl.pack(side=TOP)

btn = Button(win, text="Play", font=("Hellvetica", 32), command=play)
btn.pack(pady=20)
win.mainloop()









import tkinter as tk
from tkinter import *
from tkinter import messagebox
win = tk.Tk()
win.title("KPIT")
win.geometry("600x500+10+20")

def click(arg):
    messagebox.showinfo("KPIT", "lulululululu................")

def func(arg):
    messagebox.showinfo("KPIT", arg)

btn1 = Button(win, text="Yellow", command="click", font=("Arial", 26), activebackground="yellow",
              activeforeground="orange", pady=10)
btn2 = Button(win, text="green", command=lambda: func("Hello World"), font=("Arial", 26), activebackground="green",
              activeforeground="pink", pady=10)
btn3 = Button(win, text="blue",command="click", font=("Arial", 26), activebackground="purple", activeforeground="red", pady=10)
btn4 = Button(win, text="red",command="click", font=("Arial", 26), activebackground="red", activeforeground="maroon", pady=10)

btn4.pack(side=BOTTOM)
btn1.pack(side=LEFT)
btn2.pack(side=RIGHT)
btn3.pack(side=TOP)
win.mainloop()








import tkinter as tk
from tkinter import *
from tkinter import messagebox
root = tk.Tk()
root.title("KPIT")
root.geometry('600x500+10+20')
txt1 = Entry(root, font=("Ariel", 14))
txt1.place(x=50, y=75)
txt2 = Entry(root, font=("Ariel", 14))
txt2.place(x=50, y=250)
txt3 = Entry(root, font=("Ariel", 14))
txt3.place(x=50, y=350)

def sum():
    var1 = int(txt1.get())
    var2 = int(txt2.get())
    var3 = var1 + var2
    txt3.delete(0, 10)
    txt3.insert(INSERT, str(var3))

btn = Button(root, text="Add", command=sum)
btn.place(x=150, y=200)
menu_bar = tk.Menu(root)
# create a file menu
file_menu = tk.Menu(menu_bar, tearoff=1)
menu_bar.add_cascade(label="FILE", menu=file_menu)
# add new menu items2
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
root.config(menu=menu_bar)
root.mainloop()
 


















import tkinter as tk
from tkinter import *
from tkinter import messagebox
root = tk.Tk()
root.title("KPIT")
root.geometry('600x500+10+20')
v = Scrollbar(root, orient="vertical")
v.pack(side=RIGHT, fill='y')
txt = Text(root, width=150, borderwidth=2, font=("Ariel", 26))
v.config(command=txt.yview)
txt.pack(side=TOP)

def disp():
    messagebox.showinfo("KPIT", txt.get())

bt1 = Button(root, text="click", command=disp)
bt1.pack(pady=10)

root.mainloop()












import tkinter as tk
from tkinter import *
from tkinter import messagebox
win = tk.Tk()
win.title("KPIT")
win.geometry("600x500+10+20")

def click(arg):
    messagebox.showinfo("KPIT", "lulululululu................")

def func(arg):
    messagebox.showinfo("KPIT", arg)

btn1 = Button(win, text="Yellow", command="click", font=("Arial", 26), activebackground="yellow",
              activeforeground="orange", pady=10)
btn2 = Button(win, text="green", command=lambda: func("Hello World"), font=("Arial", 26), activebackground="green",
              activeforeground="pink", pady=10)
btn3 = Button(win, text="blue",command="click", font=("Arial", 26), activebackground="purple", activeforeground="red", pady=10)
btn4 = Button(win, text="red",command="click", font=("Arial", 26), activebackground="red", activeforeground="maroon", pady=10)

btn4.pack(side=BOTTOM)
btn1.pack(side=LEFT)
btn2.pack(side=RIGHT)
btn3.pack(side=TOP)
win.mainloop()
