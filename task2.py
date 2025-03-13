import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation selected.")

        messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields
tk.Label(root, text="Enter first number:").grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:").grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

# Create operation choices
operation_var = tk.StringVar(value="Add")
tk.Label(root, text="Select operation:").grid(row=2, column=0)
tk.Radiobutton(root, text="Add", variable=operation_var, value="Add").grid(row=2, column=1)
tk.Radiobutton(root, text="Subtract", variable=operation_var, value="Subtract").grid(row=3, column=1)
tk.Radiobutton(root, text="Multiply", variable=operation_var, value="Multiply").grid(row=4, column=1)
tk.Radiobutton(root, text="Divide", variable=operation_var, value="Divide").grid(row=5, column=1)

# Create a button to perform the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=6, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()