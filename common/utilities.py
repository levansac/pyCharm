import pandas as pd
from tkinter import filedialog
from tkinter import messagebox

def export_to_excel(tree):
    # Get all items from the Treeview
    rows = []
    for item in tree.get_children():
        rows.append(tree.item(item, "values"))  # Get values from each row

    if not rows:
        messagebox.showwarning("No Data", "There is no data to export.")
        return

    # Convert to Pandas DataFrame
    df = pd.DataFrame(rows, columns=tree['columns'])

    # Ask user for file save location
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                             filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")],
                                             title="Save as")

    if not file_path:  # If user cancels the file dialog
        return

    try:
        # Save DataFrame to Excel
        with pd.ExcelWriter(file_path, engine="xlsxwriter") as writer:
            df.to_excel(writer, sheet_name="Data Exported", index=False)

        messagebox.showinfo("Success", f"Data exported successfully to {file_path}")

    except Exception as e:
        messagebox.showerror("Export Error", f"Failed to export data: {str(e)}")

# Function to Convert Status (0 → "Active", 1 → "Inactive")
def get_status_text(status):
    return "Active" if status == 0 else "Inactive"

# Function to Convert Status ("Active" → 0, "Inactive" → 1)
def get_status_id(status):
    return 1 if status == "Inactive" else 0