import tkinter as tk
from tkinter import messagebox
contacts = []
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone:
        contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_fields()
        update_contact_list()
    else:
        messagebox.showerror("Error", "Name and phone number are required!")
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
def search_contact():
    search_term = search_entry.get()
    if search_term:
        matching_contacts = [contact for contact in contacts if
                             search_term.lower() in contact["Name"].lower() or search_term in contact["Phone"]]
        if matching_contacts:
            contact_listbox.delete(0, tk.END)
            for contact in matching_contacts:
                contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")
        else:
            messagebox.showinfo("No Match", "No contacts found matching the search criteria.")
    else:
        messagebox.showwarning("Empty Search", "Please enter a search term.")
def delete_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        index = selected_contact[0]
        del contacts[index]
        update_contact_list()
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showwarning("No Selection", "Please select a contact to delete.")
def update_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        index = selected_contact[0]
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        if name and phone:
            contacts[index] = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            update_contact_list()
            messagebox.showinfo("Success", "Contact updated successfully!")
            clear_fields()
        else:
            messagebox.showerror("Error", "Name and phone number are required!")
    else:
        messagebox.showwarning("No Selection", "Please select a contact to update.")
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x550")
add_frame = tk.Frame(root)
add_frame.pack(pady=10)
tk.Label(add_frame, text="Name:", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=3)
name_entry = tk.Entry(add_frame, font=("Helvetica", 12))
name_entry.grid(row=0, column=1, padx=5, pady=3)
tk.Label(add_frame, text="Phone:", font=("Helvetica", 12)).grid(row=1, column=0, padx=5, pady=3)
phone_entry = tk.Entry(add_frame, font=("Helvetica", 12))
phone_entry.grid(row=1, column=1, padx=5, pady=3)
tk.Label(add_frame, text="Email:", font=("Helvetica", 12)).grid(row=2, column=0, padx=5, pady=3)
email_entry = tk.Entry(add_frame, font=("Helvetica", 12))
email_entry.grid(row=2, column=1, padx=5, pady=3)
tk.Label(add_frame, text="Address:", font=("Helvetica", 12)).grid(row=3, column=0, padx=5, pady=3)
address_entry = tk.Entry(add_frame, font=("Helvetica", 12))
address_entry.grid(row=3, column=1, padx=5, pady=3)
add_button = tk.Button(add_frame, text="Add Contact", font=("Helvetica", 12), command=add_contact)
add_button.grid(row=4, columnspan=2, pady=5)
search_frame = tk.Frame(root)
search_frame.pack(pady=10)
search_entry = tk.Entry(search_frame, width=30, font=("Helvetica", 12))
search_entry.grid(row=0, column=0, padx=5)
search_button = tk.Button(search_frame, text="Search", font=("Helvetica", 12), command=search_contact)
search_button.grid(row=0, column=1, padx=5)
list_frame = tk.Frame(root)
list_frame.pack(pady=10)
contact_listbox = tk.Listbox(list_frame, width=50, font=("Helvetica", 12))
contact_listbox.pack(side=tk.LEFT)
scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.config(command=contact_listbox.yview)
contact_listbox.config(yscrollcommand=scrollbar.set)
update_button = tk.Button(root, text="Update Contact", font=("Helvetica", 12), command=update_contact)
update_button.pack(pady=5)
delete_button = tk.Button(root, text="Delete Contact", font=("Helvetica", 12), command=delete_contact)
delete_button.pack(pady=5)
root.mainloop()
