import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import threading

def shrimp_yes():
    shrimp_window = tk.Toplevel()
    shrimp_window.title("Shrimp Detected")
    shrimp_window.geometry("600x400")

    shrimp_label = tk.Label(shrimp_window, text="Shrimp detected!", font=("Arial", 18))
    shrimp_label.pack(pady=10)

    shrimp_image_path = "shrimp.jpg"
    try:
        shrimp_image = Image.open(shrimp_image_path)
        shrimp_image = shrimp_image.resize((400, 300), Image.LANCZOS)
        shrimp_photo = ImageTk.PhotoImage(shrimp_image)
        img_label = tk.Label(shrimp_window, image=shrimp_photo)
        img_label.image = shrimp_photo
        img_label.pack()
    except FileNotFoundError:
        error_label = tk.Label(shrimp_window, text="Shrimp image not found!", font=("Arial", 14), fg="red")
        error_label.pack(pady=20)

def shrimp_no():
    messagebox.showinfo("No Shrimps Detected", "No shrimps here!")
    def delayed_exit():
        time.sleep(10)
        root.destroy()
    threading.Thread(target=delayed_exit, daemon=True).start()

def show_source_code_alert():
    messagebox.showinfo(
        "Source Code",
        "Extremely Advanced Shrimp Detection Software is too confidential to have its source code leaked.\n"
        "What if shrimps circumvent the code? Just think about that for a second...."
    )

def show_about_info():
    about_window = tk.Toplevel()
    about_window.title("About")
    about_window.geometry("400x200")

    about_text = (
        "Extremely Advanced Shrimp Detection Software\n"
        "Designed for military use by absolute professionals for combatting against shrimps.\n\n"
        "Version 1 and only version, because our system has no flaws."
    )
    about_label = tk.Label(about_window, text=about_text, font=("Arial", 12), justify="center", padx=10, pady=10)
    about_label.pack()

root = tk.Tk()
root.title("Extremely Advanced Shrimp Detection Software")
root.geometry("500x300")

menu_bar = tk.Menu(root)
info_menu = tk.Menu(menu_bar, tearoff=0)
info_menu.add_command(label="Source Code", command=show_source_code_alert)
info_menu.add_command(label="About", command=show_about_info)  # Added "About"
menu_bar.add_cascade(label="Info", menu=info_menu)
root.config(menu=menu_bar)

title_label = tk.Label(root, text="Extremely Advanced Shrimp Detection Software", font=("Arial", 16), pady=10)
title_label.pack()

question_label = tk.Label(root, text="Are you shrimp?", font=("Arial", 14), pady=20)
question_label.pack()

yes_button = tk.Button(root, text="Yes", font=("Arial", 12), command=shrimp_yes)
yes_button.pack(side=tk.LEFT, padx=50, pady=20)

no_button = tk.Button(root, text="No", font=("Arial", 12), command=shrimp_no)
no_button.pack(side=tk.RIGHT, padx=50, pady=20)

root.mainloop()
