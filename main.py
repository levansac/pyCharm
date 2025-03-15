import tkinter as tk
from tkinter import Toplevel, messagebox
from employeeScreen import open_employee_screen

# Hàm để mở các màn hình chức năng khác
def open_task_screen():
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

def open_salary_screen():
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

# Tạo cửa sổ chính
root = tk.Tk()
root.title("HR Application")
root.geometry("400x400")
root.configure(bg="#f0f0f0")  # Màu nền cửa sổ chính

#Khai báo biến ở đây
txtEmpScreen ="Employee Management"
txtTaskScreen ="Task Management"
txtSalaryScreen ="Salary Management"

# Tạo menu bar
menu_bar = tk.Menu(root, bg="#333", fg="#fff", font=("Arial", 12))

# Tạo menu cho các màn hình
function_menu = tk.Menu(menu_bar, tearoff=0)
function_menu.add_command(label=txtEmpScreen, command=lambda:open_employee_screen(root))
function_menu.add_command(label=txtTaskScreen, command=open_task_screen)
function_menu.add_command(label=txtSalaryScreen, command=open_salary_screen)

# Thêm menu vào menu bar
menu_bar.add_cascade(label="Menu", menu=function_menu)

# Đặt menu bar cho cửa sổ chính
root.config(menu=menu_bar)

# Thêm một nhãn (Label) vào cửa sổ chính
label = tk.Label(root, text="Chào mừng bạn đến với ứng dụng của tôi!", font=("Arial", 14))
label.pack(pady=20)

# Tạo một frame bên trái để chứa các nút
frame_left = tk.Frame(root, bg="#2c3e50", width=150, height=400)
frame_left.pack(side="left", fill="y")

# Thêm các nút vào frame bên trái
button1 = tk.Button(frame_left, text=txtEmpScreen, command=lambda: open_employee_screen(root), width=20, bg="green", fg="#fff", font=("Arial", 12))
button1.pack(pady=20)

button2 = tk.Button(frame_left, text=txtTaskScreen, command=open_task_screen, width=20, bg="green", fg="#fff", font=("Arial", 12))
button2.pack(pady=20)

button3 = tk.Button(frame_left, text=txtSalaryScreen, command=open_salary_screen, width=20, bg="green", fg="#fff", font=("Arial", 12))
button3.pack(pady=20)



# Thêm một nút để đóng ứng dụng
def close_app():
    if messagebox.askokcancel("Thoát", "Bạn có muốn thoát ứng dụng?"):
        root.quit()

button_exit = tk.Button(root, text="Thoát", command=close_app, bg="#ff6347", font=("Arial", 12, "bold"))
button_exit.pack(pady=20)

# Hiển thị cửa sổ
root.mainloop()
