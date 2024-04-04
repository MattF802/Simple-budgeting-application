#Simple template made using chat gpt
import tkinter as tk
from tkinter import messagebox, simpledialog
from openpyxl import load_workbook, Workbook

# Function to load budget data from Excel file
def load_budget():
    filename = "budget.xlsx"
    try:
        wb = load_workbook(filename)
        ws = wb.active
        budget.clear()
        for row in ws.iter_rows(min_row=2, values_only=True):
            if row[0] and row[1]:
                budget[row[0].lower()] = row[1]
        update_budget_display()
        messagebox.showinfo("Success", "Budget loaded from budget.xlsx")
    except FileNotFoundError:
        messagebox.showerror("Error", "Budget file not found.")

# Function to save budget data to Excel file
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
    category = category_entry.get().lower()
    amount_str = amount_entry.get()
    try:
        amount = float(amount_str)  # Convert amount to float
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")
        return
    
    if category and amount:
        budget[category] = amount
        update_budget_display()
        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter both category and amount.")

def delete_category():
    category = simpledialog.askstring("Delete Category", "Enter category to delete:")
    if category:
        category = category.lower()
        if category in budget:
            del budget[category]
            update_budget_display()
        else:
            messagebox.showerror("Error", f"Category '{category}' not found.")

def update_category():
    old_category = simpledialog.askstring("Update Category", "Enter category to update:")
    if old_category:
        old_category = old_category.lower()
        if old_category in budget:
            new_amount = simpledialog.askfloat("Update Category", "Enter new amount:")
            if new_amount is not None:
                budget[old_category] = new_amount
                update_budget_display()
        else:
            messagebox.showerror("Error", f"Category '{old_category}' not found.")

def update_budget_display():
    budget_display.delete(1.0, tk.END)
    for category, amount in budget.items():
        budget_display.insert(tk.END, f"{category}: ${amount}\n")

def calculate_remaining():
    total_expenses = sum(budget.values())
    salary = float(salary_entry.get())  # Get the salary input
    remaining = salary - total_expenses
    remaining_label.config(text=f"Remaining budget: ${remaining}")

# Initialize the main application window
app = tk.Tk()
app.title("Budgeting Application")

# Load budget data from Excel file
load_budget()

# Labels and Entries for user input
salary_label = tk.Label(app, text="Enter your monthly salary:")
salary_label.grid(row=0, column=0, padx=10, pady=5)
salary_entry = tk.Entry(app)
salary_entry.grid(row=0, column=1, padx=10, pady=5)

category_label = tk.Label(app, text="Category:")
category_label.grid(row=1, column=0, padx=10, pady=5)
category_entry = tk.Entry(app)
category_entry.grid(row=1, column=1, padx=10, pady=5)

amount_label = tk.Label(app, text="Amount:")
amount_label.grid(row=2, column=0, padx=10, pady=5)
amount_entry = tk.Entry(app)
amount_entry.grid(row=2, column=1, padx=10, pady=5)

add_button = tk.Button(app, text="Add to Budget", command=add_to_budget)
add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Displaying the budget
budget_display = tk.Text(app, height=10, width=30)
budget_display.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Button to save budget
save_button = tk.Button(app, text="Save Budget", command=save_budget)
save_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Label to display remaining budget
remaining_label = tk.Label(app, text="")
remaining_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Calculate remaining budget
calculate_button = tk.Button(app, text="Calculate Remaining Budget", command=calculate_remaining)
calculate_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Button to delete category
delete_button = tk.Button(app, text="Delete Category", command=delete_category)
delete_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

# Button to update category
update_button = tk.Button(app, text="Update Category", command=update_category)
update_button.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

# Run the application
app.mainloop()
