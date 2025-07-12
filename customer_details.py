from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import os
import subprocess
from db_connection import connect_to_database

# --- Get Arguments or Defaults ---
if len(sys.argv) < 6:
    room_name = "Suite Room S303"
    room_price = "₹5,000 / night"
    image_file = "suite_room.png"
    checkin_date = "2025-07-09"
    checkout_date = "2025-07-10"
else:
    room_name = sys.argv[1]
    room_price = sys.argv[2]
    image_file = sys.argv[3]
    checkin_date = sys.argv[4]
    checkout_date = sys.argv[5]

# --- Setup Window ---
root = Tk()
root.title("Customer Details")
root.geometry("1000x700")
root.configure(bg="white")
root.attributes('-fullscreen', True)

def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

root.bind("<Escape>", exit_fullscreen)

def go_back():
    subprocess.Popen(["python3", "second_page.py"])
    root.after(500, root.destroy)

Button(root, text="← Back", font=("Arial", 15, "bold"), bg="orange", fg="black", command=go_back).place(x=960, y=20)

Label(root, text="Customer Details", font=("Arial", 30, "bold"), fg="teal", bg="white").pack(pady=20)

main_frame = Frame(root, bg="white")
main_frame.pack(padx=40, pady=10, fill=BOTH)

# --- Room Image ---
img = Image.open(image_file)
img = img.resize((300, 200))
room_photo = ImageTk.PhotoImage(img)
Label(main_frame, image=room_photo, bg="white").grid(row=0, column=0, rowspan=5, padx=(0, 40), pady=20)

# --- Room Info Text ---
info = f"Room: {room_name}\nRate: {room_price}\nCheck-in: {checkin_date}\nCheck-out: {checkout_date}"

Label(main_frame, image=room_photo, bg="white").grid(row=0, column=0, rowspan=6, padx=(0, 40), pady=20)
Label(main_frame, text=info, font=("Arial", 16), bg="white", justify=LEFT).grid(row=6, column=0, sticky="nw", padx=(0, 40))


Label(main_frame, text="Full Name: *", font=("Arial", 18), bg="white").grid(row=1, column=1, sticky="e", pady=10)
name_entry = Entry(main_frame,text="Full Name", font=("Arial", 16), width=45)
name_entry.grid(row=1, column=2, sticky="w", padx=5)

Label(main_frame, text="Phone Number: *", font=("Arial", 18), bg="white").grid(row=2, column=1, sticky="e", pady=10)
phone_entry = Entry(main_frame, font=("Arial", 16), width=45)
phone_entry.grid(row=2, column=2, sticky="w", padx=5)

Label(main_frame, text="Email (optional):", font=("Arial", 18), bg="white").grid(row=3, column=1, sticky="e", pady=10)
email_entry = Entry(main_frame, font=("Arial", 16), width=45)
email_entry.grid(row=3, column=2, sticky="w", padx=5)


Label(main_frame, text="Gender: *", font=("Arial", 18), bg="white").grid(row=4, column=1, sticky="e", pady=10)
gender_var = StringVar()
gender_frame = Frame(main_frame, bg="white")
gender_frame.grid(row=4, column=2, sticky="w", padx=5)

for g in ["Male", "Female", "Other"]:
    Radiobutton(gender_frame, text=g, variable=gender_var, value=g, font=("Arial", 12), bg="white").pack(side=LEFT, padx=10)

Label(main_frame, text="State: *", font=("Arial", 18), bg="white").grid(row=5, column=1, sticky="e", pady=10)
states = ["Andhra Pradesh", "Telangana", "Tamil Nadu", "Karnataka", "Kerala", "Maharashtra", "Delhi", "Other"]
state_var = StringVar(value=states[0])
OptionMenu(main_frame, state_var, *states).grid(row=5, column=2, sticky="w", padx=5)

Label(main_frame, text="City: *", font=("Arial", 18), bg="white").grid(row=6, column=1, sticky="e", pady=10)
city_entry = Entry(main_frame, font=("Arial", 16), width=45)
city_entry.grid(row=6, column=2, sticky="w", padx=5)


