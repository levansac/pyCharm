import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import uuid
from connector.cassandra_connection import CassandraDB
# import datetime
from datetime import datetime
from common.utilities import export_to_excel, get_status_text, get_status_id
from tkcalendar import DateEntry

def open_employee_screen(root):
    global stored_role_dict,stored_department_dict, frame_employee, entry_employee_code, entry_employee_firstname,\
        entry_employee_lastname,entry_employee_email, tree, selected_item, entry_employee_phone,entry_employee_department,\
        entry_employee_role,entry_employee_status,entry_employee_startdate,entry_employee_enddate,entry_employee_createdate,\
        entry_employee_modifieddate, entry_search_code, entry_search_firstname, entry_search_lastname, entry_search_status

    selected_item = None
    # Get only active departments
    department_dict = get_department_dict(True)
    department_names = list(department_dict.values())

    # Get all department
    stored_department_dict = get_department_dict()

    # Get only active roles
    role_dict = get_role_dict(True)
    role_names = list(role_dict.values())

    # Get all role
    stored_role_dict = get_role_dict()

    frame_employee = tk.Frame(root, padx=20, pady=20, bd=2, relief="solid", width=1100, height=600, bg="#ecf0f1")
    frame_employee.pack(padx=3, pady=3, fill="both", expand=True)

    label_title = tk.Label(frame_employee, text="Employee Management", font=("Arial", 12, "bold"), bg="#ecf0f1")
    label_title.grid(row=0, column=0, columnspan=4, sticky="nw")

    search_frame = ttk.LabelFrame(frame_employee, text="Search")
    search_frame.grid(row=1, column=0, columnspan=10, sticky="nsew", pady=5)
    search_frame.grid_columnconfigure(0, weight=0)
    search_frame.grid_columnconfigure(1, weight=0)
    search_frame.grid_columnconfigure(2, weight=0)
    search_frame.grid_columnconfigure(3, weight=0)
    search_frame.grid_columnconfigure(4, weight=0)
    search_frame.grid_columnconfigure(5, weight=0)
    search_frame.grid_columnconfigure(6, weight=0)
    search_frame.grid_columnconfigure(7, weight=1)
    search_frame.grid_columnconfigure(8, weight=0)
    search_frame.grid_columnconfigure(9, weight=0)

    label_search_code = tk.Label(search_frame, text="Code:", font=("Arial", 12), bg="#ecf0f1")
    label_search_code.grid(row=1, column=0)
    entry_search_code = tk.Entry(search_frame, font=("Arial", 12), relief="groove")
    entry_search_code.grid(row=1, column=1)
    label_search_firstname = tk.Label(search_frame, text="First Name:", font=("Arial", 12), bg="#ecf0f1")
    label_search_firstname.grid(row=1, column=2, )
    entry_search_firstname = tk.Entry(search_frame, font=("Arial", 12), relief="groove")
    entry_search_firstname.grid(row=1, column=3, )
    label_search_lastname = tk.Label(search_frame, text="Last Name:", font=("Arial", 12), bg="#ecf0f1")
    label_search_lastname.grid(row=1, column=4)
    entry_search_lastname = tk.Entry(search_frame, font=("Arial", 12), relief="groove")
    entry_search_lastname.grid(row=1, column=5)

    label_search_status = tk.Label(search_frame, text="Status:", font=("Arial", 12), bg="#ecf0f1")
    label_search_status.grid(row=1, column=6)
    entry_search_status = ttk.Combobox(search_frame, values=["Active", "Inactive"], font=("Arial", 12), state="readonly")
    entry_search_status.grid(row=1, column=7)


    button_search = tk.Button(search_frame, text="Search", font=("Arial", 12), bg="#27ae60", fg="white", bd=2,
                              activebackground="blue",
                              activeforeground="white", highlightthickness=7, relief="raised",
                              command=search_employee, cursor="hand2", justify="right", height=1, width=6)
    button_search.grid(row=1, column=8, sticky="e", padx=(0, 5))
    button_reset = tk.Button(search_frame, text="Clear", font=("Arial", 12), bg="#27ae60", fg="white", bd=2,
                             activebackground="blue",
                             activeforeground="white", highlightthickness=7, relief="raised", command=reset_fields,
                             cursor="hand2", justify="right", height=1, width=6)
    button_reset.grid(row=1, column=9, sticky="e", pady=(0,3))
    details_frame = ttk.LabelFrame(frame_employee, text="Details")
    details_frame.grid(row=4, column=0, columnspan=10, sticky="nsew", pady=5)
    label_employee_code = tk.Label(details_frame, text="Code:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_code.grid(row=4, column=0, pady=10)
    entry_employee_code = tk.Entry(details_frame, font=("Arial", 12), relief="groove")
    entry_employee_code.grid(row=4, column=1)
    label_employee_firstname = tk.Label(details_frame, text="First Name:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_firstname.grid(row=4, column=2, )
    entry_employee_firstname = tk.Entry(details_frame, font=("Arial", 12), relief="groove")
    entry_employee_firstname.grid(row=4, column=3,)
    label_employee_lastname = tk.Label(details_frame, text="Last Name:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_lastname.grid(row=4, column=4)
    entry_employee_lastname = tk.Entry(details_frame, font=("Arial", 12), relief="groove")
    entry_employee_lastname.grid(row=4, column=5)
    label_employee_department = tk.Label(details_frame, text="Department:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_department.grid(row=4, column=6)
    entry_employee_department = ttk.Combobox(details_frame, values=department_names, font=("Arial", 12),state="readonly")
    entry_employee_department.grid(row=4, column=7)
    label_employee_phone = tk.Label(details_frame, text="Phone:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_phone.grid(row=5, column=0, pady=10)
    entry_employee_phone = tk.Entry(details_frame, font=("Arial", 12), relief="groove")
    entry_employee_phone.grid(row=5, column=1)
    label_employee_email = tk.Label(details_frame, text="Email:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_email.grid(row=5, column=2)
    entry_employee_email = tk.Entry(details_frame, font=("Arial", 12), relief="groove")
    entry_employee_email.grid(row=5, column=3)
    label_employee_startdate = tk.Label(details_frame, text="Start Date:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_startdate.grid(row=5, column=4)
    entry_employee_startdate = DateEntry(details_frame, width=18, background='darkblue',
                                         foreground='white', borderwidth=2, font=("Arial", 12),
                                         date_pattern='yyyy-MM-dd',relief="groove")  # Format: YYYY-MM-DD
    entry_employee_startdate.grid(row=5, column=5)
    entry_employee_startdate._set_text('')
    label_employee_role = tk.Label(details_frame, text="Role:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_role.grid(row=5, column=6)
    entry_employee_role = ttk.Combobox(details_frame, values=role_names, font=("Arial", 12),state="readonly")
    entry_employee_role.grid(row=5, column=7)
    label_employee_enddate = tk.Label(details_frame, text="End Date:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_enddate.grid(row=6, column=0, pady=10)
    entry_employee_enddate = DateEntry(details_frame, width=18, background='darkblue',
                                         foreground='white', borderwidth=2, font=("Arial", 12),
                                         date_pattern='yyyy-MM-dd',relief="groove")  # Format: YYYY-MM-DD
    entry_employee_enddate.grid(row=6, column=1)
    entry_employee_enddate._set_text('')
    label_employee_createdate = tk.Label(details_frame, text="Created Date:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_createdate.grid(row=6, column=2)
    entry_employee_createdate = tk.Entry(details_frame, font=("Arial", 12), relief="groove", state="readonly")
    entry_employee_createdate.grid(row=6, column=3)
    label_employee_modifieddate = tk.Label(details_frame, text="Modified Date:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_modifieddate.grid(row=6, column=4)
    entry_employee_modifieddate = tk.Entry(details_frame, font=("Arial", 12), relief="groove", state="readonly")
    entry_employee_modifieddate.grid(row=6, column=5)
    label_employee_status = tk.Label(details_frame, text="Status:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_status.grid(row=6, column=6)
    entry_employee_status = ttk.Combobox(details_frame, values=["Active", "Inactive"], font=("Arial", 12), state="readonly")
    entry_employee_status.grid(row=6, column=7)

    button_export = tk.Button(frame_employee, text="Export", font=("Arial", 12), bg="#f3a0a0", fg="white", bd=2,
                              activebackground="blue",
                              activeforeground="white", highlightthickness=7, relief="raised", cursor="hand2",
                              justify="right", command=lambda: export_to_excel(tree), height=1, width=6)
    button_export.grid(row=7, column=7, sticky="e",padx=(0, 5), pady=5)
    button_edit = tk.Button(frame_employee, text="Edit", font=("Arial", 12), bg="#efc497", fg="white", bd=2,
                            activebackground="blue",
                            activeforeground="white", highlightthickness=7, relief="raised", cursor="hand2",
                            justify="right", command=edit_employee, height=1, width=6)
    button_edit.grid(row=7, column=8, sticky="e",padx=(0, 5))
    button_add = tk.Button(frame_employee, text="Add", font=("Arial", 12), bg="#27ae60", fg="white", bd=2,
                           activebackground="blue",
                           activeforeground="white", highlightthickness=7, relief="raised", command=add_employee,
                           cursor="hand2", justify="right", height=1, width=6)
    button_add.grid(row=7, column=9, sticky="e")

    # Function creating treeview
    creatingTreeView()
    return frame_employee

def creatingTreeView():
    global tree, frame_employee, selected_item
    # Create Treeview widget (Grid/Table)
    tree = ttk.Treeview(frame_employee, show="headings", height=15)

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
    tree.column('Email', width=200, anchor='center')
    tree.column('Phone', width=100, anchor='center')
    tree.column('DepartmentId', width=150, anchor='center')
    tree.column('RoleId', width=150, anchor='center')
    tree.column('Status', width=100, anchor='center')
    tree.column('StartDate', width=150, anchor='center')
    tree.column('EndDate', width=150, anchor='center')
    tree.column('CreatedDate', width=150, anchor='center')
    tree.column('ModifiedDate', width=150, anchor='center')

    # Add Style for borders
    style = ttk.Style()

    # Define treeview appearance
    style.configure("Treeview",
                    background="#f9f9f9",
                    foreground="black",
                    rowheight=26,
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
    vsb.grid(row=2, column=10, sticky='ns')  # Place scrollbar at the right of the Treeview

    # Horizontal scrollbar
    hsb = ttk.Scrollbar(frame_employee, orient="horizontal", command=tree.xview)
    hsb.grid(row=3, column=0, columnspan=10, sticky='ew')
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Grid the Treeview widget
    tree.grid(row=2, column=0, columnspan=10, sticky="nsew", pady=5)

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

    def safe_value(index):
        """Returns an empty string if the value is None or out of range."""
        return values[index] if index < len(values) and values[index] not in [None, "None"] else ""

    entry_employee_code.delete(0, tk.END)
    entry_employee_code.insert(0, safe_value(1))
    entry_employee_firstname.delete(0, tk.END)
    entry_employee_firstname.insert(0, safe_value(2))
    entry_employee_lastname.delete(0, tk.END)
    entry_employee_lastname.insert(0, safe_value(3))
    entry_employee_email.delete(0, tk.END)
    entry_employee_email.insert(0, safe_value(4))
    entry_employee_phone.delete(0, tk.END)
    entry_employee_phone.insert(0, safe_value(5))
    entry_employee_department.set(safe_value(6))
    entry_employee_role.set(safe_value(7))
    entry_employee_status.set(safe_value(8))

    # Update DateEntry (Start Date)
    start_date = safe_value(9)
    try:
        if start_date:
            entry_employee_startdate.set_date(start_date[:10])  # Set date if valid
        else:
            entry_employee_startdate._set_text('')  # Set default if empty
    except Exception as e:
        print(f"Error setting start date: {e}")
        entry_employee_startdate.set_date('')

    # Update DateEntry (End Date)
    end_date = safe_value(10)
    try:
        if end_date:
            entry_employee_enddate.set_date(end_date[:10])  # Set date if valid
        else:
            entry_employee_enddate._set_text('')  # Set default if empty
    except Exception as e:
        print(f"Error setting start date: {e}")
        entry_employee_enddate.set_date('')

    entry_employee_createdate.config(state="normal")
    entry_employee_createdate.delete(0, tk.END)
    entry_employee_createdate.insert(0, safe_value(11)[:10])
    entry_employee_createdate.config(state="readonly")
    entry_employee_modifieddate.config(state="normal")
    entry_employee_modifieddate.delete(0, tk.END)
    entry_employee_modifieddate.insert(0, safe_value(12)[:10])
    entry_employee_modifieddate.config(state="readonly")

def search_employee():
    # Get search input values
    code = entry_search_code.get().strip()
    first_name = entry_search_firstname.get().strip().lower()
    last_name = entry_search_lastname.get().strip().lower()
    status = entry_search_status.get().strip()

    # Fetch all employees with department and role details
    all_employees = fetch_employees_with_details()

    # Apply filtering
    filtered_employees = []
    for emp in all_employees:
        emp_code, emp_first_name, emp_last_name, emp_status = str(emp[1]), emp[2].lower(), emp[3].lower(), emp[8]

        if (not status or status == emp_status) and \
           (not code or code == emp_code)  and \
           (not first_name or first_name in emp_first_name) and \
           (not last_name or last_name in emp_last_name):
            filtered_employees.append(emp)

    # Clear the Treeview
    for item in tree.get_children():
        tree.delete(item)

    # Insert new data
    for emp in filtered_employees:
        tree.insert("", "end", values=emp)


def add_employee():
    employee_id = uuid.uuid4()
    employee_role = uuid.uuid4()
    employee_code = entry_employee_code.get().strip()
    employee_firstname = entry_employee_firstname.get().strip()
    employee_lastname = entry_employee_lastname.get().strip()
    employee_email = entry_employee_email.get().strip()
    employee_phone = entry_employee_phone.get().strip()
    employee_status = 0
    created_date = datetime.now().strftime('%Y-%m-%d')[:10]  # Convert to string format
    action_date = datetime.now()
    # Fetch and format Start Date
    emp_startdate = entry_employee_startdate.get_date()
    employee_startdate = emp_startdate.strftime('%Y-%m-%d')  # Convert to string format
    # Fetch and format End Date
    emp_enddate = entry_employee_enddate.get_date()
    employee_enddate = emp_enddate.strftime('%Y-%m-%d')  # Convert to string format
    selected_department_name = entry_employee_department.get()  # Get selected department name
    employee_department = [key for key, value in stored_department_dict.items() if value == selected_department_name][0]  # Get ID
    employee_department = uuid.UUID(employee_department)
    selected_role_name = entry_employee_role.get()  # Get selected role name
    employee_role = [key for key, value in stored_role_dict.items() if value == selected_role_name][0]  # Get ID
    employee_role = uuid.UUID(employee_role)

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

        insert_query = "INSERT INTO employee (Id, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, EndDate, CreatedDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        session.execute(insert_query, (employee_id, employee_code, employee_firstname, employee_lastname,employee_email, employee_phone,employee_department,employee_role, employee_status,employee_startdate,employee_enddate, created_date))

        #Insert into history table
        insert_history_query = "INSERT INTO history (Id, Action, ActionDate, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, EndDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        session.execute(insert_history_query, (employee_id, "INSERT", action_date, employee_code, employee_firstname, employee_lastname,employee_email, employee_phone,employee_department,employee_role, employee_status,employee_startdate,employee_enddate))


        messagebox.showinfo("Success", "Employee added successfully!")
        reset_fields()
    except Exception as e:
        messagebox.showerror("Error", f"Error adding employee: {str(e)}")

def edit_employee():
    global selected_item
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a record to edit.")
        return

    employee_code = entry_employee_code.get().strip()
    employee_firstname = entry_employee_firstname.get().strip()
    employee_lastname = entry_employee_lastname.get().strip()
    employee_email = entry_employee_email.get().strip()
    employee_phone = entry_employee_phone.get().strip()
    modified_date = datetime.now().strftime('%Y-%m-%d')[:10]  # Convert to string format
    action_date = datetime.now()
    selected_department_name = entry_employee_department.get()  # Get selected name
    employee_department = [key for key, value in stored_department_dict.items() if value == selected_department_name][0]  # Get ID
    employee_department = uuid.UUID(employee_department)
    selected_role_name = entry_employee_role.get()  # Get selected role name
    employee_role = [key for key, value in stored_role_dict.items() if value == selected_role_name][0]  # Get ID
    employee_role = uuid.UUID(employee_role)
    employee_status = get_status_id(entry_employee_status.get().strip())

    # Fetch and format Start Date
    emp_startdate = entry_employee_startdate.get_date()
    employee_startdate = emp_startdate.strftime('%Y-%m-%d')  # Convert to string format

    # Fetch and format End Date
    emp_enddate = entry_employee_enddate.get_date()
    employee_enddate = emp_enddate.strftime('%Y-%m-%d')  # Convert to string format

    if not employee_code or not employee_firstname:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    try:
        employee_id = uuid.UUID(tree.item(selected_item, "values")[0])  # Convert to UUID
        history_id = uuid.uuid4()
        session = get_cassandra_session()
        query = "UPDATE employee SET EmployeeCode = %s, FirstName = %s, LastName = %s, Email = %s, Phone = %s, DepartmentId = %s, RoleId = %s, Status = %s, StartDate = %s, EndDate = %s, ModifiedDate = %s WHERE Id = %s"
        session.execute(query, (employee_code, employee_firstname,employee_lastname, employee_email, employee_phone, employee_department, employee_role,employee_status, employee_startdate,employee_enddate, modified_date, employee_id))

        #Insert into history table
        insert_history_query = "INSERT INTO history (Id, Action, ActionDate, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, EndDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        session.execute(insert_history_query, (history_id, "UPDATE", action_date, employee_code, employee_firstname, employee_lastname,employee_email, employee_phone,employee_department,employee_role, employee_status,employee_startdate,employee_enddate))


        # show_data_on_grid()
        messagebox.showinfo("Success", "Employee updated successfully!")
        reset_fields()
    except Exception as e:
        messagebox.showerror("Error", f"Error updating employee: {str(e)}")

def show_data_on_grid():
    for item in tree.get_children():
        tree.delete(item)

    for employee in fetch_employees_with_details():
        tree.insert('', 'end', values=employee)

def get_department_dict(only_active=False):
    session = get_cassandra_session()
    if only_active:
        query = "SELECT Id, DepartmentName FROM department WHERE Status = 0 ALLOW FILTERING"
    else:
        query = "SELECT Id, DepartmentName FROM department"
    rows = session.execute(query)
    # Create a dictionary {department_id: department_name}
    return {str(row.id): row.departmentname for row in rows}

def get_role_dict(only_active=False):
    session = get_cassandra_session()
    if only_active:
        query = "SELECT Id, RoleName FROM role WHERE Status = 0 ALLOW FILTERING"
    else:
        query = "SELECT Id, RoleName FROM role"
    rows = session.execute(query)
    # Create a dictionary {role_id: role_name}
    return {str(row.id): row.rolename for row in rows}

def fetch_employees_with_details():
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
    entry_search_code.delete(0, tk.END)
    entry_search_firstname.delete(0, tk.END)
    entry_search_lastname.delete(0, tk.END)
    entry_search_status.set('')
    entry_employee_code.delete(0, tk.END)
    entry_employee_firstname.delete(0, tk.END)
    entry_employee_lastname.delete(0, tk.END)
    entry_employee_phone.delete(0, tk.END)
    entry_employee_email.delete(0, tk.END)
    entry_employee_department.set('')
    entry_employee_role.set('')
    entry_employee_status.set('')
    entry_employee_startdate._set_text('')
    entry_employee_enddate._set_text('')
    entry_employee_createdate.config(state="normal")
    entry_employee_createdate.delete(0, tk.END)
    entry_employee_createdate.config(state="readonly")
    entry_employee_modifieddate.config(state="normal")
    entry_employee_modifieddate.delete(0, tk.END)
    entry_employee_modifieddate.config(state="readonly")
    show_data_on_grid()  # Refresh the grid
