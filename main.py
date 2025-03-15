import tkinter as tk
from tkinter import Toplevel, messagebox
from employeeScreen import open_employee_screen
from taskScreen import open_task_screen
from salaryScreen import open_salary_screen

# Tạo cửa sổ chính
root = tk.Tk()
root.title("HR Application")
root.geometry("400x400")
root.configure(bg="#f0f0f0")  # Màu nền cửa sổ chính

#Khai báo biến ở đây
txtEmpScreen ="Employee Management"
txtTaskScreen ="Task Management"
txtSalaryScreen ="Salary Management"
txtApplication ="ỨNG DỤNG QUẢN LÝ NHÂN SỰ"

# Tạo menu bar
menu_bar = tk.Menu(root, bg="#333", fg="#fff", font=("Arial", 12))

# Tạo menu cho các màn hình
function_menu = tk.Menu(menu_bar, tearoff=0)
function_menu.add_command(label=txtEmpScreen, command=lambda:open_employee_screen(root))
function_menu.add_command(label=txtTaskScreen, command=lambda: open_task_screen(root))
function_menu.add_command(label=txtSalaryScreen, command=lambda: open_salary_screen(root))

# Thêm menu vào menu bar
menu_bar.add_cascade(label="Menu", menu=function_menu)

# Đặt menu bar cho cửa sổ chính
root.config(menu=menu_bar)

# Thêm một nhãn (Label) vào cửa sổ chính
label = tk.Label(root, text=txtApplication, font=("Arial", 14))
label.pack(pady=20)

# Tạo một frame bên trái để chứa các nút
frame_left = tk.Frame(root, bg="#2c3e50", width=150, height=400)
frame_left.pack(side="left", fill="y")

# Thêm các nút vào frame bên trái
button1 = tk.Button(frame_left, text=txtEmpScreen, command=lambda : open_employee_screen(root), width=20, bg="green", fg="#fff", font=("Arial", 12))
button1.pack(pady=20)

button2 = tk.Button(frame_left, text=txtTaskScreen, command=lambda : open_task_screen(root), width=20, bg="green", fg="#fff", font=("Arial", 12))
button2.pack(pady=20)

button3 = tk.Button(frame_left, text=txtSalaryScreen, command=lambda : open_salary_screen(root), width=20, bg="green", fg="#fff", font=("Arial", 12))
button3.pack(pady=20)



# Thêm một nút để đóng ứng dụng
def close_app():
    if messagebox.askokcancel("Thoát", "Bạn có muốn thoát ứng dụng?"):
        root.quit()

button_exit = tk.Button(root, text="Thoát", command=close_app, bg="#ff6347", font=("Arial", 12, "bold"))
button_exit.place(relx=1.0, rely=1.0, anchor="se", x=-20, y=-20)

# Hiển thị cửa sổ
root.mainloop()
