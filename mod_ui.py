import tkinter as tk
import os
import random
from image_path import *
from PIL import Image, ImageTk

# import PIL


class UI:
    def __init__(self, window, canvas):
        self.window = window
        self.canvas = canvas
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
        self.label.image = None
        self.delete_button(self.frame)
        self.frame = tk.Frame(self.window)
        self.frame.pack()
        button1 = tk.Button(
            self.frame,
            text="大调音阶",
            command=lambda: self.SwitchToImage(majorScales_path),
        )
        button1.grid(row=0, column=0)

        button2 = tk.Button(
            self.frame,
            text="小调音阶",
            command=lambda: self.SwitchToImage(minorScales_path),
        )
        button2.grid(row=0, column=1)

        button4 = tk.Button(
            self.frame,
            text="大调五声音阶",
            command=lambda: self.SwitchToImage(majorPenScales_path),
        )
        button4.grid(row=0, column=2)

        button5 = tk.Button(
            self.frame,
            text="小调五声音阶",
            command=lambda: self.SwitchToImage(minorPenScales_path),
        )
        button5.grid(row=0, column=3)

        button6 = tk.Button(
            self.frame,
            text="大调布鲁斯音阶",
            command=lambda: self.SwitchToImage(majorBluesScales_path),
        )
        button6.grid(row=0, column=4)

        button7 = tk.Button(
            self.frame,
            text="大调布鲁斯音阶",
            command=lambda: self.SwitchToImage(minorBluesScales_path),
        )
        button7.grid(row=0, column=5)

        button3 = tk.Button(
            self.frame,
            text="返回",
            command=self.SwitchToIni,
        )
        button3.grid(row=0, column=6)
        # button3.pack()

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
            image = Image.open(file_path)
            self.photo = ImageTk.PhotoImage(image)

            self.canvas.itemconfigure(
                self.canvas.find_withtag("fingerboard"), image=self.photo
            )

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
