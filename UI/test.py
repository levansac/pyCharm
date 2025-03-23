import tkinter as tk
from tkinter import ttk

# Sample Data (Replace with real Cassandra query results)
data = [
    ("EMP001", "John", "Doe", "john.doe@example.com", "+1234567890", 0),  # Active
    ("EMP002", "Alice", "Smith", "alice.smith@example.com", "+1987654321", 1),  # Inactive
    ("EMP003", "Michael", "Brown", "michael.brown@example.com", "+1122334455", 0),  # Active
]


# Function to Convert Status (0 → "Active", 1 → "Inactive")
def get_status_text(status):
    return "Active" if status == 0 else "Inactive"


# Create Main Window
root = tk.Tk()
root.title("Employee Management")
root.geometry("600x400")

# Treeview Frame
frame = tk.Frame(root)
frame.pack(pady=20)

# Define Columns
columns = ("EmployeeCode", "FirstName", "LastName", "Email", "Phone", "Status")
tree = ttk.Treeview(frame, columns=columns, show="headings")

# Define Headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

# Insert Sample Data with Converted Status
for emp in data:
    tree.insert("", "end", values=(emp[0], emp[1], emp[2], emp[3], emp[4], get_status_text(emp[5])))

tree.pack()

# Labels & Entry Fields
labels = ["Employee Code:", "First Name:", "Last Name:", "Email:", "Phone:"]
entries = {}

for i, label in enumerate(labels):
    tk.Label(root, text=label).place(x=50, y=250 + (i * 30))
    entry = tk.Entry(root)
    entry.place(x=200, y=250 + (i * 30))
    entries[label] = entry  # Store Entry widgets in dictionary

# Status Label & Listbox
tk.Label(root, text="Status:").place(x=50, y=400)
status_listbox = tk.Listbox(root, height=2)
status_listbox.place(x=200, y=400)

# Populate Listbox with Status Options
status_options = ["Active", "Inactive"]
for status in status_options:
    status_listbox.insert(tk.END, status)


# Function to Display Selected Row in Entry Fields & Listbox
def on_tree_select(event):
    selected_item = tree.selection()
    if selected_item:
        values = tree.item(selected_item, "values")

        # Update Entry Fields
        for i, key in enumerate(labels):
            entries[key].delete(0, tk.END)
            entries[key].insert(0, values[i])

        # Update Status Listbox Selection
        status_listbox.selection_clear(0, tk.END)  # Clear previous selection
        for i, status in enumerate(status_options):
            if values[-1] == status:  # Compare with status text
                status_listbox.selection_set(i)


# Bind Selection Event
tree.bind("<<TreeviewSelect>>", on_tree_select)

# Run Application
#fd
root.mainloop()
