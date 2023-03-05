#!/usr/bin/env python3

# This is a simple wallpaper app, for tiling window managers like i3wm and awesomewm.
# It will also work on openbox if you would like.
# ------------------------------------------------------------------------------
#         MAIN WINDOW
# ------------------------------------------------------------------------------
# This application useses the MIT license

# Importing Third-Party modules
import customtkinter as ctk
from PIL import Image, ImageTk

# Importing Custom modules
from buttons import Buttons
from buttons import *


# Loading the logo
image = CTkImage(Image.open("../logo/argon.png"), size=(200, 200))

# Setting the aprence modes for the for the app
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Creating the window
window = ctk.CTk()

# Setting the window title
window.title("Argon")

# Setting the window size
window.geometry("500x450")

# This is the frame for the images
frame = ctk.CTkFrame(master=window, width=200, height=200).pack(pady=50)

# This is the label for the custom logo
logo = ctk.CTkLabel(master=frame, image=image, text="").place(x=150, y=50)

# This opens your directoies
open_button = ctk.CTkButton(
    master=window, text="Open File", command=Buttons.button_function
).pack(padx=20, pady=20)

# This saves the wallpaper when the computer restarts
save_button = ctk.CTkButton(
    master=window, text="Save File", command=Buttons.save_file
).pack(padx=20, pady=10)

window.mainloop()
