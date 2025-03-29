import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import uuid
from connector.cassandra_connection import CassandraDB
# import datetime
from datetime import datetime
from common.utilities import export_to_excel
from tkcalendar import DateEntry

def open_history_screen(root):
    global stored_role_dict,stored_department_dict, frame_history, entry_employee_code, entry_employee_firstname,\
        entry_employee_lastname,entry_employee_email, tree, selected_item, entry_employee_phone,entry_employee_department,\
        entry_employee_role,entry_employee_status,entry_employee_startdate,entry_employee_enddate,entry_employee_action,\
        entry_employee_actiondate, entry_search_code, entry_search_firstname, entry_search_lastname, entry_search_status

    selected_item = None
    department_dict = get_department_dict()
    department_names = list(department_dict.values())
    stored_department_dict = department_dict

    role_dict = get_role_dict()
    role_names = list(role_dict.values())
    stored_role_dict = role_dict

    frame_history = tk.Frame(root, padx=20, pady=20, bd=2, relief="solid", width=1100, height=600, bg="#ecf0f1")
    frame_history.pack(padx=3, pady=3, fill="both", expand=True)

    label_title = tk.Label(frame_history, text="History", font=("Arial", 12, "bold"), bg="#ecf0f1")
    label_title.grid(row=0, column=0, columnspan=4, sticky="nw")

    search_frame = ttk.LabelFrame(frame_history, text="Search")
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
    details_frame = ttk.LabelFrame(frame_history, text="Details")
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
    entry_employee_startdate = tk.Entry(details_frame, font=("Arial", 12), relief="groove")
    entry_employee_startdate.grid(row=5, column=5)

    label_employee_role = tk.Label(details_frame, text="Role:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_role.grid(row=5, column=6)
    entry_employee_role = ttk.Combobox(details_frame, values=role_names, font=("Arial", 12),state="readonly")
    entry_employee_role.grid(row=5, column=7)
    label_employee_enddate = tk.Label(details_frame, text="End Date:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_enddate.grid(row=6, column=0, pady=10)
    entry_employee_enddate = tk.Entry(details_frame, font=("Arial", 12), relief="groove")
    entry_employee_enddate.grid(row=6, column=1)


    label_employee_action = tk.Label(details_frame, text="Action:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_action.grid(row=6, column=2)
    entry_employee_action = tk.Entry(details_frame, font=("Arial", 12), relief="groove")
    entry_employee_action.grid(row=6, column=3)
    label_employee_actiondate = tk.Label(details_frame, text="Action Date:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_actiondate.grid(row=6, column=4)
    entry_employee_actiondate = tk.Entry(details_frame, font=("Arial", 12), relief="groove")
    entry_employee_actiondate.grid(row=6, column=5)

    label_employee_status = tk.Label(details_frame, text="Status:", font=("Arial", 12), bg="#ecf0f1")
    label_employee_status.grid(row=6, column=6)
    entry_employee_status = ttk.Combobox(details_frame, values=["Active", "Inactive"], font=("Arial", 12), state="readonly")
    entry_employee_status.grid(row=6, column=7)

    button_export = tk.Button(frame_history, text="Export", font=("Arial", 12), bg="#f3a0a0", fg="white", bd=2,
                              activebackground="blue",
                              activeforeground="white", highlightthickness=7, relief="raised", cursor="hand2",
                              justify="right", command=lambda: export_to_excel(tree), height=1, width=6)
    button_export.grid(row=7, column=7, sticky="e", pady=5)

    # Function creating treeview
    creatingTreeView()
    return frame_history

def creatingTreeView():
    global tree, frame_history, selected_item
    # Create Treeview widget (Grid/Table)
    tree = ttk.Treeview(frame_history, show="headings", height=15)

    tree['columns'] = ('Id', 'Action', 'ActionDate', 'EmployeeCode', 'FirstName', 'LastName', 'Email', 'Phone','DepartmentId',
                        'RoleId', 'Status','StartDate', 'EndDate')

    tree.heading('Id', text='Id')  # Hidden column
    tree.heading('Action', text='Action')
    tree.heading('ActionDate', text='ActionDate')
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
    tree.column('Id', width=0, stretch=False)  # Hide the ID column
    tree.column('Action', width=100, anchor='center')
    tree.column('ActionDate', width=150, anchor='center')
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
    vsb = ttk.Scrollbar(frame_history, orient="vertical", command=tree.yview)
    vsb.grid(row=2, column=10, sticky='ns')  # Place scrollbar at the right of the Treeview

    # Horizontal scrollbar
    hsb = ttk.Scrollbar(frame_history, orient="horizontal", command=tree.xview)
    hsb.grid(row=3, column=0, columnspan=10, sticky='ew')
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Grid the Treeview widget
    tree.grid(row=2, column=0, columnspan=10, sticky="nsew", pady=5)

    # Configure row and column weights to make the Treeview expandable
    frame_history.grid_rowconfigure(1, weight=0)
    frame_history.grid_rowconfigure(2, weight=0)
    frame_history.grid_rowconfigure(3, weight=0)
    frame_history.grid_rowconfigure(4, weight=0)
    frame_history.grid_rowconfigure(5, weight=0)
    frame_history.grid_rowconfigure(6, weight=0)
    frame_history.grid_columnconfigure(0, weight=0)
    frame_history.grid_columnconfigure(1, weight=0)
    frame_history.grid_columnconfigure(2, weight=0)
    frame_history.grid_columnconfigure(3, weight=0)
    frame_history.grid_columnconfigure(4, weight=0)
    frame_history.grid_columnconfigure(5, weight=0)
    frame_history.grid_columnconfigure(6, weight=0)
    frame_history.grid_columnconfigure(7, weight=1)
    frame_history.grid_columnconfigure(8, weight=0)
    frame_history.grid_columnconfigure(9, weight=0)
    frame_history.grid_columnconfigure(10, weight=0)

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

    entry_employee_action.delete(0, tk.END)
    entry_employee_action.insert(0, safe_value(1))
    entry_employee_actiondate.delete(0, tk.END)
    entry_employee_actiondate.insert(0, safe_value(2)[:10])
    entry_employee_code.delete(0, tk.END)
    entry_employee_code.insert(0, safe_value(3))
    entry_employee_firstname.delete(0, tk.END)
    entry_employee_firstname.insert(0, safe_value(4))
    entry_employee_lastname.delete(0, tk.END)
    entry_employee_lastname.insert(0, safe_value(5))
    entry_employee_email.delete(0, tk.END)
    entry_employee_email.insert(0, safe_value(6))
    entry_employee_phone.delete(0, tk.END)
    entry_employee_phone.insert(0, safe_value(7))
    entry_employee_department.set(safe_value(8))
    entry_employee_role.set(safe_value(9))
    entry_employee_status.set(safe_value(10))
    entry_employee_startdate.delete(0, tk.END)
    entry_employee_startdate.insert(0, safe_value(11)[:10])
    entry_employee_enddate.delete(0, tk.END)
    entry_employee_enddate.insert(0, safe_value(12)[:10])

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
        emp_code, emp_first_name, emp_last_name, emp_status = str(emp[3]), emp[4].lower(), emp[5].lower(), emp[6]

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

def fetch_employees_with_details():
    session = get_cassandra_session()
    query = "SELECT Id, Action, ActionDate, EmployeeCode, FirstName, LastName, Email, Phone, DepartmentId, RoleId, Status, StartDate, EndDate FROM history"
    rows = session.execute(query)

    # Get department and role dictionaries
    dept_dict = get_department_dict()
    role_dict = get_role_dict()

    employees = []
    for row in rows:
        department_name = dept_dict.get(str(row.departmentid), "Unknown")  # Lookup department name
        role_name = role_dict.get(str(row.roleid), "Unknown")  # Lookup role name
        employees.append((
            str(row.id), row.action, row.actiondate, row.employeecode, row.firstname, row.lastname, row.email,
            row.phone, department_name, role_name, get_status_text(row.status),
            row.startdate, row.enddate
        ))

    # Sort results manually in Python
    employees.sort(key=lambda x: (x[3], x[2]),reverse=True)  # EmployeeCode (index 3), ActionDate (index 2)

    return employees

def get_cassandra_session():
    return CassandraDB().get_session()

def reset_fields():
    entry_employee_action.delete(0, tk.END)
    entry_employee_actiondate.delete(0, tk.END)
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
    entry_employee_startdate.delete(0, tk.END)
    entry_employee_enddate.delete(0, tk.END)
    show_data_on_grid()  # Refresh the grid

# Function to Convert Status (0 → "Active", 1 → "Inactive")
def get_status_text(status):
    return "Active" if status == 0 else "Inactive"

# Function to Convert Status ("Active" → 0, "Inactive" → 1)
def get_status_id(status):
    return 1 if status == "Inactive" else 0
