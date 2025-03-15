import tkinter as tk
from tkinter import Toplevel

def open_employee_screen(root):
    screen1 = Toplevel(root)
    screen1.title("Employee Management")
    screen1.geometry("700x500")

    # Lấy kích thước của màn hình máy tính
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Lấy kích thước cửa sổ con
    screen1_width = 700
    screen1_height = 500

    # Tính toán tọa độ x và y của cửa sổ con để căn giữa màn hình
    screen1_x = (screen_width - screen1_width) // 2
    screen1_y = (screen_height - screen1_height) // 2

    # Cập nhật vị trí cửa sổ con
    screen1.geometry(f'{screen1_width}x{screen1_height}+{screen1_x}+{screen1_y}')

    label1 = tk.Label(screen1, text="Đây là Màn Hình Employee Management", font=("Arial", 14))
    label1.pack(pady=50)
    button_close1 = tk.Button(screen1, text="Đóng", command=screen1.destroy)
    button_close1.pack(pady=10)