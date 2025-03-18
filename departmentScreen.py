# import tkinter as tk
# from tkinter import Toplevel
# from tkinter import messagebox
# 
# def open_department_screen(root):
#     # frame = tk.Frame(root, padx=20, pady=20, bd=2, relief="solid")
#     # frame.pack(padx=3, pady=3, fill="both", expand=True,)
#     # # Tiêu đề
#     # label_title = tk.Label(frame, text="Department Management", font=("Arial", 16, "bold"))
#     # label_title.grid(row=0, column=0, columnspan=2, pady=10)
#     # return frame
# 
#     global entry_department, listbox_departments  # Biến toàn cục
# 
#     # Tạo một frame cho màn hình quản lý phòng ban
#     frame_department = tk.Frame(root, padx=20, pady=20, bd=2, relief="solid", width=1100, height=600, bg="#ecf0f1")
#     frame_department.pack(padx=3, pady=3, fill="both", expand=True)
# 
#     # Tiêu đề màn hình
#     label_title = tk.Label(frame_department, text="Department Management", font=("Arial", 18, "bold"), bg="#ecf0f1")
#     label_title.grid(row=0, column=0, columnspan=2, sticky="w")
# 
#     # Label Entry for Department Name
#     label_department = tk.Label(frame_department, text="Department Name:", font=("Arial", 12), bg="#ecf0f1")
#     label_department.grid(row=1, column=0, sticky="w", pady=5)
# 
#     entry_department = tk.Entry(frame_department, font=("Arial", 12), width=50, relief="solid")
#     entry_department.grid(row=1, column=1, pady=5, padx=5)
# 
#     # Label for Descriptions
#     label_department = tk.Label(frame_department, text="Descriptions:", font=("Arial", 12), bg="#ecf0f1")
#     label_department.grid(row=1, column=2, pady=5, padx=5)
# 
#     entry_department = tk.Entry(frame_department, font=("Arial", 12), width=50, relief="solid")
#     entry_department.grid(row=1, column=3, pady=5, padx=5)
# 
#     # Listbox để hiển thị các phòng ban
#     listbox_departments = tk.Listbox(frame_department, font=("Arial", 12), selectmode=tk.SINGLE, relief="solid",
#                                      bg="#ccffff")
#     listbox_departments.grid(row=3, column=0, columnspan=10, pady=10, sticky="ew", padx=5)
# 
#     # Các nút chức năng
#     button_add = tk.Button(frame_department, text="Add Department", font=("Arial", 12), bg="#27ae60", fg="white",
#                            relief="flat", height=2, command=add_department)
#     button_add.grid(row=4, column=0, pady=5, sticky="ew", padx=10)
# 
#     button_edit = tk.Button(frame_department, text="Edit Department", font=("Arial", 12), bg="#f39c12", fg="black",
#                             relief="flat", height=2, command=edit_department)
#     button_edit.grid(row=4, column=1, pady=5, sticky="ew", padx=10)
# 
#     button_delete = tk.Button(frame_department, text="Delete Department", font=("Arial", 12), bg="#e74c3c", fg="white",
#                               relief="flat", height=2, command=delete_department)
#     button_delete.grid(row=4, column=0, columnspan=2, pady=5, padx=10)
#     return frame_department
# 
# # Hàm xử lý thao tác thêm phòng ban
# def add_department():
#     department_name = entry_department.get()
#     if department_name:
#         listbox_departments.insert(tk.END, department_name)
#         entry_department.delete(0, tk.END)  # Xóa text sau khi thêm
#     else:
#         messagebox.showwarning("Warning", "Please enter a department name.")
# 
# # Hàm xử lý thao tác xóa phòng ban
# def delete_department():
#     try:
#         selected_department = listbox_departments.curselection()
#         listbox_departments.delete(selected_department)
#     except IndexError:
#         messagebox.showwarning("Warning", "Please select a department to delete.")
# 
# # Hàm xử lý thao tác chỉnh sửa phòng ban
# def edit_department():
#     try:
#         selected_department = listbox_departments.curselection()
#         old_department_name = listbox_departments.get(selected_department)
#         new_department_name = entry_department.get()
#         if new_department_name:
#             listbox_departments.delete(selected_department)
#             listbox_departments.insert(selected_department, new_department_name)
#             entry_department.delete(0, tk.END)
#         else:
#             messagebox.showwarning("Warning", "Please enter a new department name.")
#     except IndexError:
#         messagebox.showwarning("Warning", "Please select a department to edit.")
import tkinter as tk
from tkinter import messagebox

