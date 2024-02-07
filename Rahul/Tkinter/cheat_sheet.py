import tkinter as tk

# Create a main window
root = tk.Tk()
root.title("My Tkinter App")

# Label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Button
def button_callback():
    label.config(text="Button Clicked!")

button = tk.Button(root, text="Click me!", command=button_callback)
button.pack()

# Entry (Single Line Text Input)
entry = tk.Entry(root)
entry.pack()

# Text (Multiline Text Input)
text = tk.Text(root, height=4, width=30)
text.pack()

# Checkbutton
check_var = tk.IntVar()
check_button = tk.Checkbutton(root, text="Check me", variable=check_var)
check_button.pack()

# Radiobutton
radio_var = tk.StringVar()
radio_button = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="1")
radio_button.pack()

# Listbox
listbox = tk.Listbox(root)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.pack()

# Scrollbar
scrollbar = tk.Scrollbar(root, orient="vertical", command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Geometry Managers
frame = tk.Frame(root)
frame.pack()

# Events and Bindings
def callback_function():
    entry_text = entry.get()
    text.insert(tk.END, entry_text + "\n")

entry_button = tk.Button(root, text="Add to Text", command=callback_function)
entry_button.pack()

# Start the GUI event loop
root.mainloop()
