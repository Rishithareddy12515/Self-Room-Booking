from tkinter import *
from datetime import datetime
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import subprocess
from functools import partial
import os
import csv

# --- Initialize Window ---
root = Tk()
root.title("Executive Rooms Available")
root.geometry("800x600")
root.configure(bg="white")

# Full screen mode
root.attributes('-fullscreen', True)

def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

root.bind("<Escape>", exit_fullscreen)

# --- Go Back Function ---
# def go_back():
#     root.destroy()
#     subprocess.run(["python3", "second_page.py"])

def go_back():
    subprocess.Popen(["python3", "second_page.py"])
    root.after(500, root.destroy)


# --- Open Booking Page Function ---
def open_customer_details(room_name, rate, image_file, checkin, checkout):
    root.destroy()
    subprocess.run(["python", "customer_details.py", room_name, rate, image_file, checkin, checkout])

# --- Today's Date ---
today = datetime.today().strftime("%Y-%m-%d")

# --- Title ---
Label(root, text="Executive Rooms Available", font=("Arial", 30, "bold"), fg="teal", bg="white").pack(pady=10)

# --- Filter Frame with Date Range and Back Button ---
filter_frame = Frame(root, bg="white")
filter_frame.pack(pady=5, fill=X)

Button(filter_frame, text="Back", font=("Arial", 15, "bold"),
       bg="red", fg="black", command=go_back).pack(side=RIGHT, padx=20)

Label(filter_frame, text="From Date:", font=("Arial", 12), bg="white", fg="orange").pack(side=LEFT, padx=5)
from_date = DateEntry(filter_frame, font=("Arial", 12), date_pattern='yyyy-mm-dd')
from_date.set_date(today)
from_date.pack(side=LEFT, padx=5)

Label(filter_frame, text="To Date:", font=("Arial", 12), bg="white", fg="orange").pack(side=LEFT, padx=5)
to_date = DateEntry(filter_frame, font=("Arial", 12), date_pattern='yyyy-mm-dd')
to_date.pack(side=LEFT, padx=5)

# --- Room Cards Frame ---
cards_frame = Frame(root, bg="white")
cards_frame.pack(pady=20)

# --- Load Executive Room Image ---
room_img = Image.open("room_sample.png")  # Use executive image
room_img = room_img.resize((160, 110))
room_photo = ImageTk.PhotoImage(room_img)

# --- Executive Rooms List ---
rooms = [
    {"name": "Room E201", "price": "₹3,000 / night"},
    {"name": "Room E202", "price": "₹3,000 / night"},
    {"name": "Room E203", "price": "₹3,000 / night"},
    {"name": "Room E204", "price": "₹3,000 / night"},
    {"name": "Room E205", "price": "₹3,000 / night"},
    {"name": "Room E206", "price": "₹3,000 / night"},
    {"name": "Room E207", "price": "₹3,000 / night"},
    {"name": "Room E208", "price": "₹3,000 / night"},
]

# --- Load Existing Bookings from CSV ---
booked_rooms = set()
if os.path.exists("bookings.csv"):
    with open("bookings.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            key = (row["room_name"], row["checkin_date"], row["checkout_date"])
            booked_rooms.add(key)

# --- Create Room Cards ---
def refresh_rooms():
    for widget in cards_frame.winfo_children():
        widget.destroy()

    for i, room in enumerate(rooms):
        card = Frame(cards_frame, bd=1, relief=SOLID, bg="white", padx=50, pady=40)
        card.grid(row=i // 4, column=i % 4, padx=50, pady=50)

        Label(card, image=room_photo, bg="white").pack()
        Label(card, text=room["name"], font=("Arial", 18, "bold"), bg="white").pack(pady=5)
        Label(card, text=room["price"], font=("Arial", 10), bg="white").pack()

        room_key = (room["name"], from_date.get(), to_date.get())
        is_booked = room_key in booked_rooms

        Button(
            card,
            text="Booked" if is_booked else "Book",
            font=("Arial", 15, "bold"),
            bg="gray" if is_booked else "green",
            fg="black",
            state=DISABLED if is_booked else NORMAL,
            command=partial(
                open_customer_details,
                room["name"],
                room["price"],
                "room_sample.png",
                from_date.get(),
                to_date.get()
            )
        ).pack(pady=5)

# --- Refresh Rooms Initially and on Button ---
refresh_rooms()
Button(filter_frame, text="CHECK ROOMS", font=("Arial", 12, "bold"),
       bg="mediumseagreen", fg="black", command=refresh_rooms).pack(side=LEFT, padx=10)

# --- Prevent Image Garbage Collection ---
root.room_photo = room_photo

root.mainloop()


