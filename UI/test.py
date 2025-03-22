import uuid
import datetime
import tkinter as tk
from tkinter import messagebox
from cassandra.cluster import Cluster


def get_cassandra_session():
    """Function to return a Cassandra session."""
    cluster = Cluster(['127.0.0.1'])  # Update with your Cassandra host
    session = cluster.connect('your_keyspace')  # Replace 'your_keyspace' with your actual keyspace
    return session


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

        # Check if department with the same code exists (optimized)
        check_query = "SELECT DepartmentCode FROM department WHERE DepartmentCode = %s LIMIT 1"
        result = session.execute(check_query, (department_code,))

        if result.one():  # If any row is returned, department already exists
            messagebox.showwarning("Duplicate Entry", "A department with this code already exists!")
            return

        # Get the current date
        created_date = datetime.datetime.now()

        # Insert new department including CreatedDate
        insert_query = """INSERT INTO department (Id, DepartmentCode, DepartmentName, Descriptions, CreatedDate)
                          VALUES (%s, %s, %s, %s, %s)"""
        session.execute(insert_query, (department_id, department_code, department_name, description, created_date))

        # Clear input fields
        entry_department_code.delete(0, tk.END)
        entry_department_name.delete(0, tk.END)
        entry_description.delete(0, tk.END)

        showDataOnGrid()  # Refresh the grid
        messagebox.showinfo("Success", "Department added successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Error adding department: {str(e)}")
