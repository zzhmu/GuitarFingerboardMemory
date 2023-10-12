import tkinter as tk
import os
import random
from image_path import *
import PIL


class UI:
    def __init__(self, window):
        self.window = window
        self.frame = tk.Frame(self.window)
        self.frame.pack()
        button1 = tk.Button(self.frame, text="音阶识别", command=self.SwitchToScale)
        button1.pack()

        button2 = tk.Button(self.frame, text="退出", command=self.close_window)
        button2.pack()

        self.label = tk.Label(window)
        self.label.pack()

    def close_window(self):
        self.window.destroy()

    def delete_button(self, component):
        component.destroy()

    def SwitchToIni(self):
        self.delete_button(self.frame)
        self.frame = tk.Frame(self.window)
        self.frame.pack()
        button1 = tk.Button(self.frame, text="音阶识别", command=self.SwitchToScale)
        button1.pack()

        button2 = tk.Button(self.frame, text="退出", command=self.close_window)
        button2.pack()

    def SwitchToScale(self):
        self.delete_button(self.frame)
        self.frame = tk.Frame(self.window)
        self.frame.pack()
        button1 = tk.Button(
            self.frame,
            text="大调音阶",
            command=lambda: self.SwitchToImage(majorScales_path),
        )
        button1.pack()
        button2 = tk.Button(
            self.frame,
            text="小调音阶",
            command=lambda: self.SwitchToImage(majorScales_path),
        )
        button2.pack()
        button3 = tk.Button(
            self.frame,
            text="返回",
            command=self.SwitchToIni,
        )
        button3.pack()

    def SwitchToImage(self, path):
        self.delete_button(self.frame)
        self.frame = tk.Frame(self.window)
        self.frame.pack()
        image_files = self.GetImageList(path)
        button1 = tk.Button(
            self.frame,
            text="切换图片",
            command=lambda: self.ChangeImage(image_files, path),
        )

        button1.pack()
        button2 = tk.Button(self.frame, text="返回", command=self.SwitchToScale)

        button2.pack()

    def GetImageList(self, path):
        image_files = [
            file
            for file in os.listdir(path)
            if file.endswith((".jpg", ".jpeg", ".png"))
        ]
        return image_files

    def ChangeImage(self, image_files, path):
        if len(image_files) > 0:
            selected_file = random.choice(image_files)
            file_path = os.path.join(path, selected_file)
            image = PIL.Image.open(file_path)
            scaled_image = image.resize((200, 200))
            photo = PIL.ImageTk.PhotoImage(scaled_image)
            self.label.configure(image=photo)
            self.label.image = photo

    def SwitchButton(root, new_button_text, switch_func):
        # 获取当前按钮所在的父控件和当前按钮
        parent = root.nametowidget(root.winfo_parent())
        current_button = root.master

        # 创建新的按钮
        new_button = tk.Button(parent, text=new_button_text, command=switch_func)

        # 将新按钮添加到父控件
        new_button.pack(side="top")

        # 删除当前按钮
        current_button.destroy()
