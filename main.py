import tkinter as tk
from tkinter import Toplevel

# Hàm để mở các màn hình chức năng khác
def open_employee_screen():
    screen1 = Toplevel(root)
    screen1.title("Employee Management")
    screen1.geometry("700x700")
    label1 = tk.Label(screen1, text="Đây là Màn Hình 1", font=("Arial", 14))
    label1.pack(pady=50)
    button_close1 = tk.Button(screen1, text="Đóng", command=screen1.destroy)
    button_close1.pack(pady=10)

def open_task_screen():
    screen2 = Toplevel(root)
    screen2.title("Task Management")
    screen2.geometry("400x300")
    label2 = tk.Label(screen2, text="Đây là Màn Hình 2", font=("Arial", 14))
    label2.pack(pady=50)
    button_close2 = tk.Button(screen2, text="Đóng", command=screen2.destroy)
    button_close2.pack(pady=10)

def open_salary_screen():
    screen3 = Toplevel(root)
    screen3.title("Salary Management")
    screen3.geometry("400x300")
    label3 = tk.Label(screen3, text="Đây là Màn Hình 3", font=("Arial", 14))
    label3.pack(pady=50)
    button_close3 = tk.Button(screen3, text="Đóng", command=screen3.destroy)
    button_close3.pack(pady=10)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("HR Application")
root.geometry("700x700")

# Tạo menu bar
menu_bar = tk.Menu(root)

# Tạo menu cho chức năng
function_menu = tk.Menu(menu_bar, tearoff=0)
function_menu.add_command(label="Employee Management", command=open_employee_screen)
function_menu.add_command(label="Task Management", command=open_task_screen)
function_menu.add_command(label="Salary Management", command=open_salary_screen)

# Thêm menu vào menu bar
menu_bar.add_cascade(label="Menu", menu=function_menu)

# Đặt menu bar cho cửa sổ chính
root.config(menu=menu_bar)

# Thêm một nhãn (Label) vào cửa sổ chính
label = tk.Label(root, text="Chào mừng bạn đến với ứng dụng của tôi!", font=("Arial", 14))
label.pack(pady=20)

# Hiển thị cửa sổ
root.mainloop()