Label(main_frame, text="Number of Guests: *", font=("Arial", 18), bg="white").grid(row=7, column=1, sticky="e", pady=10)
guests_spinbox = Spinbox(main_frame, from_=1, to=10, font=("Arial", 16), width=10)
guests_spinbox.grid(row=7, column=2, sticky="w", padx=5)


Label(main_frame, text="ID Proof: *", font=("Arial", 18), bg="white").grid(row=8, column=1, sticky="e", pady=10)
id_proof_options = ["Aadhaar Card", "PAN Card", "Passport", "Driving License", "Voter ID", "College ID", "Other"]
id_var = StringVar(value=id_proof_options[0])
OptionMenu(main_frame, id_var, *id_proof_options).grid(row=8, column=2, sticky="w", padx=5)


Label(main_frame, text="ID Number: *", font=("Arial", 18), bg="white").grid(row=9, column=1, sticky="e", pady=10)
id_number_entry = Entry(main_frame, font=("Arial", 16), width=45)
id_number_entry.grid(row=9, column=2, sticky="w", padx=5)


# --- Save Button Logic ---
def save_to_db():
    try:
        name = name_entry.get().strip()
        phone = phone_entry.get().strip()
        email = email_entry.get().strip()
        gender = gender_var.get()
        state = state_var.get()
        city = city_entry.get().strip()
        guests_val = guests_spinbox.get().strip()
        id_proof = id_var.get().strip()
        id_number = id_number_entry.get().strip()

        if not name or not phone or not gender or not guests_val or not id_proof or not id_number:
            messagebox.showwarning("Missing Info", "Please fill all required fields.")
            return

        if not phone.isdigit():
            messagebox.showwarning("Invalid Phone", "Phone number must be numeric.")
            return

        if not guests_val.isdigit():
            messagebox.showwarning("Invalid Guests", "Guests should be a number.")
            return
        if len(phone) != 10 or not phone.isdigit():
            messagebox.showwarning("Invalid Phone", "Phone number must be exactly 10 digits.")
            return

        if email and "@" not in email:
            messagebox.showwarning("Invalid Email", "Please enter a valid email address.")
            return

        if not gender:
            messagebox.showwarning("Missing Info", "Please select a gender.")
            return

        if not all(char.isalpha() or char.isspace() for char in name):
            messagebox.showwarning("Invalid Name", "Name should only contain letters and spaces.")
            return

        db = connect_to_database()
        cursor = db.cursor()

        check_query = """
        SELECT COUNT(*) FROM Bookings
        WHERE room_name = %s AND checkin_date = %s AND checkout_date = %s
        """
        cursor.execute(check_query, (room_name, checkin_date, checkout_date))
        (count,) = cursor.fetchone()

        if count > 0:
            messagebox.showinfo("Already Booked", f"{room_name} is already booked from {checkin_date} to {checkout_date}.")
            return

        insert_query = """
        INSERT INTO Bookings (
            room_name, name, phone_no, email, gender,
            state, city, guests, id_proof, id_number,
            checkin_date, checkout_date, status, created_by
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            room_name, name, int(phone), email, gender,
            state, city, int(guests_val), id_proof, id_number,
            checkin_date, checkout_date, 'active', 1
        )

        cursor.execute(insert_query, values)
        db.commit()

        messagebox.showinfo("Booking Confirmed", f"You have successfully booked {room_name} from {checkin_date} to {checkout_date}")
        book_button.config(state=DISABLED)

    except Exception as e:
        messagebox.showerror("Error", f"Booking failed: {str(e)}")
    finally:
        if db.is_connected():
            cursor.close()
            db.close()

# --- Submit Button ---
book_button = Button(root, text="Book Now", font=("Arial", 20, "bold"), bg="green", fg="black", command=save_to_db)
book_button.pack(pady=30)

root.mainloop()











