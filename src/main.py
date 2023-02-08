#!/usr/bin/env python3

# This is a simple wallpaper app, for tiling window managers like i3wm and awesomewm.
# It will also work on openbox if you would like.
# ------------------------------------------------------------------------------
#         MAIN WINDOW
# ------------------------------------------------------------------------------
# This application useses the MIT license

# Importing Third-Party modules
import customtkinter as ctk

# Importing Custom modules
from buttons import Buttons

# Setting the aprence modes for the for the app
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Creating the window
window = ctk.CTk()

# Setting the window title
window.title("Simple Wallpapers")

# Setting the window size
window.geometry("500x400")

# This is the frame for the images
picture_frame = ctk.CTkFrame(master=window, width=350, height=200).pack(pady=50)


# This opens your directoies
open_button = ctk.CTkButton(
    master=window, text="Open Folder", command=Buttons.open_folder
).pack(padx=20, pady=20)

window.mainloop()
