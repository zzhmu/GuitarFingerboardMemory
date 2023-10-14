from image_path import *
import tkinter as tk
import mod_ui
from PIL import Image, ImageTk

# import PIL

# from PIL import Image, ImageTk

window = tk.Tk()
window.title("指板识记")
width = 300
height = 320
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
x = (screenwidth - width) / 22
y = (screenheight - height) / 2
window.geometry("%dx%d+%d+%d" % (width, height, x, y))

background_image = Image.open("guitar1.png")
background_image = ImageTk.PhotoImage(background_image.resize((200, 200)))

guitarboard = Image.open("guitarboard.png")
guitarboard = ImageTk.PhotoImage(guitarboard.resize((200, 200)))

canvas = tk.Canvas(window, width=500, height=400)
canvas.pack()
background = canvas.create_image(0, 0, anchor="nw", image=background_image)
main_interface = canvas.create_image(
    100, 100, anchor="nw", image=guitarboard, tags="fingerboard"
)

ui = mod_ui.UI(window, canvas)

# label = Label(window)
# label.pack()

window.mainloop()
