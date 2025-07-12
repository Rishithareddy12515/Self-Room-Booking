from tkinter import *
from tkinter import ttk, messagebox
from db_connection import connect_to_database

# --- Main Window ---
root = Tk()
root.title("View All Bookings")
root.geometry("1200x600")
root.configure(bg="white")

Label(root, text="All Bookings", font=("Arial", 24, "bold"), fg="darkblue", bg="white").pack(pady=20)

# --- Frame for Treeview Table ---
tree_frame = Frame(root)
tree_frame.pack(padx=20, pady=10, fill=BOTH, expand=True)

# --- Scrollbars ---
scroll_x = Scrollbar(tree_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(tree_frame, orient=VERTICAL)

# --- Treeview Table Setup ---
columns = (
    "booking_id","room_name", "name", "phone_no", "email", "gender",
    "state", "city", "guests", "id_proof", "id_number",
    "checkin_date", "checkout_date", "status", "created_by"
)



tree = ttk.Treeview(
    tree_frame,
    columns=columns,#aldready have describe it above
    xscrollcommand=scroll_x.set,
    yscrollcommand=scroll_y.set,
    show="headings"
)

scroll_x.config(command=tree.xview)
scroll_y.config(command=tree.yview)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

tree.pack(fill=BOTH, expand=True)

# --- Set Column Headings ---
for col in columns:
    tree.heading(col, text=col.replace("_", " ").title())
    tree.column(col, anchor=CENTER, width=120)

# --- Fetch Data from Database ---
try:
    db = connect_to_database()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM Bookings")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", END, values=row)

except Exception as e:
    messagebox.showerror("Database Error", f"Could not load bookings.\n{str(e)}")

finally:
    if db.is_connected():
        cursor.close()
        db.close()

# --- Run GUI ---
root.mainloop()
