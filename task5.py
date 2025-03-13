import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Manager")
        
        # Initialize contact list
        self.contacts = {}
        
        # Create input fields
        tk.Label(master, text="Name:").grid(row=0, column=0)
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1)

        tk.Label(master, text="Phone:").grid(row=1, column=0)
        self.entry_phone = tk.Entry(master)
        self.entry_phone.grid(row=1, column=1)

        tk.Label(master, text="Email:").grid(row=2, column=0)
        self.entry_email = tk.Entry(master)
        self.entry_email.grid(row=2, column=1)

        tk.Label(master, text="Address:").grid(row=3, column=0)
        self.entry_address = tk.Entry(master)
        self.entry_address.grid(row=3, column=1)

        # Create buttons
        tk.Button(master, text="Add Contact", command=self.add_contact).grid(row=4, column=0)
        tk.Button(master, text="View Contacts", command=self.view_contacts).grid(row=4, column=1)
        tk.Button(master, text="Search Contact", command=self.search_contact).grid(row=5, column=0)
        tk.Button(master, text="Update Contact", command=self.update_contact).grid(row=5, column=1)
        tk.Button(master, text="Delete Contact", command=self.delete_contact).grid(row=6, column=0)

        # Listbox to display contacts
        self.listbox = tk.Listbox(master, width=50)
        self.listbox.grid(row=7, column=0, columnspan=2)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Success", f"Contact '{name}' added.")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Name and Phone are required.")

    def view_contacts(self):
        self.listbox.delete(0, tk.END)
        for name, details in self.contacts.items():
            self.listbox.insert(tk.END, f"{name} - {details['phone']}")

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter name or phone number:")
        if search_term:
            found_contacts = [name for name in self.contacts if search_term in name or search_term in self.contacts[name]['phone']]
            self.listbox.delete(0, tk.END)
            for name in found_contacts:
                self.listbox.insert(tk.END, f"{name} - {self.contacts[name]['phone']}")
            if not found_contacts:
                messagebox.showinfo("Search Result", "No contacts found.")

    def update_contact(self):
        selected_contact = self.listbox.curselection()
        if selected_contact:
            name = self.listbox.get(selected_contact).split(" - ")[0]
            phone = self.entry_phone.get()
            email = self.entry_email.get()
            address = self.entry_address.get()

            if name in self.contacts:
                self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
                messagebox.showinfo("Success", f"Contact '{name}' updated.")
                self.clear_entries()
                self.view_contacts()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_contact = self.listbox.curselection()
        if selected_contact:
            name = self.listbox.get(selected_contact).split(" - ")[0]
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact '{name}' deleted.")
            self.view_contacts()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

# Create the main window
root = tk.Tk()
app = ContactManager(root)

# Start the GUI event loop
root.mainloop()