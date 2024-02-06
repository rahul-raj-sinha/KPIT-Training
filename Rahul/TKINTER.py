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
