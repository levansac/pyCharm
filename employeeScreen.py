import tkinter as tk
from tkinter import Toplevel

def open_employee_screen(root):
    frame = tk.Frame(root, padx=20, pady=20, bd=2, relief="solid")
    frame.pack(padx=3, pady=3, fill="both", expand=True, )
    # Tiêu đề
    label_title = tk.Label(frame, text="Employee Management", font=("Arial", 16, "bold"))
    label_title.grid(row=0, column=0, columnspan=2, pady=10)
    return frame