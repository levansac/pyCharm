import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import uuid
from cassandra.cluster import Cluster
from connector.cassandra_connection import CassandraDB
import datetime
from common.utilities import export_to_excel


def open_role_screen(root):
    global frame_role, entry_role_code, entry_role_name, entry_description, tree, selected_item

    selected_item = None

    frame_role = tk.Frame(root, padx=20, pady=20, bd=2, relief="solid", width=1100, height=600, bg="#ecf0f1")
    frame_role.pack(padx=3, pady=3,fill="both", expand=True)

    label_title = tk.Label(frame_role, text="Role Management", font=("Arial", 12, "bold"), bg="#ecf0f1")
    label_title.grid(row=0, column=0, columnspan=4, sticky="nw")

    label_role_code = tk.Label(frame_role, text="Code:", font=("Arial", 12), bg="#ecf0f1")
    label_role_code.grid(row=1, column=0, sticky="w")
    entry_role_code = tk.Entry(frame_role, font=("Arial", 12), relief="groove")
    entry_role_code.grid(row=1,column=1, columnspan=2, sticky="w")
    label_role_name = tk.Label(frame_role, text="Name:", font=("Arial", 12), bg="#ecf0f1")
    label_role_name.grid(row=1, column=3,sticky="e")
    entry_role_name = tk.Entry(frame_role, font=("Arial", 12), relief="groove")
    entry_role_name.grid(row=1, column=4,columnspan=3, sticky="ew")
    button_search = tk.Button(frame_role, text="Search", font=("Arial", 12), bg="#27ae60", fg="white", bd=2, activebackground="blue",
                   activeforeground="white", highlightthickness=7, relief="raised", command=search_role, cursor="hand2", justify="right",height=1,  width=6)
    button_search.grid(row=1,column=7,sticky="e", padx=(0,5))
    button_reset = tk.Button(frame_role, text="Clear", font=("Arial", 12), bg="#27ae60", fg="white", bd=2, activebackground="blue",
                   activeforeground="white", highlightthickness=7, relief="raised", command=reset_fields, cursor="hand2", justify="right", height=1, width=6)
    button_reset.grid(row=1, column=8,sticky="e")

    label_description = tk.Label(frame_role, text="Descriptions:", font=("Arial", 12), bg="#ecf0f1")
    label_description.grid(row=2, column=0, sticky="w")
    entry_description = tk.Entry(frame_role, font=("Arial", 12), relief="groove")
    entry_description.grid(row=2, column=1, columnspan=6, sticky="ew")
    button_add = tk.Button(frame_role, text="Add", font=("Arial", 12), bg="#27ae60", fg="white", bd=2, activebackground="blue",
                   activeforeground="white", highlightthickness=7, relief="raised", command=add_role, cursor="hand2", justify="right",height=1,  width=6)
    button_add.grid(row=2, column=8, sticky="e", pady=(5,0))

    button_export = tk.Button(frame_role, text="Export", font=("Arial", 12), bg="#f3a0a0", fg="white", bd=2,
                              activebackground="blue",
                              activeforeground="white", highlightthickness=7, relief="raised", cursor="hand2",
                              justify="right", command=lambda: export_to_excel(tree), height=1, width=6)
    button_export.grid(row=4, column=6, sticky="e", padx=(0, 5))

    # Button Edit
    button_edit = tk.Button(frame_role, text="Edit", font=("Arial", 12), bg="#efc497", fg="white", bd=2, activebackground="blue",
                   activeforeground="white", highlightthickness=7, relief="raised", cursor="hand2", justify="right", command=edit_role, height=1,  width=6)
    button_edit.grid(row=4, column=7, sticky="e", padx=(0,5))
    button_delete = tk.Button(frame_role, text="Delete", font=("Arial", 12), bg="#f3a0a0", fg="white", bd=2, activebackground="blue",
                   activeforeground="white", highlightthickness=7, relief="raised", cursor="hand2", justify="right", command=delete_role, height=1,  width=6)
    button_delete.grid(row=4, column=8, sticky="e")

    # Function creating treeview
    creatingTreeView()
    return frame_role


