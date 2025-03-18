import tkinter as tk
from tkinter import Toplevel, messagebox
from employeeScreen import open_employee_screen
from roleScreen import open_role_screen
from departmentScreen import open_department_screen

# Tạo cửa sổ chính
root = tk.Tk()
root.title("HR Application")
# Mở cửa sổ ở chế độ toàn màn hình
root.attributes("-fullscreen", True)
root.geometry("1100x700")
root.configure(bg="#f0f0f0")  # Màu nền cửa sổ chính

#Khai báo biến ở đây
txtEmpScreen ="Employee Management"
txtDepartmentScreen ="Department Management"
txtRoleScreen ="Role Management"
txtApplication ="ỨNG DỤNG QUẢN LÝ NHÂN SỰ"
# Biến toàn cục để lưu Frame Department
isFrameOpen = None
# Thêm một nút để đóng ứng dụng
def close_app():
    if messagebox.askokcancel("Thoát", "Bạn có muốn thoát ứng dụng?"):
        root.quit()

# Tạo một Frame cho button_exit
frame_exit = tk.Frame(root, bg="#f0f0f0")  # Background giống cửa sổ chính
frame_exit.pack(side="top", anchor="ne", padx=0, pady=2, fill="x")

# Tạo button_exit
button_exit = tk.Button(frame_exit, text="Thoát", command=close_app, bg="#ff6347", font=("Arial", 12, "bold"))
button_exit.pack(side="right")

# Thêm tiêu đề vào frame_title (ở chính giữa)
label_title = tk.Label(frame_exit, text=txtApplication, font=("Arial", 16, "bold"), bg="#f0f0f0")
label_title.pack()

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
