import tkinter as tk
from UI.employeeScreen import open_employee_screen
from UI.roleScreen import open_role_screen
from UI.departmentScreen import open_department_screen
from tkinter import Label  # Explicitly import Label
from tkinter import PhotoImage  # Import PhotoImage if using PNG

# Tạo cửa sổ chính
root = tk.Tk()
root.state('zoomed')
root.title("HR Application")
root.configure(bg="#f0f0f0")  # Màu nền cửa sổ chính

#Khai báo biến ở đây
txtEmpScreen ="Employee Management"
txtDepartmentScreen ="Department Management"
txtRoleScreen ="Role Management"
# Biến toàn cục để lưu Frame Department
isFrameOpen = None

# Tạo một frame bên trái để chứa các nút
frame_left = tk.Frame(root, bg="#2c3e50", width=150, height=400)
frame_left.pack(side="left", fill="y")

# Load an image
image = PhotoImage(file="../photo/logo-hutech.png")
image_label = Label(frame_left, image=image, bg="#2c3e50")
image_label.image = image
image_label.pack()

# Thêm các nút vào frame bên trái
button1 = tk.Button(frame_left, text=txtEmpScreen, command=lambda : show_screen(txtEmpScreen), width=20, bg="green", fg="#fff", font=("Arial", 12), anchor='w')
button1.pack(pady=20)

button2 = tk.Button(frame_left, text=txtDepartmentScreen, command= lambda : show_screen(txtDepartmentScreen), width=20, bg="green", fg="#fff", font=("Arial", 12), anchor='w')
button2.pack(pady=20)

button3 = tk.Button(frame_left, text=txtRoleScreen, command=lambda : show_screen(txtRoleScreen), width=20, bg="green", fg="#fff", font=("Arial", 12), anchor='w')
button3.pack(pady=20)

# Add bottom label
bottom_label = Label(frame_left, text="Made by: vietmy, ngockieng, saclv", fg="white", bg="#2c3e50", font=("Arial", 8, "italic"))
bottom_label.pack(side="bottom", pady=10)  # Place it at the bottom

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
