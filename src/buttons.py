# Importing Third_Party module
from customtkinter import filedialog as f
from customtkinter import CTkImage

# Importing Standerd module
import subprocess as sub
from PIL import Image

# Button class
class Buttons:
    def open_folder():
        file_name = f.askopenfilename(
            initialdir="~",
            title="Sclect a File",
            filetypes=(("png files", "*.png"), ("all files", "*.*")),
        )
        command = ["xwallpaper", "--zoom", file_name]
        sub.run(command)

    # TODO: Add a way to add to a image in another funtion
    def add_to_image():
       pass 
