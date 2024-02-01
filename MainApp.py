from tkinter import *

from PIL import ImageTk, Image


class Main:
    def resize_method(self, imagePath, imageSize):
        currentImage = Image.open(imagePath)
        resizedImage = currentImage.resize(imageSize)
        return ImageTk.PhotoImage(resizedImage)

    def exitMethod(self):
        self.root.destroy()

    def mainMethod(self):
        image_size = (465, 200)
        self.photoImage = self.resize_method("images/18.webp", image_size)
        Label(self.root, image=self.photoImage, text='').place(x=0, y=0)

        image_size = (465, 170)
        self.photoImage4 = self.resize_method("images/12.webp", image_size)
        Label(self.root, image=self.photoImage4, text='').place(x=465, y=30)

        image_size = (500, 180)
        self.photoImage2 = self.resize_method("images/6th.jpg", image_size)
        Label(self.root, image=self.photoImage2, text='').place(x=930, y=20)

        image_size = (1530, 710)
        self.photoImage3 = self.resize_method("images/26 (2).jpg", image_size)
        Label(self.root, image=self.photoImage3, text='').place(x=0, y=200)

        titleLabel = Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM", fg="Red",
                           font=("Consolas", 25, "bold underline"), bg="cyan")

        titleLabel.place(x=0, y=0, width=1530, height=40)

        # Student Details Button

        image_size = (220, 220)
        self.buttonPhotoImage1 = self.resize_method("images/9th.jpg", image_size)

        self.studentDetailButton1 = Button(self.root, image=self.buttonPhotoImage1, cursor="hand2",
                                           activebackground="blue")
        self.studentDetailButton1.place(x=100, y=230, width=220, height=220)

        self.studentDetailButton = Button(self.root, text='Student Details', cursor="hand2", font=("Consolas", 13),
                                          fg="white", bg="darkblue", activebackground="blue", activeforeground="orange")
        self.studentDetailButton.place(x=99, y=410, width=221, height=40)

        # Face Detector Button

        image_size = (220, 220)
        self.buttonPhotoImage2 = self.resize_method("images/9th.jpg", image_size)

        self.faceDetectorButton1 = Button(self.root, image=self.buttonPhotoImage2, cursor="hand2",
                                          activebackground="blue")
        self.faceDetectorButton1.place(x=420, y=230, width=220, height=220)

        self.faceDetectorButton = Button(self.root, text='Face Detector', cursor="hand2", font=("Consolas", 13),
                                         fg="white", bg="darkblue", activebackground="blue", activeforeground="orange")
        self.faceDetectorButton.place(x=419, y=410, width=221, height=40)

        # Attendance Button

        image_size = (220, 220)
        self.buttonPhotoImage3 = self.resize_method("images/9th.jpg", image_size)

        self.attendanceDetailButton1 = Button(self.root, image=self.buttonPhotoImage3, cursor="hand2",
                                              activebackground="blue")
        self.attendanceDetailButton1.place(x=740, y=230, width=220, height=220)

        self.attendanceDetailButton = Button(self.root, text='Attendance', cursor="hand2", font=("Consolas", 13),
                                             fg="white", bg="darkblue", activebackground="blue",
                                             activeforeground="orange")
        self.attendanceDetailButton.place(x=739, y=410, width=221, height=40)

        # Help Desk Button

        image_size = (220, 220)
        self.buttonPhotoImage4 = self.resize_method("images/9th.jpg", image_size)

        self.helpDeskButton1 = Button(self.root, image=self.buttonPhotoImage4, cursor="hand2", activebackground="blue")
        self.helpDeskButton1.place(x=1060, y=230, width=220, height=220)

        self.helpDeskButton = Button(self.root, text='Help Desk', cursor="hand2", font=("Consolas", 13), fg="white",
                                     bg="darkblue", activebackground="blue", activeforeground="orange")
        self.helpDeskButton.place(x=1059, y=410, width=221, height=40)

        # Train Data Button

        image_size = (220, 220)
        self.buttonPhotoImage5 = self.resize_method("images/9th.jpg", image_size)

        self.trainDataButton1 = Button(self.root, image=self.buttonPhotoImage5, cursor="hand2", activebackground="blue")
        self.trainDataButton1.place(x=100, y=500, width=220, height=220)

        self.trainDataButton = Button(self.root, text='Train', cursor="hand2", font=("Consolas", 13), fg="white",
                                      bg="darkblue", activebackground="blue", activeforeground="orange")
        self.trainDataButton.place(x=99, y=680, width=221, height=40)

        # Student Details Button

        image_size = (220, 220)
        self.buttonPhotoImage6 = self.resize_method("images/9th.jpg", image_size)

        self.photosButton1 = Button(self.root, image=self.buttonPhotoImage6, cursor="hand2", activebackground="blue")
        self.photosButton1.place(x=420, y=500, width=220, height=220)

        self.photosButton = Button(self.root, text='Photos', cursor="hand2", font=("Consolas", 13), fg="white",
                                   bg="darkblue", activebackground="blue", activeforeground="orange")
        self.photosButton.place(x=419, y=680, width=221, height=40)

        # Developer Details Button

        image_size = (220, 220)
        self.buttonPhotoImage7 = self.resize_method("images/9th.jpg", image_size)

        self.developerDetailButton1 = Button(self.root, image=self.buttonPhotoImage7, cursor="hand2",
                                             activebackground="blue")
        self.developerDetailButton1.place(x=740, y=500, width=220, height=220)

        self.developerDetailButton = Button(self.root, text='Developer', cursor="hand2", font=("Consolas", 13),
                                            fg="white", bg="darkblue", activebackground="blue",
                                            activeforeground="orange")
        self.developerDetailButton.place(x=739, y=680, width=221, height=40)

        # Exit Button

        image_size = (220, 220)
        self.buttonPhotoImage8 = self.resize_method("images/9th.jpg", image_size)

        self.exitButton1 = Button(self.root, image=self.buttonPhotoImage8, cursor="hand2", activebackground="blue",
                                  command=lambda: self.exitMethod())
        self.exitButton1.place(x=1060, y=500, width=220, height=220, )

        self.exitButton = Button(self.root, text='Exit', cursor="hand2", font=("Consolas", 13), fg="white",
                                 bg="darkblue", activebackground="blue", activeforeground="orange",
                                 command=self.exitMethod)
        self.exitButton.place(x=1059, y=680, width=221, height=40)

    def __init__(self):
        self.photoImage = None
        self.studentDetailButton1 = None
        self.photoImage3 = None
        self.buttonPhotoImage1 = None
        self.photoImage2 = None
        self.faceDetectorButton = None
        self.faceDetectorButton1 = None
        self.buttonPhotoImage2 = None
        self.buttonPhotoImage4 = None
        self.attendanceDetailButton = None
        self.helpDeskButton1 = None
        self.studentDetailButton = None
        self.photoImage4 = None
        self.attendanceDetailButton1 = None
        self.helpDeskButton = None
        self.trainDataButton = None
        self.trainDataButton1 = None
        self.buttonPhotoImage3 = None
        self.buttonPhotoImage5 = None
        self.photosButton1 = None
        self.buttonPhotoImage6 = None
        self.photosButton = None
        self.developerDetailButton1 = None
        self.buttonPhotoImage7 = None
        self.developerDetailButton = None
        self.buttonPhotoImage8 = None
        self.exitButton1 = None
        self.exitButton = None

        self.root = Tk()
        self.root.mainloop()
        self.root.wm_overrideredirect(True)
        self.root.geometry("1530x790+0+0")
        self.root.iconbitmap("images/favicon (2).ico")
        self.exitMethod = self.exitMethod

        self.mainMethod()


if __name__ == '__main__':
    mainApplication = Main()
