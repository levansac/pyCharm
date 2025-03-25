import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import uuid
from connector.cassandra_connection import CassandraDB
import datetime
from common.utilities import export_to_excel


def open_employee_screen(root):
    global frame_employee, entry_employee_code, entry_employee_firstname,entry_employee_lastname,entry_employee_email, tree, selected_item, entry_employee_phone,entry_employee_department,entry_employee_role,entry_employee_status

    selected_item = None

    frame_employee = tk.Frame(root, padx=20, pady=20, bd=2, relief="solid", width=1100, height=600, bg="#ecf0f1")
    frame_employee.pack(padx=3, pady=3, fill="both", expand=True)

    label_title = tk.Label(frame_employee, text="Employee Management", font=("Arial", 12, "bold"), bg="#ecf0f1")
    label_title.grid(row=0, column=0, columnspan=4, sticky="nw")

    label_employee_code = tk.Label(frame_employee, text="Code:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_code.grid(row=1, column=0)
    entry_employee_code = tk.Entry(frame_employee, font=("Arial", 12), relief="groove")
    entry_employee_code.grid(row=1, column=1)
    label_employee_firstname = tk.Label(frame_employee, text="First Name:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_firstname.grid(row=1, column=2, )
    entry_employee_firstname = tk.Entry(frame_employee, font=("Arial", 12), relief="groove")
    entry_employee_firstname.grid(row=1, column=3,)

    label_employee_lastname = tk.Label(frame_employee, text="Last Name:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_lastname.grid(row=1, column=4)
    entry_employee_lastname = tk.Entry(frame_employee, font=("Arial", 12), relief="groove")
    entry_employee_lastname.grid(row=1, column=5)

    label_employee_email = tk.Label(frame_employee, text="Email:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_email.grid(row=1, column=6)
    entry_employee_email = tk.Entry(frame_employee, font=("Arial", 12), relief="groove")
    entry_employee_email.grid(row=1, column=7)

    button_search = tk.Button(frame_employee, text="Search", font=("Arial", 12), bg="#27ae60", fg="white", bd=2,
                              activebackground="blue",
                              activeforeground="white", highlightthickness=7, relief="raised",
                              command=search_employee, cursor="hand2", justify="right", height=1, width=6)
    button_search.grid(row=1, column=8, sticky="e", padx=(0, 5))
    button_reset = tk.Button(frame_employee, text="Clear", font=("Arial", 12), bg="#27ae60", fg="white", bd=2,
                             activebackground="blue",
                             activeforeground="white", highlightthickness=7, relief="raised", command=reset_fields,
                             cursor="hand2", justify="right", height=1, width=6)
    button_reset.grid(row=1, column=9, sticky="e")

    label_employee_phone = tk.Label(frame_employee, text="Phone:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_phone.grid(row=2, column=0)
    entry_employee_phone = tk.Entry(frame_employee, font=("Arial", 12), relief="groove")
    entry_employee_phone.grid(row=2, column=1)
    label_employee_department = tk.Label(frame_employee, text="Department:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_department.grid(row=2, column=2)
    entry_employee_department = tk.Entry(frame_employee, font=("Arial", 12), relief="groove")
    entry_employee_department.grid(row=2, column=3)

    label_employee_role = tk.Label(frame_employee, text="Role:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_role.grid(row=2, column=4)
    entry_employee_role = tk.Entry(frame_employee, font=("Arial", 12), relief="groove")
    entry_employee_role.grid(row=2, column=5)

    label_employee_status = tk.Label(frame_employee, text="Status:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_status.grid(row=2, column=6)
    entry_employee_status = tk.Entry(frame_employee, font=("Arial", 12), relief="groove", state="readonly")
    entry_employee_status.grid(row=2, column=7)
    # Disable user selection change

    button_add = tk.Button(frame_employee, text="Add", font=("Arial", 12), bg="#27ae60", fg="white", bd=2,
                           activebackground="blue",
                           activeforeground="white", highlightthickness=7, relief="raised", command=add_employee,
                           cursor="hand2", justify="right", height=1, width=6)
    button_add.grid(row=2, column=9, sticky="e", pady=(5, 0))

    button_export = tk.Button(frame_employee, text="Export", font=("Arial", 12), bg="#f3a0a0", fg="white", bd=2,
                              activebackground="blue",
                              activeforeground="white", highlightthickness=7, relief="raised", cursor="hand2",
                              justify="right", command=lambda: export_to_excel(tree), height=1, width=6)
    button_export.grid(row=5, column=5, sticky="e",)
    button_edit = tk.Button(frame_employee, text="Edit", font=("Arial", 12), bg="#efc497", fg="white", bd=2,
                            activebackground="blue",
                            activeforeground="white", highlightthickness=7, relief="raised", cursor="hand2",
                            justify="right", command=edit_employee, height=1, width=6)
    button_edit.grid(row=5, column=8, sticky="e", padx=(0, 5))
    button_delete = tk.Button(frame_employee, text="Delete", font=("Arial", 12), bg="#f3a0a0", fg="white", bd=2,
                              activebackground="blue",
                              activeforeground="white", highlightthickness=7, relief="raised", cursor="hand2",
                              justify="right", command=delete_employee, height=1, width=6)
    button_delete.grid(row=5, column=9, sticky="e")

    # Function creating treeview
    creatingTreeView()
    return frame_employee


def creatingTreeView():
    global tree, frame_employee, selected_item
    # Create Treeview widget (Grid/Table)
    tree = ttk.Treeview(frame_employee, show="headings", height=17)

    tree['columns'] = ('Id', 'EmployeeCode', 'FirstName', 'LastName', 'Email', 'Phone','DepartmentId',
                        'RoleId', 'Status','StartDate', 'EndDate','CreatedDate', 'ModifiedDate')

    tree.heading('Id', text='Id')  # Hidden column
    tree.heading('EmployeeCode', text='Code')
    tree.heading('FirstName', text='FirstName')
    tree.heading('LastName', text='LastName')
    tree.heading('Email', text='Email')
    tree.heading('Phone', text='Phone')
    tree.heading('DepartmentId', text='DepartmentId')
    tree.heading('RoleId', text='RoleId')
    tree.heading('Status', text='Status')
    tree.heading('StartDate', text='StartDate')
    tree.heading('EndDate', text='EndDate')

    tree.heading('CreatedDate', text='Created Date')
    tree.heading('ModifiedDate', text='Modified Date')

    tree.column('Id', width=0, stretch=False)  # Hide the ID column
    tree.column('EmployeeCode', width=150, anchor='center')
    tree.column('FirstName', width=200, anchor='center')
    tree.column('LastName', width=200, anchor='center')
    tree.column('Email', width=250, anchor='center')
    tree.column('Phone', width=100, anchor='center')
    tree.column('DepartmentId', width=100, anchor='center')
    tree.column('RoleId', width=100, anchor='center')
    tree.column('Status', width=100, anchor='center')
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
                    rowheight=31,
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
    show_data_on_grid()

    # Add Scrollbars to Treeview
    vsb = ttk.Scrollbar(frame_employee, orient="vertical", command=tree.yview)
    vsb.grid(row=3, column=10, sticky='ns')  # Place scrollbar at the right of the Treeview

    # Horizontal scrollbar
    hsb = ttk.Scrollbar(frame_employee, orient="horizontal", command=tree.xview)
    hsb.grid(row=4, column=0, columnspan=10, sticky='ew')

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)


    # Grid the Treeview widget
    tree.grid(row=3, column=0, columnspan=10, sticky="nsew", pady=5)

    # Configure row and column weights to make the Treeview expandable
    frame_employee.grid_rowconfigure(1, weight=0)
    frame_employee.grid_rowconfigure(2, weight=0)
    frame_employee.grid_rowconfigure(3, weight=0)
    frame_employee.grid_rowconfigure(4, weight=0)
    frame_employee.grid_rowconfigure(5, weight=0)
    frame_employee.grid_rowconfigure(6, weight=0)
    frame_employee.grid_columnconfigure(0, weight=0)
    frame_employee.grid_columnconfigure(1, weight=0)
    frame_employee.grid_columnconfigure(2, weight=0)
    frame_employee.grid_columnconfigure(3, weight=0)
    frame_employee.grid_columnconfigure(4, weight=0)
    frame_employee.grid_columnconfigure(5, weight=0)
    frame_employee.grid_columnconfigure(6, weight=0)
    frame_employee.grid_columnconfigure(7, weight=1)
    frame_employee.grid_columnconfigure(8, weight=0)
    frame_employee.grid_columnconfigure(9, weight=0)
    frame_employee.grid_columnconfigure(10, weight=0)

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
    entry_employee_lastname.delete(0, tk.END)
    entry_employee_lastname.insert(0, values[3])
    entry_employee_email.delete(0, tk.END)
    entry_employee_email.insert(0, values[4])
    entry_employee_phone.delete(0, tk.END)
    entry_employee_phone.insert(0, values[5])
    entry_employee_department.delete(0, tk.END)
    entry_employee_department.insert(0, values[6])
    entry_employee_role.delete(0, tk.END)
    entry_employee_role.insert(0, values[7])
    entry_employee_status.config(state="normal")
    entry_employee_status.delete(0, tk.END)
    entry_employee_status.insert(0, values[8])
    entry_employee_status.config(state="readonly")


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
        fetch_employees_with_details(search_code,search_name)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")





def add_employee():
    employee_id = uuid.uuid4()
    employee_code = entry_employee_code.get().strip()
    employee_firstname = entry_employee_firstname.get().strip()
    employee_lastname = entry_employee_lastname.get().strip()
    employee_email = entry_employee_email.get().strip()
    employee_phone = entry_employee_phone.get().strip()
    employee_status = 0
    created_date = datetime.datetime.now()
    employee_department = uuid.UUID(entry_employee_department.get().strip())
    employee_role = uuid.UUID(entry_employee_role.get().strip())

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

        insert_query = "INSERT INTO employee (Id, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, CreatedDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        session.execute(insert_query, (employee_id, employee_code, employee_firstname, employee_lastname,employee_email, employee_phone,employee_department,employee_role, employee_status, created_date))

        messagebox.showinfo("Success", "Employee added successfully!")
        reset_fields()


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
    modified_date = datetime.datetime.now()

    if not employee_code or not employee_firstname:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    try:
        employee_id = uuid.UUID(tree.item(selected_item, "values")[0])  # Convert to UUID

        session = get_cassandra_session()
        query = "UPDATE employee SET EmployeeCode = %s, FirstName = %s, ModifiedDate = %s WHERE Id = %s"
        session.execute(query, (employee_code, employee_firstname, modified_date, employee_id))

        show_data_on_grid()
        messagebox.showinfo("Success", "Employee updated successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Error updating employee: {str(e)}")


def fetch_data_from_cassandra():
    session = get_cassandra_session()
    query = "SELECT * FROM employee"
    return sorted(session.execute(query), key=lambda row: row.employeecode)


def show_data_on_grid():
    for item in tree.get_children():
        tree.delete(item)

    for employee in fetch_employees_with_details():
        tree.insert('', 'end', values=employee)

def get_department_dict():
    session = get_cassandra_session()
    query = "SELECT Id, DepartmentName FROM department"
    rows = session.execute(query)

    # Create a dictionary {department_id: department_name}
    return {str(row.id): row.departmentname for row in rows}


def get_role_dict():
    session = get_cassandra_session()
    query = "SELECT Id, RoleName FROM role"
    rows = session.execute(query)

    # Create a dictionary {role_id: role_name}
    return {str(row.id): row.rolename for row in rows}


def fetch_employees_with_details(search_code=None, search_name=None):
    session = get_cassandra_session()
    query = "SELECT Id, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, EndDate, CreatedDate, ModifiedDate FROM employee"

    rows = session.execute(query)

    # Get department and role dictionaries
    dept_dict = get_department_dict()
    role_dict = get_role_dict()

    employees = []
    for row in rows:
        department_name = dept_dict.get(str(row.departmentid), "Unknown")  # Lookup department name
        role_name = role_dict.get(str(row.roleid), "Unknown")  # Lookup role name
        employees.append((
            str(row.id), row.employeecode, row.firstname, row.lastname, row.email,
            row.phone, department_name, role_name, get_status_text(row.status),
            row.startdate, row.enddate, row.createddate, row.modifieddate
        ))

    return employees


def get_cassandra_session():
    return CassandraDB().get_session()


def reset_fields():
    entry_employee_code.delete(0, tk.END)
    entry_employee_firstname.delete(0, tk.END)
    entry_employee_lastname.delete(0, tk.END)
    entry_employee_phone.delete(0, tk.END)
    entry_employee_email.delete(0, tk.END)
    entry_employee_department.delete(0, tk.END)
    entry_employee_role.delete(0, tk.END)
    entry_employee_status.config(state="normal")
    entry_employee_status.delete(0, tk.END)
    entry_employee_status.config(state="readonly")

    show_data_on_grid()  # Refresh the grid

# Function to Convert Status (0 → "Active", 1 → "Inactive")
def get_status_text(status):
    return "Active" if status == 0 else "Inactive"