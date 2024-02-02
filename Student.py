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
    def current_time(self):
        obj_date = datetime.now()
        current_time = obj_date.strftime("%H:%M:%S %p")
        self.timeLabel.config(text=f"Time: {current_time}")
        self.timeLabel.after(1000, self.current_time)

    def studentMethod(self):
        titleLabel = Label(self.window, text="STUDENT MANAGEMENT SYSTEM", fg="Green",
                           font=("Consolas", 20, "bold underline"), bg="white")
        titleLabel.place(x=0, y=130, width=1530, height=30)

        timeLabel = Label(self.window, fg="Green", bg="white", font=("Consolas", 18,))
        timeLabel.place(x=10, y=135, width=250, height=27)
        self.timeLabel = timeLabel
        self.current_time()

        # Images
        image_size = (465, 130)
        self.photoImage = resize_method("images/23.jpg", image_size)
        Label(self.window, image=self.photoImage, text='').place(x=0, y=0)

        image_size = (465, 130)
        self.photoImage4 = resize_method("images/11th.jpg", image_size)
        Label(self.window, image=self.photoImage4, text='').place(x=465, y=0)

        image_size = (500, 130)
        self.photoImage2 = resize_method("images/clg.jpg", image_size)
        Label(self.window, image=self.photoImage2, text='').place(x=930, y=0)

        image_size = (1530, 710)
        self.photoImage3 = resize_method("images/1st.jpg", image_size)
        Label(self.window, image=self.photoImage3, text='').place(x=0, y=160)

        # Main Frame
        studentMainFrame = Frame(self.window, bg="white", bd=2)
        studentMainFrame.place(x=10, y=172, width=1480, height=600)

        # Label Frame
        studentDetailsFrame = LabelFrame(studentMainFrame, text="Student Details", fg="red", relief=RIDGE,
                                         font=("Consolas", 18), bg="white", borderwidth=6, highlightbackground="yellow",
                                         highlightthickness=10
                                         )
        studentDetailsFrame.place(x=10, y=10, height=540, width=700)

    def __init__(self):
        self.timeLabel = None
        self.photoImage3 = None
        self.photoImage2 = None
        self.photoImage4 = None
        self.photoImage = None
        self.window = Tk()
        self.window.geometry("1530x790+-3+1")
        self.window.iconbitmap("images/favicon (2).ico")

        self.studentMethod()

        self.window.mainloop()


if __name__ == '__main__':
    StudentWindow()
