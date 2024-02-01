from datetime import datetime
from tkinter import *
from tkinter import messagebox
import time

from PIL import ImageTk, Image


def resize_method(imagePath, imageSize):
    currentImage = Image.open(imagePath)
    resizedImage = currentImage.resize(imageSize)
    return ImageTk.PhotoImage(resizedImage)


class StudentWindow:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1530x790+0+0")
        self.window.iconbitmap("images/MainAppImages/favicon (2).ico")

        self.window.mainloop()


if __name__ == '__main__':
    StudentWindow()
