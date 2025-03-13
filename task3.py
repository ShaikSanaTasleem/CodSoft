import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        # Define the character set
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate a random password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display the generated password
        label_result.config(text=f"Generated Password: {password}")
    except ValueError as e:
        label_result.config(text=str(e))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create input field for password length
tk.Label(root, text="Enter desired password length:").grid(row=0, column=0)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1)

# Create a button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2)

# Label to display the generated password
label_result = tk.Label(root, text="")
label_result.grid(row=2, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()