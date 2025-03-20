import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import uuid
from cassandra.cluster import Cluster
from connector.cassandra_connection import CassandraDB


def open_department_screen(root):
    global frame_department, entry_department_code, entry_department_name, entry_description, tree, selected_item

    selected_item = None

    frame_department = tk.Frame(root, padx=20, pady=20, bd=2, relief="solid", width=1100, height=600, bg="#ecf0f1")
    frame_department.pack(padx=3, pady=3,fill="both", expand=True)

    label_title = tk.Label(frame_department, text="Department Management", font=("Arial", 12, "bold"), bg="#ecf0f1")
    label_title.grid(row=0, column=0, columnspan=4, sticky="nw")

    label_department_code = tk.Label(frame_department, text="Code:", font=("Arial", 12), bg="#ecf0f1")
    label_department_code.grid(row=1, column=0, sticky="w")
    entry_department_code = tk.Entry(frame_department, font=("Arial", 12), width=15, relief="groove")
    entry_department_code.grid(row=1,column=1,padx=5, sticky="w")
    label_department_name = tk.Label(frame_department, text="Name:", font=("Arial", 12), bg="#ecf0f1")
    label_department_name.grid(row=1, column=2,padx=5)
    entry_department_name = tk.Entry(frame_department, font=("Arial", 12), width=40, relief="groove")
    entry_department_name.grid(row=1, column=3,padx=5)
    button_search = tk.Button(frame_department, text="Search", font=("Arial", 12), bg="#27ae60", fg="white", bd=2, activebackground="blue",
                   activeforeground="white", highlightthickness=7, relief="raised", command=search_department, cursor="hand2", justify="right")
    button_search.grid(row=1,column=7,padx=5)
    button_reset = tk.Button(frame_department, text="Clear", font=("Arial", 12), bg="#27ae60", fg="white", bd=2, activebackground="blue",
                   activeforeground="white", highlightthickness=7, relief="raised", command=showDataOnGrid, cursor="hand2", justify="right")
    button_reset.grid(row=1, column=8, padx=5,sticky="e")

    label_description = tk.Label(frame_department, text="Descriptions:", font=("Arial", 12), bg="#ecf0f1")
    label_description.grid(row=2, column=0, sticky="w")
    entry_description = tk.Entry(frame_department, font=("Arial", 12), width=70, relief="groove")
    entry_description.grid(row=2, column=1, columnspan=4)
    button_add = tk.Button(frame_department, text="Add", font=("Arial", 12), bg="#27ae60", fg="white", bd=2, activebackground="blue",
                   activeforeground="white", highlightthickness=7, relief="raised", command=add_department, cursor="hand2", justify="right")
    button_add.grid(row=2, column=8, sticky="e")

    # Button Edit
    button_edit = tk.Button(frame_department, text="Edit", font=("Arial", 12), bg="#efc497", fg="white", bd=2, activebackground="blue",
                   activeforeground="white", highlightthickness=7, relief="raised", cursor="hand2", justify="right", command=edit_department)
    button_edit.grid(row=4, column=5, padx=10, sticky="e")
    button_delete = tk.Button(frame_department, text="Delete", font=("Arial", 12), bg="#f3a0a0", fg="white", bd=2, activebackground="blue",
                   activeforeground="white", highlightthickness=7, relief="raised", cursor="hand2", justify="right", command=delete_department)
    button_delete.grid(row=4, column=8, sticky="e")

    # Function creating treeview
    creatingTreeView()
    return frame_department


