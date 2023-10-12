from tkinter import *
import os
from PIL import ImageTk, Image
import random

# 创建窗口
window = Tk()

# 加载图片并调整大小
majorScales_path = "board_image/MajorScales"  # 替换为你的文件夹路径

path = majorScales_path
image_files = [
    file for file in os.listdir(path) if file.endswith((".jpg", ".jpeg", ".png"))
]
if len(image_files) > 0:
    # 随机选择一个图片文件
    selected_file = random.choice(image_files)
    file_path = os.path.join(majorScales_path, selected_file)
image = Image.open(file_path)
scaled_image = image.resize((100, 100))
photo = ImageTk.PhotoImage(scaled_image)
label = Label(window, image=photo)
label.pack()


def button_clicked():
    print("成功")


button = Button(window, text="切换图片", command=button_clicked)
button.pack()

window.mainloop()
