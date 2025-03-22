import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import uuid
from connector.cassandra_connection import CassandraDB
import datetime
from common.utilities import export_to_excel


def open_employee_screen(root):
    global frame_employee, entry_employee_code, entry_employee_firstname, entry_description, tree, selected_item

    selected_item = None

    frame_employee = tk.Frame(root, padx=20, pady=20, bd=2, relief="solid", width=1100, height=600, bg="#ecf0f1")
    frame_employee.pack(padx=3, pady=3, fill="both", expand=True)

    label_title = tk.Label(frame_employee, text="Employee Management", font=("Arial", 12, "bold"), bg="#ecf0f1")
    label_title.grid(row=0, column=0, columnspan=4, sticky="nw")

    label_employee_code = tk.Label(frame_employee, text="Employee Code:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_code.grid(row=1, column=0, sticky="w")
    entry_employee_code = tk.Entry(frame_employee, font=("Arial", 12), relief="groove")
    entry_employee_code.grid(row=1, column=1, columnspan=2, sticky="w")
    label_employee_firstname = tk.Label(frame_employee, text="First Name:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_firstname.grid(row=1, column=3, sticky="e")
    entry_employee_firstname = tk.Entry(frame_employee, font=("Arial", 12), relief="groove")
    entry_employee_firstname.grid(row=1, column=4, columnspan=3, sticky="ew")
    button_search = tk.Button(frame_employee, text="Search", font=("Arial", 12), bg="#27ae60", fg="white", bd=2,
                              activebackground="blue",
                              activeforeground="white", highlightthickness=7, relief="raised",
                              command=search_employee, cursor="hand2", justify="right", height=1, width=6)
    button_search.grid(row=1, column=7, sticky="e", padx=(0, 5))
    button_reset = tk.Button(frame_employee, text="Clear", font=("Arial", 12), bg="#27ae60", fg="white", bd=2,
                             activebackground="blue",
                             activeforeground="white", highlightthickness=7, relief="raised", command=reset_fields,
                             cursor="hand2", justify="right", height=1, width=6)
    button_reset.grid(row=1, column=8, sticky="e")

    label_description = tk.Label(frame_employee, text="Descriptions:", font=("Arial", 12), bg="#ecf0f1")
    label_description.grid(row=2, column=0, sticky="w")
    entry_description = tk.Entry(frame_employee, font=("Arial", 12), relief="groove")
    entry_description.grid(row=2, column=1, columnspan=6, sticky="ew")
    button_add = tk.Button(frame_employee, text="Add", font=("Arial", 12), bg="#27ae60", fg="white", bd=2,
                           activebackground="blue",
                           activeforeground="white", highlightthickness=7, relief="raised", command=add_employee,
                           cursor="hand2", justify="right", height=1, width=6)
    button_add.grid(row=2, column=8, sticky="e", pady=(5, 0))

    button_export = tk.Button(frame_employee, text="Export", font=("Arial", 12), bg="#f3a0a0", fg="white", bd=2,
                              activebackground="blue",
                              activeforeground="white", highlightthickness=7, relief="raised", cursor="hand2",
                              justify="right", command=lambda: export_to_excel(tree), height=1, width=6)
    button_export.grid(row=4, column=6, sticky="e", padx=(0, 5))
    button_edit = tk.Button(frame_employee, text="Edit", font=("Arial", 12), bg="#efc497", fg="white", bd=2,
                            activebackground="blue",
                            activeforeground="white", highlightthickness=7, relief="raised", cursor="hand2",
                            justify="right", command=edit_employee, height=1, width=6)
    button_edit.grid(row=4, column=7, sticky="e", padx=(0, 5))
    button_delete = tk.Button(frame_employee, text="Delete", font=("Arial", 12), bg="#f3a0a0", fg="white", bd=2,
                              activebackground="blue",
                              activeforeground="white", highlightthickness=7, relief="raised", cursor="hand2",
                              justify="right", command=delete_employee, height=1, width=6)
    button_delete.grid(row=4, column=8, sticky="e")

    # Function creating treeview
    creatingTreeView()
    return frame_employee


def creatingTreeView():
    global tree, frame_employee, selected_item
    # Create Treeview widget (Grid/Table)
    tree = ttk.Treeview(frame_employee, show="headings", height=12)

    tree['columns'] = ('Id', 'EmployeeCode', 'FirstName', 'LastName', 'Email', 'Phone','DepartmentId',
                        'RoleId', 'StartDate', 'EndDate','CreatedDate', 'ModifiedDate')

    tree.heading('Id', text='Id')  # Hidden column
    tree.heading('EmployeeCode', text='EmployeeCode')
    tree.heading('FirstName', text='FirstName')
    tree.heading('LastName', text='LastName')
    tree.heading('Email', text='Email')
    tree.heading('Phone', text='Phone')
    tree.heading('DepartmentId', text='DepartmentId')
    tree.heading('RoleId', text='RoleId')
    tree.heading('StartDate', text='StartDate')
    tree.heading('EndDate', text='EndDate')

    tree.heading('CreatedDate', text='Created Date')
    tree.heading('ModifiedDate', text='Modified Date')

    tree.column('Id', width=0, stretch=False)  # Hide the ID column
    tree.column('EmployeeCode', width=50, anchor='center')
    tree.column('FirstName', width=200, anchor='center')
    tree.column('LastName', width=300, anchor='center')
    tree.column('Email', width=100, anchor='center')
    tree.column('Phone', width=100, anchor='center')
    tree.column('DepartmentId', width=100, anchor='center')
    tree.column('RoleId', width=100, anchor='center')
    tree.column('StartDate', width=100, anchor='center')
    tree.column('EndDate', width=100, anchor='center')
    tree.column('CreatedDate', width=100, anchor='center')
    tree.column('ModifiedDate', width=100, anchor='center')

    # Add Style for borders
    style = ttk.Style()

    # Define treeview appearance
    style.configure("Treeview",
                    background="#f9f9f9",
                    foreground="black",
                    rowheight=39,
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
    vsb = ttk.Scrollbar(frame_employee, orient="vertical", command=tree.yview)
    vsb.grid(row=3, column=9, sticky='ns')  # Place scrollbar at the right of the Treeview
    tree.configure(yscrollcommand=vsb.set)

    # Grid the Treeview widget
    tree.grid(row=3, column=0, columnspan=9, sticky="nsew", pady=5)

    # Configure row and column weights to make the Treeview expandable
    frame_employee.grid_rowconfigure(1, weight=0)
    frame_employee.grid_rowconfigure(2, weight=0)
    frame_employee.grid_columnconfigure(0, weight=0)
    frame_employee.grid_columnconfigure(1, weight=1)
    frame_employee.grid_columnconfigure(2, weight=0)
    frame_employee.grid_columnconfigure(3, weight=0)
    frame_employee.grid_columnconfigure(4, weight=0)
    frame_employee.grid_columnconfigure(5, weight=1)
    frame_employee.grid_columnconfigure(6, weight=0)
    frame_employee.grid_columnconfigure(7, weight=1)
    frame_employee.grid_columnconfigure(8, weight=0)

    # Bind row selection event
    tree.bind("<<TreeviewSelect>>", on_item_select)
    tree.bind("<Double-1>", on_double_click)  # Bind double-click to show full value


def on_double_click(event):
    global selected_item
    selected_item = tree.selection()  # Get selected row
    if selected_item:
        values = tree.item(selected_item, "values")  # Get all column values
        column = tree.identify_column(event.x)  # Identify which column was clicked
        col_index = int(column[1:]) - 1  # Convert column format (‘#1’, ‘#2’) to an index

        if 0 <= col_index < len(values):  # Ensure valid index
            messagebox.showinfo("Full Value", values[col_index])  # Show full value


def on_item_select(event):
    global selected_item
    selected_items = tree.selection()

    if not selected_items:
        return  # No selection

    selected_item = selected_items[0]
    values = tree.item(selected_item, "values")

    entry_employee_code.delete(0, tk.END)
    entry_employee_code.insert(0, values[1])

    entry_employee_firstname.delete(0, tk.END)
    entry_employee_firstname.insert(0, values[2])


def search_employee():
    search_code = entry_employee_code.get().strip().lower()
    search_name = entry_employee_firstname.get().strip().lower()

    if not search_code and not search_name:
        reset_fields()
        return

    # Clear previous search results
    for item in tree.get_children():
        tree.delete(item)

    try:
        for row in fetch_data_from_cassandra():
            if (search_code and search_code in row.employeecode.lower()) or \
                    (search_name and search_name in row.employeename.lower()):
                tree.insert('', 'end', values=(
                    str(row.id), row.employeecode, row.employeename, row.descriptions, row.createddate,
                    row.modifieddate))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def add_employee():
    employee_id = uuid.uuid4()
    employee_code = entry_employee_code.get().strip()
    employee_firstname = entry_employee_firstname.get().strip()
    # description = entry_description.get().strip()
    created_date = datetime.datetime.now()

    if not employee_code or not employee_firstname:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    try:
        session = get_cassandra_session()

        # Check if employee with same code exists
        check_query = "SELECT COUNT(*) FROM employee WHERE EmployeeCode = %s"
        result = session.execute(check_query, (employee_code,))
        count = result.one()[0]

        if count > 0:
            messagebox.showwarning("Duplicate Entry", "A employee with this code already exists!")
            return

        insert_query = "INSERT INTO employee (Id, EmployeeCode, FirstName) VALUES (%s, %s, %s, %s)"
        session.execute(insert_query, (employee_id, employee_code, employee_firstname))

        entry_employee_code.delete(0, tk.END)
        entry_employee_firstname.delete(0, tk.END)
        entry_description.delete(0, tk.END)

        showDataOnGrid()
        messagebox.showinfo("Success", "Employee added successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Error adding employee: {str(e)}")


def delete_employee():
    global selected_item
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a employee to delete.")
        return

    try:
        employee_id = uuid.UUID(tree.item(selected_item, "values")[0])  # Convert to UUID

        session = get_cassandra_session()
        query = "DELETE FROM employee WHERE Id = %s"
        session.execute(query, (employee_id,))

        tree.delete(selected_item)
        messagebox.showinfo("Success", "Employee deleted successfully!")
        reset_fields()

    except Exception as e:
        messagebox.showerror("Error", f"Error deleting employee: {str(e)}")


def edit_employee():
    global selected_item
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a record to edit.")
        return

    employee_code = entry_employee_code.get().strip()
    employee_firstname = entry_employee_firstname.get().strip()
    description = entry_description.get().strip()
    modified_date = datetime.datetime.now()

    if not employee_code or not employee_firstname:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    try:
        employee_id = uuid.UUID(tree.item(selected_item, "values")[0])  # Convert to UUID

        session = get_cassandra_session()
        query = "UPDATE employee SET EmployeeCode = %s, FirstName = %s, ModifiedDate = %s WHERE Id = %s"
        session.execute(query, (employee_code, employee_firstname, modified_date, employee_id))

        showDataOnGrid()
        messagebox.showinfo("Success", "Employee updated successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Error updating employee: {str(e)}")


def fetch_data_from_cassandra():
    session = get_cassandra_session()
    query = "SELECT * FROM employee"
    return sorted(session.execute(query), key=lambda row: row.employeecode)


def showDataOnGrid():
    for item in tree.get_children():
        tree.delete(item)

    for row in fetch_data_from_cassandra():
        tree.insert('', 'end', values=(
            str(row.id), row.employeecode, row.firstname, row.lastname,  row.email,row.phone,row.departmentid, row.roleid, row.startdate,row.enddate,row.createddate, row.modifieddate))

def get_cassandra_session():
    return CassandraDB().get_session()


def reset_fields():
    entry_employee_code.delete(0, tk.END)
    entry_employee_firstname.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    showDataOnGrid()  # Refresh the grid
