import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number greater than 0")
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.config(bg="#2C3E50")
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 18, "bold"), bg="#2C3E50", fg="#ECF0F1")
title_label.pack(pady=20)
length_frame = tk.Frame(root, bg="#2C3E50")
length_frame.pack(pady=10)
length_label = tk.Label(length_frame, text="Password Length:", font=("Helvetica", 12), bg="#2C3E50", fg="#ECF0F1")
length_label.pack(side=tk.LEFT, padx=5)
length_entry = tk.Entry(length_frame, width=5, font=("Helvetica", 12), bg="#ECF0F1", fg="#2C3E50")
length_entry.pack(side=tk.LEFT, padx=5)
generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12, "bold"), bg="#3498DB", fg="#ECF0F1", command=generate_password)
generate_button.pack(pady=20, ipadx=10, ipady=5)
password_entry = tk.Entry(root, font=("Helvetica", 12), width=30, bg="#ECF0F1", fg="#2C3E50", bd=0, justify=tk.CENTER)
password_entry.pack(pady=10, ipady=5)
footer_label = tk.Label(root, text="", font=("Helvetica", 10), bg="#2C3E50", fg="#ECF0F1")
footer_label.pack(side=tk.BOTTOM, pady=10)
root.mainloop()