def creatingTreeView():
    global tree, frame_department, selected_item
    # Create Treeview widget (Grid/Table)
    tree = ttk.Treeview(frame_department, show="headings")
    tree['columns'] = ('Id', 'DepartmentCode', 'DepartmentName', 'Descriptions')

    tree.heading('Id', text='Id')  # Hidden column
    tree.heading('DepartmentCode', text='Code')
    tree.heading('DepartmentName', text='Name')
    tree.heading('Descriptions', text='Descriptions')

    tree.column('Id', width=0, stretch=False)  # Hide the ID column
    tree.column('DepartmentCode', width=100, anchor='center')
    tree.column('DepartmentName', width=200, anchor='center')
    tree.column('Descriptions', width=300, anchor='center')

    # Add Style for borders
    style = ttk.Style()

    # Define treeview appearance
    style.configure("Treeview",
                    background="#f9f9f9",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#f9f9f9")

    # Define the style for the Treeview heading
    style.configure("Treeview.Heading",
                    font=("Arial", 12, "bold"),
                    background="#f1f1f1",
                    foreground="black")

    # Define borders for cells by adding padding
    style.map("Treeview",
              background=[('selected', '#dfe6e9')],
              foreground=[('selected', 'black')])

    # Insert data into the Treeview (grid)
    showDataOnGrid()

    # Add Scrollbars to Treeview
    vsb = ttk.Scrollbar(frame_department, orient="vertical", command=tree.yview)
    vsb.grid(row=3, column=9, sticky='ns')  # Place scrollbar at the right of the Treeview
    tree.configure(yscrollcommand=vsb.set)

    # Grid the Treeview widget
    tree.grid(row=3, column=0, columnspan=9, sticky="nsew", pady=5)

    # Configure row and column weights to make the Treeview expandable
    frame_department.grid_rowconfigure(2, weight=1)
    frame_department.grid_columnconfigure(0, weight=1)
    frame_department.grid_columnconfigure(1, weight=1)
    frame_department.grid_columnconfigure(2, weight=1)
    frame_department.grid_columnconfigure(3, weight=1)
    frame_department.grid_columnconfigure(4, weight=1)
    frame_department.grid_columnconfigure(5, weight=1)
    frame_department.grid_columnconfigure(6, weight=1)
    frame_department.grid_columnconfigure(7, weight=1)
    frame_department.grid_columnconfigure(8, weight=1)

    # Bind row selection event
    tree.bind("<<TreeviewSelect>>", on_item_select)


def on_item_select(event):
    global selected_item
    selected_items = tree.selection()

    if not selected_items:
        return  # No selection

    selected_item = selected_items[0]
    values = tree.item(selected_item, "values")

    entry_department_code.delete(0, tk.END)
    entry_department_code.insert(0, values[1])

    entry_department_name.delete(0, tk.END)
    entry_department_name.insert(0, values[2])

    entry_description.delete(0, tk.END)
    entry_description.insert(0, values[3])

def search_department():
    search_code = entry_department_code.get().strip().lower()
    search_name = entry_department_name.get().strip().lower()

    if not search_code or not search_name:
        messagebox.showwarning("Search Error", "Please enter a search information.")
        return

    for item in tree.get_children():
        tree.delete(item)

    for row in fetch_data_from_cassandra():
        if search_code in row.departmentcode.lower() or search_name in row.departmentname.lower():
            tree.insert('', 'end', values=(str(row.id), row.departmentcode, row.departmentname, row.descriptions))

def add_department():
    department_id = uuid.uuid4()
    department_code = entry_department_code.get().strip()
    department_name = entry_department_name.get().strip()
    description = entry_description.get().strip()

    if not department_code or not department_name:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    try:
        session = get_cassandra_session()

        # Check if department with same code exists
        check_query = "SELECT COUNT(*) FROM department WHERE DepartmentCode = %s"
        result = session.execute(check_query, (department_code,))
        count = result.one()[0]

        if count > 0:
            messagebox.showwarning("Duplicate Entry", "A department with this code already exists!")
            return

        insert_query = "INSERT INTO department (Id, DepartmentCode, DepartmentName, Descriptions) VALUES (%s, %s, %s, %s)"
        session.execute(insert_query, (department_id, department_code, department_name, description))

        entry_department_code.delete(0, tk.END)
        entry_department_name.delete(0, tk.END)
        entry_description.delete(0, tk.END)

        showDataOnGrid()
        messagebox.showinfo("Success", "Department added successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Error adding department: {str(e)}")


def delete_department():
    global selected_item
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a department to delete.")
        return

    try:
        department_id = uuid.UUID(tree.item(selected_item, "values")[0])  # Convert to UUID

        session = get_cassandra_session()
        query = "DELETE FROM department WHERE Id = %s"
        session.execute(query, (department_id,))

        tree.delete(selected_item)
        messagebox.showinfo("Success", "Department deleted successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Error deleting department: {str(e)}")


def edit_department():
    global selected_item
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a record to edit.")
        return

    department_code = entry_department_code.get().strip()
    department_name = entry_department_name.get().strip()
    description = entry_description.get().strip()

    if not department_code or not department_name:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    try:
        department_id = uuid.UUID(tree.item(selected_item, "values")[0])  # Convert to UUID

        session = get_cassandra_session()
        query = "UPDATE department SET DepartmentCode = %s, DepartmentName = %s, Descriptions = %s WHERE Id = %s"
        session.execute(query, (department_code, department_name, description, department_id))

        showDataOnGrid()
        messagebox.showinfo("Success", "Department updated successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Error updating department: {str(e)}")


def fetch_data_from_cassandra():
    session = get_cassandra_session()
    query = "SELECT * FROM department"
    return sorted(session.execute(query), key=lambda row: row.departmentcode)


def showDataOnGrid():
    for item in tree.get_children():
        tree.delete(item)

    for row in fetch_data_from_cassandra():
        tree.insert('', 'end', values=(str(row.id), row.departmentcode, row.departmentname, row.descriptions))


def get_cassandra_session():
    return CassandraDB().get_session()
