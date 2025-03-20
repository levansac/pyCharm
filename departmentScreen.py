import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import uuid
from cassandra.cluster import Cluster

def open_department_screen(root):
    global frame_department, entry_department_code,entry_department_name, entry_description, tree, selected_item  # Biến toàn cục

    # Initialize selected_item to None
    selected_item = None

    # Tạo một frame cho màn hình quản lý phòng ban
    frame_department = tk.Frame(root, padx=20, pady=20, bd=2, relief="solid", width=1100, height=600, bg="#ecf0f1")
    frame_department.pack(padx=3, pady=3, fill="both", expand=True)

    # Tiêu đề màn hình
    label_title = tk.Label(frame_department, text="Department Management", font=("Arial", 18, "bold"), bg="#ecf0f1")
    label_title.grid(row=0, column=0, columnspan=4, sticky="w", pady=10)

    # Label và Entry for DepartmentCode
    label_department_code = tk.Label(frame_department, text="Code:", font=("Arial", 12), bg="#ecf0f1")
    label_department_code.grid(row=1, column=0, sticky="w")

    entry_department_code = tk.Entry(frame_department, font=("Arial", 12), width=8, relief="groove")
    entry_department_code.grid(row=1, column=1, padx=5)

    # Label và Entry cho tên phòng ban
    label_department_name = tk.Label(frame_department, text="Name:", font=("Arial", 12), bg="#ecf0f1")
    label_department_name.grid(row=1, column=2, padx=5)

    entry_department_name = tk.Entry(frame_department, font=("Arial", 12), width=30, relief="groove")
    entry_department_name.grid(row=1, column=3, padx=5)

    # Label và Entry cho mô tả
    label_description = tk.Label(frame_department, text="Descriptions:", font=("Arial", 12), bg="#ecf0f1")
    label_description.grid(row=1, column=4, padx=5)

    entry_description = tk.Entry(frame_department, font=("Arial", 12), width=40, relief="groove")
    entry_description.grid(row=1, column=5, padx=5)

    # Button Add
    button_add = tk.Button(frame_department, text="Add", font=("Arial", 12), bg="#27ae60", fg="white", bd=2, activebackground="blue",
                   activeforeground="white", highlightthickness=7, relief="raised", command=add_department, cursor="hand2", justify="right")
    button_add.grid(row=1, column=8, sticky="e")

    # Button Edit
    button_edit = tk.Button(frame_department, text="Edit", font=("Arial", 12), bg="#efc497", fg="white", bd=2, activebackground="blue",
                   activeforeground="white", highlightthickness=7, relief="raised", cursor="hand2", justify="right", command=edit_department)
    button_edit.grid(row=3, column=5, padx=10, sticky="e")

    # Button Delete
    button_delete = tk.Button(frame_department, text="Delete", font=("Arial", 12), bg="#f3a0a0", fg="white", bd=2, activebackground="blue",
                   activeforeground="white", highlightthickness=7, relief="raised", cursor="hand2", justify="right", command=delete_department)
    button_delete.grid(row=3, column=8, sticky="e")

    # Function creating treeview
    creatingTreeView()

    return frame_department
#
def creatingTreeView():
    global tree, frame_department, selected_item
    # Create Treeview widget (Grid/Table)
    tree = ttk.Treeview(frame_department, show="headings")

    # Define the columns
    tree['columns'] = ('DepartmentCode', 'DepartmentName', 'Descriptions')  # Adjust column names according to your data

    # Define headings (column names)
    # tree.heading('Id', text='Id')
    tree.heading('DepartmentCode', text='Code')
    tree.heading('DepartmentName', text='Name')
    tree.heading('Descriptions', text='Descriptions')

    # Configure column widths
    # tree.column('Id', width=100, anchor='center')
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
    vsb.grid(row=2, column=9, sticky='ns')  # Place scrollbar at the right of the Treeview
    tree.configure(yscrollcommand=vsb.set)

    # Grid the Treeview widget
    tree.grid(row=2, column=0, columnspan=9, sticky="nsew", pady=5)

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
    selected_item = tree.selection()[0]  # Get selected row ID
    values = tree.item(selected_item, "values")

    # Populate the fields with selected values
    entry_department_code.delete(0, tk.END)
    entry_department_code.insert(0, values[0])

    entry_department_name.delete(0, tk.END)
    entry_department_name.insert(0, values[1])

    entry_description.delete(0, tk.END)
    entry_description.insert(0, values[2])