def open_department_screen(root):
    global entry_department_name, entry_description, listbox_departments  # Biến toàn cục

    # Tạo một frame cho màn hình quản lý phòng ban
    frame_department = tk.Frame(root, padx=20, pady=20, bd=2, relief="solid", width=1100, height=600, bg="#ecf0f1")
    frame_department.pack(padx=3, pady=3, fill="both", expand=True)

    # Tiêu đề màn hình
    label_title = tk.Label(frame_department, text="Department Management", font=("Arial", 18, "bold"), bg="#ecf0f1")
    label_title.grid(row=0, column=0, columnspan=4, sticky="w", pady=10)

    # Label và Entry cho tên phòng ban
    label_department_name = tk.Label(frame_department, text="Department Name:", font=("Arial", 12), bg="#ecf0f1")
    label_department_name.grid(row=1, column=0, sticky="w", pady=5)

    entry_department_name = tk.Entry(frame_department, font=("Arial", 12), width=50, relief="solid")
    entry_department_name.grid(row=1, column=1, pady=5, padx=5)

    # Label và Entry cho mô tả
    label_description = tk.Label(frame_department, text="Description:", font=("Arial", 12), bg="#ecf0f1")
    label_description.grid(row=1, column=2, pady=5, padx=5)

    entry_description = tk.Entry(frame_department, font=("Arial", 12), width=50, relief="solid")
    entry_description.grid(row=1, column=3, pady=5, padx=5)

    # Listbox để hiển thị các phòng ban
    listbox_departments = tk.Listbox(frame_department, font=("Arial", 12), selectmode=tk.SINGLE, relief="solid",
                                     bg="#ccffff")
    listbox_departments.grid(row=2, column=0, columnspan=4, pady=10, sticky="ew", padx=5)

    # Các nút chức năng
    button_add = tk.Button(frame_department, text="Add Department", font=("Arial", 12), bg="#27ae60", fg="white",
                           relief="flat", height=2, command=add_department)
    button_add.grid(row=3, column=0, pady=5, sticky="ew", padx=10)

    button_edit = tk.Button(frame_department, text="Edit Department", font=("Arial", 12), bg="#f39c12", fg="black",
                            relief="flat", height=2, command=edit_department)
    button_edit.grid(row=3, column=1, pady=5, sticky="ew", padx=10)

    button_delete = tk.Button(frame_department, text="Delete Department", font=("Arial", 12), bg="#e74c3c", fg="white",
                              relief="flat", height=2, command=delete_department)
    button_delete.grid(row=4, column=0, columnspan=2, pady=5, padx=10)

    return frame_department

# Hàm xử lý thao tác thêm phòng ban
def add_department():
    department_name = entry_department_name.get()
    description = entry_description.get()
    if department_name and description:
        department_info = f"{department_name} - {description}"
        listbox_departments.insert(tk.END, department_info)
        entry_department_name.delete(0, tk.END)  # Xóa text sau khi thêm
        entry_description.delete(0, tk.END)  # Xóa text sau khi thêm
    else:
        messagebox.showwarning("Warning", "Please enter both department name and description.")

# Hàm xử lý thao tác xóa phòng ban
def delete_department():
    try:
        selected_department = listbox_departments.curselection()
        listbox_departments.delete(selected_department)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a department to delete.")

# Hàm xử lý thao tác chỉnh sửa phòng ban
def edit_department():
    try:
        selected_department = listbox_departments.curselection()
        old_department_info = listbox_departments.get(selected_department)
        old_department_name, old_description = old_department_info.split(" - ")

        # Lấy tên mới và mô tả mới từ Entry
        new_department_name = entry_department_name.get()
        new_description = entry_description.get()

        if new_department_name and new_description:
            new_department_info = f"{new_department_name} - {new_description}"
            listbox_departments.delete(selected_department)
            listbox_departments.insert(selected_department, new_department_info)
            entry_department_name.delete(0, tk.END)
            entry_description.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a new department name and description.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a department to edit.")
