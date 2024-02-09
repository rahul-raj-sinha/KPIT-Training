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
