import tkinter as tk
from tkinter import messagebox
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")
def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task != "":
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to update.")
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x500")
root.config(bg="#F0F8FF")
title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#F0F8FF")
title_label.pack(pady=10)
task_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
task_entry.pack(pady=10)
task_listbox = tk.Listbox(root, width=50, height=10, font=("Helvetica", 12), selectbackground="#ADD8E6")
task_listbox.pack(pady=10)
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)
button_frame = tk.Frame(root, bg="#F0F8FF")
button_frame.pack(pady=20)
add_button = tk.Button(button_frame, text="Add Task", width=15, font=("Helvetica", 12), bg="#87CEEB", command=add_task)
add_button.grid(row=0, column=0, padx=10)
update_button = tk.Button(button_frame, text="Update Task", width=15, font=("Helvetica", 12), bg="#87CEEB", command=update_task)
update_button.grid(row=0, column=1, padx=10)
delete_button = tk.Button(button_frame, text="Delete Task", width=15, font=("Helvetica", 12), bg="#87CEEB", command=delete_task)
delete_button.grid(row=0, column=2, padx=10)
root.mainloop()
