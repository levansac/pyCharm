import tkinter as tk
from tkinter import Toplevel

# Hàm để mở các màn hình chức năng khác
def open_task_screen(root):
    screen2 = Toplevel(root)
    screen2.title("Task Management")
    screen2.geometry("700x500")

    # Lấy kích thước của màn hình máy tính
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Lấy kích thước cửa sổ con
    screen2_width = 700
    screen2_height = 500

    # Tính toán tọa độ x và y của cửa sổ con để căn giữa màn hình
    screen2_x = (screen_width - screen2_width) // 2
    screen2_y = (screen_height - screen2_height) // 2

    # Cập nhật vị trí cửa sổ con
    screen2.geometry(f'{screen2_width}x{screen2_height}+{screen2_x}+{screen2_y}')

    label2 = tk.Label(screen2, text="Đây là Màn Hình Task Management", font=("Arial", 14))
    label2.pack(pady=50)
    button_close2 = tk.Button(screen2, text="Đóng", command=screen2.destroy)
    button_close2.pack(pady=10)