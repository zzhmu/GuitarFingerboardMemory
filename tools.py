import random
import os

from PIL import ImageTk, Image

# import PIL
from tkinter import Label


def ChangeImage(path, window):
    image_files = [
        file for file in os.listdir(path) if file.endswith((".jpg", ".jpeg", ".png"))
    ]
    if len(image_files) > 0:
        selected_file = random.choice(image_files)
        file_path = os.path.join(path, selected_file)
        image = Image.open(file_path)
        scaled_image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(scaled_image)
        label.configure(image=photo)
        label.image = photo
