import tkinter
import customtkinter
from datetime import datetime
from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image


def resize_method(imagePath, imageSize):
    currentImage = Image.open(imagePath)
    resizedImage = currentImage.resize(imageSize)
    return ImageTk.PhotoImage(resizedImage)


font1 = ('consolas', 12, 'bold')
font2 = ('consolas', 9)
font3 = ('arial', 12)


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

        # details are as folllows ...

        # Label Frame
        studentDetailsFrame = LabelFrame(studentMainFrame, text="Student Details", fg="red", relief=GROOVE,
                                         font=("Arial", 15), bg="white", borderwidth=2,
                                         )

        # Adding images tos the StudentDetailsFrame

        self.studentPicsFrame = Frame(studentDetailsFrame, bg="#FFF", )
        self.studentPicsFrame.place(x=8, y=0, width=685, height=115)

        # ****************** Start of it ****************************
        def studentPicsMethod():
            newSize = (170, 120)
            self.studentImage1 = resize_method("images/1st.jpg", newSize)
            Label(self.studentPicsFrame, image=self.studentImage1, text='').place(x=1, y=1, width=170, height=120)

            newSize = (170, 120)
            self.studentImage2 = resize_method("images/5th.jpg", newSize)
            Label(self.studentPicsFrame, image=self.studentImage2, text='').place(x=171, y=1, width=170, height=120)

            newSize = (170, 120)
            self.studentImage3 = resize_method("images/8th.jpg", newSize)
            Label(self.studentPicsFrame, image=self.studentImage3, text='').place(x=341, y=1, width=170, height=120)

            newSize = (170, 120)
            self.studentImage4 = resize_method("images/4th.jpg", newSize)
            Label(self.studentPicsFrame, image=self.studentImage4, text='').place(x=511, y=1, width=170, height=120)

        studentPicsMethod()  # method which hold the studentImages

        # ********************* End of It *******************************

        # Start for the Current Course Info...
        courseInformationFrame = LabelFrame(studentDetailsFrame, text="Current Course Information", fg="Green",
                                            relief=RIDGE,
                                            font=("Arial", 11), bg="white", borderwidth=2
                                            )

        Label(courseInformationFrame, text="Department:", font=font1, fg="Black", bg="white", ).place(x=5, y=3,
                                                                                                      width=100)
        self.departmentDropdown = ttk.Combobox(courseInformationFrame, width=13, font=font2)
        self.departmentDropdown.set("Select Option")
        self.departmentDropdown.place(x=110, y=7, width=200, height=23)

        Label(courseInformationFrame, text="Year:", font=font1, fg="Black", bg="white").place(x=5, y=38, width=100)
        self.yearDropdown = ttk.Combobox(courseInformationFrame, width=13, font=font2)
        self.yearDropdown.set("Select Option")
        self.yearDropdown.place(x=110, y=41, width=200, height=23)

        Label(courseInformationFrame, text="Course:", font=font1, fg="Black", bg="white", ).place(x=340, y=3, width=100)
        self.departmentDropdown = ttk.Combobox(courseInformationFrame, width=13, font=font2)
        self.departmentDropdown.set("Select Option")
        self.departmentDropdown.place(x=440, y=7, width=200, height=23)

        Label(courseInformationFrame, text="Semester:", font=font1, fg="Black", bg="white", ).place(x=340, y=38,
                                                                                                    width=100)
        self.departmentDropdown = ttk.Combobox(courseInformationFrame, width=13, font=font2)
        self.departmentDropdown.set("Select Option")
        self.departmentDropdown.place(x=440, y=41, width=200, height=23)

        courseInformationFrame.place(x=3, y=120, height=100, width=690)
        # ******************  End of it *********************

        # Start for the Current Course Info...

        studentClassInformationFrame = LabelFrame(studentDetailsFrame, text="Student Class Information", fg="Green",
                                                  relief=RIDGE,
                                                  font=("Arial", 11), bg="white", borderwidth=2
                                                  )
        scrollbar = Scrollbar(studentClassInformationFrame, orient=VERTICAL)
        canvas = Canvas(studentClassInformationFrame, yscrollcommand=scrollbar.set, bg="white", width=660)

        detailsFrame = Frame(canvas, bg="blue", height=400)
        

        scrollbar.config(command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        

        studentIdNoLabel = Label(detailsFrame, text="Reg NO:", font=font1, fg="Black", bg="white", width=100)
        studentIdNoLabel.place(x=100, y=30)

        self.studentIdNoEntry = customtkinter.CTkEntry(detailsFrame, width=180, font=font3, corner_radius=15, bg_color="white", text_color="#000000", height=30)
        self.studentIdNoEntry.place(x=200, y=30)


        
        

        detailsFrame.place(x=30, y=20, height=400, width=600)

        canvas.create_window((0, 0), window=detailsFrame, anchor="nw", width=680)
        canvas.pack(side="left", fill="both", expand=True)
        # canvas.place(x=0, y=0, )

        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
            

        detailsFrame.bind("<Configure>", on_frame_configure)

        studentClassInformationFrame.place(x=3, y=230, height=295, width=690)
        # ******************  End of it *********************

        studentDetailsFrame.place(x=10, y=3, height=555, width=700)
        studentMainFrame.place(x=10, y=172, width=1480, height=600)

        # ******************  End of the MainFrame *********************

    def __init__(self):
        self.yearDropdown = None
        self.departmentDropdown = None
        self.studentPicsFrame = None
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
