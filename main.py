from image_path import *
import tkinter as tk
import mod_ui
from PIL import Image, ImageTk

# import PIL

# from PIL import Image, ImageTk

window = tk.Tk()
window.title("指板识记")
width = 600
height = 480
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
x = (screenwidth - width) / 22
y = (screenheight - height) / 2
window.geometry("%dx%d+%d+%d" % (width, height, x, y))

background_image = Image.open("shan.jpg")
background_image = ImageTk.PhotoImage(background_image)

guitarboard = Image.open("shan.jpg")
guitarboard = ImageTk.PhotoImage(guitarboard)

canvas = tk.Canvas(window, width=600, height=400)
canvas.pack()
background = canvas.create_image(600, 400, anchor="center", image=background_image)
main_interface = canvas.create_image(
    300, 200, anchor="center", image=guitarboard, tags="fingerboard"
)

ui = mod_ui.UI(window, canvas)

# label = Label(window)
# label.pack()

window.mainloop()