def creatingTreeView():
    global tree, frame_role, selected_item
    # Create Treeview widget (Grid/Table)
    tree = ttk.Treeview(frame_role, show="headings", height=12)
    tree['columns'] = ('Id', 'RoleCode', 'RoleName', 'Descriptions', 'CreatedDate', 'ModifiedDate')

    tree.heading('Id', text='Id')  # Hidden column
    tree.heading('RoleCode', text='Code')
    tree.heading('RoleName', text='Name')
    tree.heading('Descriptions', text='Descriptions')
    tree.heading('CreatedDate', text='Created Date')
    tree.heading('ModifiedDate', text='Modified Date')

    tree.column('Id', width=0, stretch=False)  # Hide the ID column
    tree.column('RoleCode', width=100, anchor='center')
    tree.column('RoleName', width=200, anchor='center')
    tree.column('Descriptions', width=300, anchor='center')
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
    vsb = ttk.Scrollbar(frame_role, orient="vertical", command=tree.yview)
    vsb.grid(row=3, column=9, sticky='ns')  # Place scrollbar at the right of the Treeview
    tree.configure(yscrollcommand=vsb.set)

    # Grid the Treeview widget
    tree.grid(row=3, column=0, columnspan=9, sticky="nsew", pady=5)

    # Configure row and column weights to make the Treeview expandable
    frame_role.grid_rowconfigure(1, weight=0)
    frame_role.grid_rowconfigure(2, weight=0)
    frame_role.grid_columnconfigure(0, weight=0)
    frame_role.grid_columnconfigure(1, weight=1)
    frame_role.grid_columnconfigure(2, weight=0)
    frame_role.grid_columnconfigure(3, weight=0)
    frame_role.grid_columnconfigure(4, weight=0)
    frame_role.grid_columnconfigure(5, weight=1)
    frame_role.grid_columnconfigure(6, weight=0)
    frame_role.grid_columnconfigure(7, weight=1)
    frame_role.grid_columnconfigure(8, weight=0)

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

    entry_role_code.delete(0, tk.END)
    entry_role_code.insert(0, values[1])

    entry_role_name.delete(0, tk.END)
    entry_role_name.insert(0, values[2])

    entry_description.delete(0, tk.END)
    entry_description.insert(0, values[3])

def search_role():
    search_code = entry_role_code.get().strip().lower()
    search_name = entry_role_name.get().strip().lower()

    if not search_code and not search_name:
        reset_fields()
        return

    # Clear previous search results
    for item in tree.get_children():
        tree.delete(item)

    try:
        for row in fetch_data_from_cassandra():
            if (search_code and search_code in row.rolecode.lower()) or \
               (search_name and search_name in row.rolename.lower()):
                tree.insert('', 'end', values=(str(row.id), row.rolecode, row.rolename, row.descriptions, row.createddate, row.modifieddate))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def add_role():
    role_id = uuid.uuid4()
    role_code = entry_role_code.get().strip()
    role_name = entry_role_name.get().strip()
    description = entry_description.get().strip()
    created_date = datetime.datetime.now()

    if not role_code or not role_name:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    try:
        session = get_cassandra_session()

        # Check if role with same code exists
        check_query = "SELECT COUNT(*) FROM role WHERE RoleCode = %s"
        result = session.execute(check_query, (role_code,))
        count = result.one()[0]

        if count > 0:
            messagebox.showwarning("Duplicate Entry", "A role with this code already exists!")
            return

        insert_query = "INSERT INTO role (Id, RoleCode, RoleName, Descriptions) VALUES (%s, %s, %s, %s, %s)"
        session.execute(insert_query, (role_id, role_code, role_name, description,created_date))

        entry_role_code.delete(0, tk.END)
        entry_role_name.delete(0, tk.END)
        entry_description.delete(0, tk.END)

        showDataOnGrid()
        messagebox.showinfo("Success", "Role added successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Error adding role: {str(e)}")


def delete_role():
    global selected_item
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a role to delete.")
        return

    try:
        role_id = uuid.UUID(tree.item(selected_item, "values")[0])  # Convert to UUID

        session = get_cassandra_session()
        query = "DELETE FROM role WHERE Id = %s"
        session.execute(query, (role_id,))

        tree.delete(selected_item)
        messagebox.showinfo("Success", "Role deleted successfully!")
        reset_fields()

    except Exception as e:
        messagebox.showerror("Error", f"Error deleting role: {str(e)}")


def edit_role():
    global selected_item
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a record to edit.")
        return

    role_code = entry_role_code.get().strip()
    role_name = entry_role_name.get().strip()
    description = entry_description.get().strip()
    modified_date = datetime.datetime.now()

    if not role_code or not role_name:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    try:
        role_id = uuid.UUID(tree.item(selected_item, "values")[0])  # Convert to UUID

        session = get_cassandra_session()
        query = "UPDATE role SET RoleCode = %s, RoleName = %s, Descriptions = %s, ModifiedDate = %s WHERE Id = %s"
        session.execute(query, (role_code, role_name, description, modified_date, role_id))

        showDataOnGrid()
        messagebox.showinfo("Success", "Role updated successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Error updating role: {str(e)}")


def fetch_data_from_cassandra():
    session = get_cassandra_session()
    query = "SELECT * FROM role"
    return sorted(session.execute(query), key=lambda row: row.rolecode)


def showDataOnGrid():
    for item in tree.get_children():
        tree.delete(item)

    for row in fetch_data_from_cassandra():
        tree.insert('', 'end', values=(str(row.id), row.rolecode, row.rolename, row.descriptions, row.createddate, row.modifieddate))


def get_cassandra_session():
    return CassandraDB().get_session()

def reset_fields():
    entry_role_code.delete(0, tk.END)
    entry_role_name.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    showDataOnGrid()  # Refresh the grid
