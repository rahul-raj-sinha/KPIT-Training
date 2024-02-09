#1
from tkinter import *
expr = "" 
def add_to_expr(num): 
    global expr 
    expr = expr + str(num) 
    expression.set(expr) 

def evaluate_expr(): 
    try: 
        global expr 
        total = str(eval(expr)) 
        expression.set(total) 
        expr = "" 
    except: 
        expression.set(" error ") 
        expr = "" 

def clear_expr(): 
    global expr 
    expr = "" 
    expression.set("") 

root = Tk() 
root.configure(background="light green") 
root.title("Simple Calculator") 
root.geometry("270x150") 

expression = StringVar() 
expression_field = Entry(root, textvariable=expression) 
expression_field.grid(columnspan=4, ipadx=70)

button1 = Button(root, text=' 1 ', fg='black', bg='red', command=lambda: add_to_expr(1), height=1, width=7) 
button1.grid(row=2, column=0) 

button2 = Button(root, text=' 2 ', fg='black', bg='red', command=lambda: add_to_expr(2), height=1, width=7) 
button2.grid(row=2, column=1) 

button3 = Button(root, text=' 3 ', fg='black', bg='red', command=lambda: add_to_expr(3), height=1, width=7) 
button3.grid(row=2, column=2) 

button4 = Button(root, text=' 4 ', fg='black', bg='red', command=lambda: add_to_expr(4), height=1, width=7) 
button4.grid(row=3, column=0) 

button5 = Button(root, text=' 5 ', fg='black', bg='red', command=lambda: add_to_expr(5), height=1, width=7) 
button5.grid(row=3, column=1) 

button6 = Button(root, text=' 6 ', fg='black', bg='red', command=lambda: add_to_expr(6), height=1, width=7) 
button6.grid(row=3, column=2) 

button7 = Button(root, text=' 7 ', fg='black', bg='red', command=lambda: add_to_expr(7), height=1, width=7) 
button7.grid(row=4, column=0) 

button8 = Button(root, text=' 8 ', fg='black', bg='red', command=lambda: add_to_expr(8), height=1, width=7) 
button8.grid(row=4, column=1) 

button9 = Button(root, text=' 9 ', fg='black', bg='red', command=lambda: add_to_expr(9), height=1, width=7) 
button9.grid(row=4, column=2) 

button0 = Button(root, text=' 0 ', fg='black', bg='red', command=lambda: add_to_expr(0), height=1, width=7) 
button0.grid(row=5, column=0) 

plus = Button(root, text=' + ', fg='black', bg='red', command=lambda: add_to_expr("+"), height=1, width=7) 
plus.grid(row=2, column=3) 

minus = Button(root, text=' - ', fg='black', bg='red', command=lambda: add_to_expr("-"), height=1, width=7) 
minus.grid(row=3, column=3) 

multiply = Button(root, text=' * ', fg='black', bg='red', command=lambda: add_to_expr("*"), height=1, width=7) 
multiply.grid(row=4, column=3) 

divide = Button(root, text=' / ', fg='black', bg='red', command=lambda: add_to_expr("/"), height=1, width=7) 
divide.grid(row=5, column=3) 

equal = Button(root, text=' = ', fg='black', bg='red', command=evaluate_expr, height=1, width=7) 
equal.grid(row=5, column=2) 

clear = Button(root, text='Clear', fg='black', bg='red', command=clear_expr, height=1, width=7) 
clear.grid(row=5, column='1') 

decimal = Button(root, text='.', fg='black', bg='red', command=lambda: add_to_expr('.'), height=1, width=7) 
decimal.grid(row=6, column=0) 

root.mainloop()





#2

import tkinter as tk

def click_button(button_value):
    current = entry_var.get()
    entry_var.set(current + str(button_value))

def clear_entry():
    entry_var.set("")

def calculate_result():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("")

def add():
    click_button('+')

def subtract():
    click_button('-')

def multiply():
    click_button('*')

def divide():
    click_button('/')

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Entry widget to display input and results
entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, font=('Arial', 16), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons 1-9
tk.Button(window, text='1', font=('Arial', 14), padx=15, command=lambda: click_button(1)).grid(row=1, column=0)
tk.Button(window, text='2', font=('Arial', 14), padx=15, command=lambda: click_button(2)).grid(row=1, column=1)
tk.Button(window, text='3', font=('Arial', 14), padx=15, command=lambda: click_button(3)).grid(row=1, column=2)
tk.Button(window, text='4', font=('Arial', 14), padx=15, command=lambda: click_button(4)).grid(row=2, column=0)
tk.Button(window, text='5', font=('Arial', 14), padx=15, command=lambda: click_button(5)).grid(row=2, column=1)
tk.Button(window, text='6', font=('Arial', 14), padx=15, command=lambda: click_button(6)).grid(row=2, column=2)
tk.Button(window, text='7', font=('Arial', 14), padx=15, command=lambda: click_button(7)).grid(row=3, column=0)
tk.Button(window, text='8', font=('Arial', 14), padx=15, command=lambda: click_button(8)).grid(row=3, column=1)
tk.Button(window, text='9', font=('Arial', 14), padx=15, command=lambda: click_button(9)).grid(row=3, column=2)

# Additional buttons
tk.Button(window, text='0', font=('Arial', 14), padx=15, command=lambda: click_button(0)).grid(row=4, column=0)
tk.Button(window, text='C', font=('Arial', 14), padx=15, command=clear_entry()).grid(row=4, column=1)
tk.Button(window, text='=', font=('Arial', 14), padx=15, command=calculate_result()).grid(row=4, column=2)

# Operator buttons
tk.Button(window, text='+', font=('Arial', 14), padx=15, command=add).grid(row=1, column=3)
tk.Button(window, text='-', font=('Arial', 14), padx=15, command=subtract).grid(row=2, column=3)
tk.Button(window, text='*', font=('Arial', 14), padx=15, command=multiply).grid(row=3, column=3)
tk.Button(window, text='/', font=('Arial', 14), padx=15, command=divide).grid(row=4, column=3)

for i in range(10):
    window.bind(str(i), lambda event, num=i: click_button(num))

window.bind("<Escape>", lambda event:clear_entry())
window.bind("<Return>", lambda event:calculate_result())
window.bind("+", lambda event:add())
window.bind("-", lambda event:subtract())
window.bind("*", lambda event:multiply())
window.bind("/", lambda event:divide())

# # Run the main loop
window.mainloop()


