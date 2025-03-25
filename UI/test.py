import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry, Calendar
from datetime import datetime

def open_datetime_picker():
    """ Opens a popup with a Date Picker and Time selection. """
    def select_date_time():
        """ Set selected date & time to DateEntry. """
        selected_date = cal.selection_get()
        selected_time = f"{hour_var.get()}:{minute_var.get()}"
        formatted_datetime = f"{selected_date.strftime('%Y-%m-%d')} {selected_time}"
        entry_employee_startdate.delete(0, tk.END)
        entry_employee_startdate.insert(0, formatted_datetime)
        popup.destroy()  # Close popup

    # Create popup window
    popup = tk.Toplevel(root)
    popup.title("Select Date & Time")
    popup.geometry("250x300")
    popup.transient(root)  # Make it modal
    popup.grab_set()  # Focus on popup

    # Add Calendar widget
    cal = Calendar(popup, selectmode="day", date_pattern="yyyy-MM-dd")
    cal.pack(pady=10)

    # Add time selection (Hour & Minute)
    frame_time = ttk.Frame(popup)
    frame_time.pack(pady=5)

    ttk.Label(frame_time, text="Hour:").pack(side="left")
    hour_var = ttk.Combobox(frame_time, values=[f"{i:02d}" for i in range(24)], width=3)
    hour_var.set(datetime.now().strftime("%H"))  # Default to current hour
    hour_var.pack(side="left")

    ttk.Label(frame_time, text=":").pack(side="left")

    ttk.Label(frame_time, text="Minute:").pack(side="left")
    minute_var = ttk.Combobox(frame_time, values=[f"{i:02d}" for i in range(60)], width=3)
    minute_var.set(datetime.now().strftime("%M"))  # Default to current minute
    minute_var.pack(side="left")

    # Confirm Button
    ttk.Button(popup, text="Select", command=select_date_time).pack(pady=10)

# Create main window
root = tk.Tk()
root.title("Employee Management")

# Create DateEntry & bind click event
entry_employee_startdate = DateEntry(root, width=15, background='darkblue', foreground='white', borderwidth=2)
entry_employee_startdate.grid(row=6, column=1, padx=5, pady=5)
entry_employee_startdate.bind("<Button-1>", lambda e: open_datetime_picker())  # Open picker on click

root.mainloop()
