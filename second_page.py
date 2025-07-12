
from tkinter import *
from PIL import Image, ImageTk
import subprocess

# --- Function to open Suite page ---
def open_suite_page():
    root.destroy()
    subprocess.run(["python3", "suite_page.py"])  # On Windows, use "python"

# --- Function to open Executive page ---
def open_exec_page():
    root.destroy()
    subprocess.run(["python3", "executive_page.py"])

# --- Setup the main window ---
root = Tk()
root.title("Self Room Booking System")
root.geometry("800x600")
root.configure(bg="white")

# --- Full screen mode ---
root.attributes('-fullscreen', True)

# --- Escape key will exit full screen ---
def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

root.bind("<Escape>", exit_fullscreen)

# --- Heading Text ---
heading = Label(root, text="Welcome", font=("Arial", 35, "bold"), bg="white", fg="green")
heading.pack(pady=10)

sub_heading = Label(root, text="to", font=("Arial", 20), bg="white", fg="green")
sub_heading.pack()

system_title = Label(root, text="Self Room Booking System", font=("Arial", 30, "bold"), bg="white", fg="green")
system_title.pack(pady=10)

# --- Frame for Suite & Executive Buttons ---
button_frame = Frame(root,bg="white")
button_frame.pack(pady=40)

# --- Suite Button ---
suite_button = Button(button_frame, text="Suite", font=("Arial", 20), width=20, height=10, bg="blue", fg="black",
                      command=open_suite_page)
suite_button.pack(side=LEFT, padx=40)

# --- Executive Button ---
executive_button = Button(button_frame, text="Executive", font=("Arial", 20), width=20, height=10, bg="blue", fg="black",
                          command=open_exec_page)
executive_button.pack(side=LEFT, padx=40)

# --- Bottom Frame for Logos ---
bottom_frame = Frame(root,bg="white")
bottom_frame.pack(side="bottom", pady=30)


# INNOVATIONS Logo
innov_img = Image.open("innov.png")
innov_img = innov_img.resize((220, 80))
innov_photo = ImageTk.PhotoImage(innov_img)
Label(bottom_frame, image=innov_photo).pack(side=LEFT, padx=30)

# --- Keep image references alive ---

root.innov_photo = innov_photo

# --- Start the main event loop ---
root.mainloop()






