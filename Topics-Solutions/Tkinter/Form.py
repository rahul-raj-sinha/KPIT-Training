import tkinter as tk
from tkinter import messagebox, filedialog

def save_user_data():
    user_name = entry_user_name.get()
    user_age = entry_user_age.get()
    user_email = entry_user_email.get()

    if not user_name or not user_age or not user_email:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "a") as file:
            file.write(f"Name: {user_name}, Age: {user_age}, Email: {user_email}\n")
        messagebox.showinfo("Success", "User data saved successfully.")
    else:
        messagebox.showwarning("Warning", "File saving cancelled.")

def clear_fields():
    entry_user_name.delete(0, tk.END)
    entry_user_age.delete(0, tk.END)
    entry_user_email.delete(0, tk.END)

root = tk.Tk()
root.title("User Data Form")

label_user_name = tk.Label(root, text="User Name:")
label_user_name.grid(row=0, column=0, padx=10, pady=5)
entry_user_name = tk.Entry(root)
entry_user_name.grid(row=0, column=1, padx=10, pady=5)

label_user_age = tk.Label(root, text="User Age:")
label_user_age.grid(row=1, column=0, padx=10, pady=5)
entry_user_age = tk.Entry(root)
entry_user_age.grid(row=1, column=1, padx=10, pady=5)

label_user_email = tk.Label(root, text="User Email:")
label_user_email.grid(row=2, column=0, padx=10, pady=5)
entry_user_email = tk.Entry(root)
entry_user_email.grid(row=2, column=1, padx=10, pady=5)

button_save = tk.Button(root, text="Save", command=save_user_data)
button_save.grid(row=3, column=0, padx=10, pady=5)

button_clear = tk.Button(root, text="Clear", command=clear_fields)
button_clear.grid(row=3, column=1, padx=10, pady=5)

root.mainloop()