# Hàm xử lý thao tác thêm phòng ban
def add_department():
    department_code = entry_department_code.get()  # Get department code from the entry field
    department_name = entry_department_name.get()  # Get department name from the entry field
    description = entry_description.get()  # Get description from the entry field

    if department_code and department_name and description:
        try:
            # Connect to Cassandra
            cluster = Cluster(['127.0.0.1'])  # Replace with your Cassandra host/IP
            session = cluster.connect('cassandrakeyspace')  # Replace with your keyspace name

            # Generate a UUID for the department Id
            department_id = uuid.uuid4()

            # Prepare and execute the insert query
            query = """
            INSERT INTO department (Id, DepartmentCode, DepartmentName, Descriptions)
            VALUES (%s, %s, %s, %s)
            """

            # Execute the query with the entered values
            session.execute(query, (department_id, department_code, department_name, description))

            # Clear the fields after inserting the record
            entry_department_code.delete(0, tk.END)
            entry_department_name.delete(0, tk.END)
            entry_description.delete(0, tk.END)

            # Show success message
            messagebox.showinfo("Success", f"Department '{department_name}' added successfully!")

            # Refresh Treeview (grid)
            creatingTreeView()

        except Exception as e:
            # Handle any exceptions (e.g., connection issues, query errors)
            messagebox.showerror("Error", f"An error occurred while adding the department: {str(e)}")

    else:
        # Warn the user if any of the fields are empty
        messagebox.showwarning("Input Error", "Please fill in all fields: Department Code, Name, and Description.")


# Hàm xử lý thao tác xóa phòng ban
def delete_department():
    messagebox.showinfo("Info", "Delete functionality not implemented in this version")

# Hàm xử lý thao tác chỉnh sửa phòng ban
def edit_department():
    global selected_item
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a record to edit.")
        return

    # Retrieve the entered data from the input fields
    department_code = entry_department_code.get()
    department_name = entry_department_name.get()
    description = entry_description.get()

    if not department_code or not department_name or not description:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    try:
        # Get the department Id (UUID) for the selected record from the Treeview tag
        department_id = uuid.UUID(tree.item(selected_item, "tags")[0])  # Convert string to UUID

        if not department_id:
            messagebox.showwarning("Selection Error", "Invalid department selected.")
            return

        # Connect to Cassandra
        cluster = Cluster(['127.0.0.1'])  # Replace with your Cassandra host/IP
        session = cluster.connect('cassandrakeyspace')  # Replace with your keyspace name

        # Prepare the UPDATE query
        query = """
        UPDATE department
        SET DepartmentCode = %s, DepartmentName = %s, Descriptions = %s
        WHERE Id = %s
        """

        # Execute the query to update the record in Cassandra
        session.execute(query, (department_code, department_name, description, department_id))

        # Clear the input fields
        entry_department_code.delete(0, tk.END)
        entry_department_name.delete(0, tk.END)
        entry_description.delete(0, tk.END)

        # Refresh the Treeview with the updated data
        showDataOnGrid()

        # Show success message
        messagebox.showinfo("Success", "Department updated successfully!")

    except Exception as e:
        # If an error occurs, show an error message
        messagebox.showerror("Error", f"An error occurred while updating the department: {str(e)}")


# Function to connect to Cassandra and Fetch Data
def fetch_data_from_cassandra():
    # Connect to the Cassandra cluster and keyspace
    cluster = Cluster(['127.0.0.1'])  # Replace with your Cassandra host/IP
    session = cluster.connect('cassandrakeyspace')  # Replace with your keyspace name

    # Fetch data from your table
    query = "SELECT * FROM department"  # Adjust as necessary
    rows = session.execute(query)

    # Return rows as a list of tuples
    return rows

def showDataOnGrid():
    # Clear the existing data in the Treeview
    for item in tree.get_children():
        tree.delete(item)

    # Fetch data from Cassandra
    data = fetch_data_from_cassandra()

    # Insert data into the Treeview (grid)
    for row in data:
        # Insert each row with department Id as a tag
        department_id = row[0]  # Assuming the department Id (UUID) is in the first column
        # tree.insert('', 'end', values=row, tags=(department_id,))
        tree.insert('', 'end', values=(row[1], row[2], row[3]), tags=(department_id,))