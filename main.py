import tkinter as tk
from tkinter import Toplevel, messagebox
from employeeScreen import open_employee_screen
from roleScreen import open_role_screen
from departmentScreen import open_department_screen

# Function to center the window on the screen
def center_window(window, width, height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the position to center the window
    position_top = int(screen_height / 2 - height / 2)
    position_right = int(screen_width / 2 - width / 2)

    # Set the window geometry (position + width x height)
    window.geometry(f'{width}x{height}+{position_right}+{position_top}')

# Tạo cửa sổ chính
root = tk.Tk()
root.title("HR Application")
root.configure(bg="#f0f0f0")  # Màu nền cửa sổ chính
# Set the desired width and height for the window
window_width = 1300
window_height = 700
# Center the window
center_window(root, window_width, window_height)

#Khai báo biến ở đây
txtEmpScreen ="Employee Management"
txtDepartmentScreen ="Department Management"
txtRoleScreen ="Role Management"
txtApplication ="HUMAN RESOURCE MANAGEMENT APPLICATION"
# Biến toàn cục để lưu Frame Department
isFrameOpen = None

# Tạo một frame bên trái để chứa các nút
frame_left = tk.Frame(root, bg="#2c3e50", width=150, height=400)
frame_left.pack(side="left", fill="y")

# Thêm các nút vào frame bên trái
button1 = tk.Button(frame_left, text=txtEmpScreen, command=lambda : show_screen(txtEmpScreen), width=20, bg="green", fg="#fff", font=("Arial", 12), anchor='w')
button1.pack(pady=20)

button2 = tk.Button(frame_left, text=txtDepartmentScreen, command= lambda : show_screen(txtDepartmentScreen), width=20, bg="green", fg="#fff", font=("Arial", 12), anchor='w')
button2.pack(pady=20)

button3 = tk.Button(frame_left, text=txtRoleScreen, command=lambda : show_screen(txtRoleScreen), width=20, bg="green", fg="#fff", font=("Arial", 12), anchor='w')
button3.pack(pady=20)

def show_screen(menu):
    #close if any exist frame first
    global isFrameOpen
    if isFrameOpen is not None and isFrameOpen.winfo_ismapped():
        isFrameOpen.pack_forget()

    if menu == txtDepartmentScreen:
        isFrameOpen = open_department_screen(root)
    elif menu == txtEmpScreen:
        isFrameOpen = open_employee_screen(root)
    elif menu == txtRoleScreen:
        isFrameOpen = open_role_screen(root)

# Hiển thị cửa sổ
root.mainloop()
