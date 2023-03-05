# Importing the modules needed.
from customtkinter import filedialog
import os

# Button class
class Buttons:
    def button_function():
        global file_name
        # Will open a file dialog for the file you want
        file_name = filedialog.askopenfilename(
            initialdir="~",
            title="Sclect a File",
            filetypes=(("png files", "*.png"), ("all files", "*.*")),
        )
        os.system("xwallpaper --zoom "+file_name) 

    def save_file():
        # This will save it to the bashrc file and write the command to it.
        with open(os.path.expanduser("~/.bashrc"), "a") as file:
            file.writelines("xwallpaper --zoom " + file_name)