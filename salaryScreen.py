import tkinter as tk
from tkinter import Toplevel

def open_salary_screen(root):
    screen3 = Toplevel(root)
    screen3.title("Salary Management")
    screen3.geometry("700x500")
    # Lấy kích thước của màn hình máy tính
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Lấy kích thước cửa sổ con
    screen3_width = 700
    screen3_height = 500

    # Tính toán tọa độ x và y của cửa sổ con để căn giữa màn hình
    screen3_x = (screen_width - screen3_width) // 2
    screen3_y = (screen_height - screen3_height) // 2

    # Cập nhật vị trí cửa sổ con
    screen3.geometry(f'{screen3_width}x{screen3_height}+{screen3_x}+{screen3_y}')
    label3 = tk.Label(screen3, text="Đây là Màn Hình Salary Management", font=("Arial", 14))
    label3.pack(pady=50)
    button_close3 = tk.Button(screen3, text="Đóng", command=screen3.destroy)
    button_close3.pack(pady=10)
