#Simple template made using chat gpt
import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook

def save_budget():
    filename = "budget.xlsx"
    wb = Workbook()
    ws = wb.active
    ws.title = "Budget"

    headers = ['Category', 'Amount']
    ws.append(headers)

    for category, amount in budget.items():
        ws.append([category, amount])

    try:
        wb.save(filename)
        messagebox.showinfo("Success", "Budget saved to budget.xlsx")
    except PermissionError:
        messagebox.showerror("Error", "Could not save the budget. Please make sure the file is not open.")

def add_to_budget():
    category = category_entry.get()
    amount = amount_entry.get()
    if category and amount:
        budget[category] = amount
        update_budget_display()
    else:
        messagebox.showerror("Error", "Please enter both category and amount.")

def update_budget_display():
    budget_display.delete(1.0, tk.END)
    for category, amount in budget.items():
        budget_display.insert(tk.END, f"{category}: ${amount}\n")

# Initialize the main application window
app = tk.Tk()
app.title("Budgeting Application")

# Budget data
budget = {}

# Labels and Entries for user input
category_label = tk.Label(app, text="Category:")
category_label.grid(row=0, column=0, padx=10, pady=5)
category_entry = tk.Entry(app)
category_entry.grid(row=0, column=1, padx=10, pady=5)

amount_label = tk.Label(app, text="Amount:")
amount_label.grid(row=1, column=0, padx=10, pady=5)
amount_entry = tk.Entry(app)
amount_entry.grid(row=1, column=1, padx=10, pady=5)

add_button = tk.Button(app, text="Add to Budget", command=add_to_budget)
add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Displaying the budget
budget_display = tk.Text(app, height=10, width=30)
budget_display.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Button to save budget
save_button = tk.Button(app, text="Save Budget", command=save_budget)
save_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Run the application
app.mainloop()
