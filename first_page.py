from tkinter import *
from PIL import Image, ImageTk
import subprocess
import time



def go_to_next():
    root.destroy()
    subprocess.run(["python3", "second_page.py"])  # On Windows, we  use "python" instead of "python3"

root = Tk()
root.title("Self Room Booking System")

root.geometry("800x600")
root.configure(bg="white")

# Full screen mode
root.attributes('-fullscreen', True)

# Press ESC to exit full screen
def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

root.bind("<Escape>", exit_fullscreen)


#animated msg
def animated_label():
    message = "Experience Seamless Booking!"
    for i in range(1, len(message) + 1):
        if welcome_label.winfo_exists():
            welcome_label.config(text=message[:i])
            root.update()
            time.sleep(0.05)
        else:
            break


welcome_label = Label(root, text="", font=("Arial", 28, "italic"), bg="#fdf2e9", fg="darkblue")
welcome_label.pack(pady=20)
root.after(1000, animated_label)


# --- Welcome Message ---
Label(root, text="Welcome", font=("Arial", 35, "bold"), bg="#fdf2e9", fg="darkgreen").pack(pady=(40, 0))
Label(root, text="To", font=("Arial", 20), bg="#fdf2e9", fg="darkgreen").pack()
Label(root, text="Self Room Booking System", font=("Arial", 30, "bold"), bg="#fdf2e9", fg="darkgreen").pack(pady=(0, 30))

# --- BOOK NOW Button ---
book_btn = Button(root, text="BOOK NOW", font=("Arial", 20, "bold"), bg="blue", fg="black", padx=50, pady=15,command=go_to_next)
book_btn.pack(pady=20)

# --- Bottom Frame for Logos ---
bottom_frame = Frame(root, bg="white")
bottom_frame.pack(side="bottom", pady=30)

# # INNOVATIONS logo
innov_img = Image.open("innov.png")
innov_img = innov_img.resize((220, 80))
innov_photo = ImageTk.PhotoImage(innov_img)
Label(bottom_frame, image=innov_photo, bg="white").pack(side=LEFT, padx=50)

# --- Keep references ---
root.innov_photo = innov_photo

root.mainloop()