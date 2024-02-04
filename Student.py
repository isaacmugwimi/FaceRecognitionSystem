from datetime import datetime
from tkinter import *
from tkinter import ttk

import customtkinter
from PIL import ImageTk, Image


def resize_method(imagePath, imageSize):
    currentImage = Image.open(imagePath)
    resizedImage = currentImage.resize(imageSize)
    return ImageTk.PhotoImage(resizedImage)


font1 = ('consolas', 11,)
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

        self.backButton = customtkinter.CTkButton(self.window, text='Back', command=self.backMethod,
                                                  text_color='#FFFFFF', bg_color="#FFF",
                                                  fg_color='#36719F', height=25, corner_radius=25, width=130,
                                                  cursor='hand2', hover_color='#FF4505', font=('arial', 14))
        self.backButton.place(x=1200, y=135)

        # Images
        image_size = (453, 130)
        self.photoImage = resize_method("images/23.jpg", image_size)
        Label(self.window, image=self.photoImage, text='').place(x=0, y=0)

        image_size = (453, 130)
        self.photoImage4 = resize_method("images/11th.jpg", image_size)
        Label(self.window, image=self.photoImage4, text='').place(x=453, y=0)

        image_size = (453, 130)
        self.photoImage2 = resize_method("images/clg.jpg", image_size)
        Label(self.window, image=self.photoImage2, text='').place(x=906, y=0)

        image_size = (1355, 710)
        self.photoImage3 = resize_method("images/1st.jpg", image_size)
        Label(self.window, image=self.photoImage3, text='').place(x=0, y=160)

        # Main Frame
        # studentMainFrame = Frame(self.window, bg="white", bd=2)

        # details are as follows ...

        # Label Frame
        studentInfoFrame = LabelFrame(self.window, text="Student Information", fg="red", relief=GROOVE,
                                      font=("Arial", 13), bg="white", borderwidth=2,
                                      )

        # Adding images tos the studentInfoFrame

        self.studentPicsFrame = Frame(studentInfoFrame, bg="#FFF", )
        self.studentPicsFrame.place(x=8, y=0, width=685, height=115)

        # ****************** Start of it ****************************
        def studentPicsMethod():
            newSize1 = (170, 120)
            self.studentImage1 = resize_method("images/1st.jpg", newSize1)
            Label(self.studentPicsFrame, image=self.studentImage1, text='').place(x=1, y=1, width=170, height=120)

            newSize2 = (170, 120)
            self.studentImage2 = resize_method("images/5th.jpg", newSize2)
            Label(self.studentPicsFrame, image=self.studentImage2, text='').place(x=171, y=1, width=170, height=120)

            newSize3 = (170, 120)
            self.studentImage3 = resize_method("images/8th.jpg", newSize3)
            Label(self.studentPicsFrame, image=self.studentImage3, text='').place(x=341, y=1, width=170, height=120)

            newSize4 = (170, 120)
            self.studentImage4 = resize_method("images/4th.jpg", newSize4)
            Label(self.studentPicsFrame, image=self.studentImage4, text='').place(x=511, y=1, width=170, height=120)

        studentPicsMethod()  # method which hold the studentImages

        # ********************* End of It *******************************

        # Start for the Current Course Info...
        courseInformationFrame = LabelFrame(studentInfoFrame, text="Current Course Information", fg="Green",
                                            relief=RIDGE,
                                            font=("Arial", 11), bg="white", borderwidth=2
                                            )

        Label(courseInformationFrame, text="Department:", font=font1, fg="Black", bg="white", ).place(x=5, y=3,
                                                                                                      width=100)
        self.departmentDropdown = ttk.Combobox(courseInformationFrame, width=13, font=font2, state="readonly",
                                               textvariable=self.var_department)
        # self.departmentDropdown.set("Select Department Option")
        self.departmentDropdown["values"] = (
            "Select Department Option", "Computer", "IT", "Civil", "Mechanical", "Business", "Education")
        self.departmentDropdown.current(0)
        self.departmentDropdown.place(x=110, y=7, width=200, height=23)

        Label(courseInformationFrame, text="Year:", font=font1, fg="Black", bg="white").place(x=5, y=38, width=100)
        self.yearDropdown = ttk.Combobox(courseInformationFrame, width=13, font=font2, state="readonly",
                                         textvariable=self.var_year)
        # self.yearDropdown.set("Select Year")
        self.yearDropdown["values"] = ("Select Year", "year 1", "year 2", "year 3", "year 4")
        self.yearDropdown.current(0)
        self.yearDropdown.place(x=110, y=41, width=200, height=23)

        Label(courseInformationFrame, text="Course:", font=font1, fg="Black", bg="white", ).place(x=340, y=3, width=100)
        self.courseDropdown = ttk.Combobox(courseInformationFrame, width=13, font=font2, state="readonly",
                                           textvariable=self.var_course)
        # self.courseDropdown.set("Select Course")
        self.courseDropdown["values"] = ("Select Course",
                                         "Computer Science", "Software Engineering", "BIT", "BBIT",
                                         "Computer Science & Maths",
                                         "Financial Engineering")
        self.courseDropdown.current(0)
        self.courseDropdown.place(x=440, y=7, width=200, height=23)

        Label(courseInformationFrame, text="Semester:", font=font1, fg="Black", bg="white", ).place(x=340, y=38,
                                                                                                    width=100)
        self.semesterDropdown = ttk.Combobox(courseInformationFrame, width=13, font=font2, state="readonly",
                                             textvariable=self.var_semester)
        # self.semesterDropdown.set("Select Semester")
        self.semesterDropdown["values"] = ("Select Semester", "Semester 1", "Semester 2", "semester 3")
        self.semesterDropdown.current(0)
        self.semesterDropdown.place(x=440, y=41, width=200, height=23)

        courseInformationFrame.place(x=3, y=120, height=100, width=690)
        # ******************  End of it *********************

        # Start for the Current Course Info...

        studentClassInformationFrame = LabelFrame(studentInfoFrame, text="Student Class Information", fg="Green",
                                                  relief=RIDGE,
                                                  font=("Arial", 11), bg="white", borderwidth=2
                                                  )

        detailsFrame = Frame(studentClassInformationFrame, bg="white")

        # studentIdNo

        studentIdNoLabel = Label(detailsFrame, text="Reg NO:", font=font1, fg="Black", bg="white")
        studentIdNoLabel.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.studentIdNoEntry = customtkinter.CTkEntry(detailsFrame, width=180, font=font3, corner_radius=15,
                                                       bg_color="white", text_color="#000000", height=25,
                                                       textvariable=self.var_regNo)
        self.studentIdNoEntry.grid(row=0, column=1, padx=5, pady=5)

        # class Division
        classDivisionComboboxLabel = Label(detailsFrame, text="Class Division:", font=font1, fg="Black", bg="white")
        classDivisionComboboxLabel.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        self.classDivisionCombobox = ttk.Combobox(detailsFrame, width=22, font=font2, state="readonly",
                                                  textvariable=self.var_classDiv)
        self.classDivisionCombobox["values"] = ("Select Class Division", "Division1", "Division2")
        self.classDivisionCombobox.current(0)
        self.classDivisionCombobox.grid(row=1, column=1, pady=5)

        # Gender
        genderComboboxLabel = Label(detailsFrame, text="Gender:", font=font1, fg="Black", bg="white")
        genderComboboxLabel.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        self.genderCombobox = ttk.Combobox(detailsFrame, width=22, font=font2, state="readonly",
                                           textvariable=self.var_gender)
        self.genderCombobox["values"] = ("Select Gender", "Male", "Female", "Other")
        self.genderCombobox.current(0)
        self.genderCombobox.grid(row=2, column=1, pady=5)

        # Email
        emailLabel = Label(detailsFrame, text="Email:", font=font1, fg="Black", bg="white")
        emailLabel.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        self.emailEntry = customtkinter.CTkEntry(detailsFrame, width=180, font=font3, corner_radius=15,
                                                 bg_color="white", text_color="#000000", height=25,
                                                 textvariable=self.var_email)
        self.emailEntry.grid(row=3, column=1, padx=5, pady=5)

        # Address
        addressLabel = Label(detailsFrame, text="Address:", font=font1, fg="Black", bg="white")
        addressLabel.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        self.addressEntry = customtkinter.CTkEntry(detailsFrame, width=180, font=font3, corner_radius=15,
                                                   bg_color="white", text_color="#000000", height=25,
                                                   textvariable=self.var_address)
        self.addressEntry.grid(row=4, column=1, padx=5, pady=5)

        # Student Name
        studentNameLabel = Label(detailsFrame, text="Student Name:", font=font1, fg="Black", bg="white")
        studentNameLabel.grid(row=0, column=2, padx=15, pady=5, sticky=W)

        self.studentNameEntry = customtkinter.CTkEntry(detailsFrame, width=180, font=font3, corner_radius=15,
                                                       bg_color="white", text_color="#000000", height=25,
                                                       textvariable=self.var_studentName)
        self.studentNameEntry.grid(row=0, column=3, padx=0, pady=5)

        # Roll No.
        studentRollNoLabel = Label(detailsFrame, text="Roll No.", font=font1, fg="Black", bg="white")
        studentRollNoLabel.grid(row=1, column=2, padx=15, pady=5, sticky=W)

        self.studentRollNoEntry = customtkinter.CTkEntry(detailsFrame, width=180, font=font3, corner_radius=15,
                                                         bg_color="white", text_color="#000000", height=25,
                                                         textvariable=self.var_rollNo)
        self.studentRollNoEntry.grid(row=1, column=3, padx=0, pady=5)

        # D.O.B
        studentDobLabel = Label(detailsFrame, text="D.O.B:", font=font1, fg="Black", bg="white")
        studentDobLabel.grid(row=2, column=2, padx=15, pady=5, sticky=W)

        self.studentDobEntry = customtkinter.CTkEntry(detailsFrame, width=180, font=font3, corner_radius=15,
                                                      bg_color="white", text_color="#000000", height=25,
                                                      textvariable=self.var_dob)
        self.studentDobEntry.grid(row=2, column=3, padx=0, pady=5)

        # Phone No.
        studentPhoneLabel = Label(detailsFrame, text="Phone No.", font=font1, fg="Black", bg="white")
        studentPhoneLabel.grid(row=3, column=2, padx=15, pady=5, sticky=W)

        self.studentPhoneEntry = customtkinter.CTkEntry(detailsFrame, width=180, font=font3, corner_radius=15,
                                                        bg_color="white", text_color="#000000", height=25,
                                                        textvariable=self.var_phoneNo)
        self.studentPhoneEntry.grid(row=3, column=3, padx=0, pady=5)

        # Radio Buttons
        photoSampleRadioButton = ttk.Radiobutton(detailsFrame, variable=self.var_radio1, text="Take Photo Sample",
                                                 value=YES)
        photoSampleRadioButton.grid(row=5, column=0, padx=5, pady=5)

        noPhotoSampleRadioButton = ttk.Radiobutton(detailsFrame, text="No Photo Sample", value=NO,
                                                   variable=self.var_radio1)
        noPhotoSampleRadioButton.grid(row=5, column=1, padx=5, pady=5)

        photoSampleRadioButton.configure(takefocus=False)
        noPhotoSampleRadioButton.configure(takefocus=False)

        # ********************* submit buttons ***************************
        self.buttonsFrame = Frame(detailsFrame, bg="white", height=60, width=680, background="white")

        # save button
        self.saveButton = customtkinter.CTkButton(self.buttonsFrame, text='SAVE',
                                                  text_color='#FFFFFF',
                                                  fg_color='#36719F', height=25, corner_radius=25, width=150,
                                                  cursor='hand2', hover_color='#FF4505', font=('arial', 14))
        self.saveButton.grid(row=0, column=0, padx=5, ipadx=5)

        # update button
        self.updateButton = customtkinter.CTkButton(self.buttonsFrame, text='UPDATE',
                                                    text_color='#FFFFFF',
                                                    fg_color='#36719F', height=25, corner_radius=25, width=150,
                                                    cursor='hand2', hover_color='#FF4505', font=('arial', 14))
        self.updateButton.grid(row=0, column=1, padx=5, ipadx=5)

        # deleteButton
        self.deleteButton = customtkinter.CTkButton(self.buttonsFrame, text='DELETE',
                                                    text_color='#FFFFFF',
                                                    fg_color='#36719F', height=25, corner_radius=25, width=150,
                                                    cursor='hand2', hover_color='#FF4505', font=('arial', 14))
        self.deleteButton.grid(row=0, column=2, padx=5, ipadx=5)

        # resetButton
        self.resetButton = customtkinter.CTkButton(self.buttonsFrame, text='RESET',
                                                   text_color='#FFFFFF', command=self.resetMethod,
                                                   fg_color='#36719F', height=25, corner_radius=25, width=150,
                                                   cursor='hand2', hover_color='#FF4505', font=('arial', 14))
        self.resetButton.grid(row=0, column=3, padx=5, ipadx=5)

        # add photo sample button
        self.addSampleButton = customtkinter.CTkButton(self.buttonsFrame, text='ADD PHOTO SAMPLE',
                                                       text_color='#FFFFFF',
                                                       fg_color='#36719F', height=25, corner_radius=25, width=320,
                                                       cursor='hand2', hover_color='#FF4505', font=('arial', 14))
        self.addSampleButton.grid(row=1, column=0, padx=5, ipadx=5, columnspan=2, pady=3)

        # Upload photo sample
        self.uploadSampleButton = customtkinter.CTkButton(self.buttonsFrame, text='UPLOAD PHOTO SAMPLE',
                                                          text_color='#FFFFFF',
                                                          fg_color='#36719F', height=25, corner_radius=25, width=320,
                                                          cursor='hand2', hover_color='#FF4505', font=('arial', 14))
        self.uploadSampleButton.grid(row=1, column=2, padx=5, pady=3, ipadx=5, columnspan=2)

        # ******* End ************

        self.buttonsFrame.place(x=5, y=210)
        detailsFrame.place(x=2, y=3, height=270, width=680)

        studentClassInformationFrame.place(x=3, y=230, height=295, width=690)
        # ***********  End of it *********************

        studentInfoFrame.place(x=13, y=175, height=555, width=700)
        # ********* End **********

        # ******* studentDetails Frame ************
        studentDetailsFrame = LabelFrame(self.window, text="Student Details", fg="red", relief=GROOVE,
                                         font=("Arial", 13), bg="white", borderwidth=2,
                                         )
        newSize = (605, 180)
        self.studentImage6 = resize_method("images/9th.jpg", newSize)
        Label(studentDetailsFrame, text="", bg="blue", image=self.studentImage6).place(x=3, y=2, width=605, height=180)

        # Frame to search student details and input in a table
        searchStudentDetailsFrame = LabelFrame(studentDetailsFrame, text="Search Student Details", fg="green",
                                               relief=GROOVE,
                                               font=("Arial", 13), bg="white", borderwidth=2,
                                               )

        # Search Label
        Label(searchStudentDetailsFrame, text="Search By:", fg="white", bg="Red", font=("Arial", 12, "bold"), ).grid(
            row=0, column=0, padx=5)

        # Search Combo box
        self.courseComboBox = ttk.Combobox(searchStudentDetailsFrame, width=15, font=font2, state="readonly",
                                           textvariable=self.var_searchCourse)
        # self.courseComboBox.set("Select Option")
        self.courseComboBox["values"] = ("Select Option", "Roll No", "Mobile No", "name")
        self.courseComboBox.current(0)
        self.courseComboBox.grid(row=0, column=1, padx=2)

        # Search Entry
        self.searchEntry = customtkinter.CTkEntry(searchStudentDetailsFrame, width=150, font=font3, corner_radius=15,
                                                  bg_color="white", text_color="#000000", height=25,
                                                  textvariable=self.var_searchCourseEntry)
        self.searchEntry.grid(row=0, column=2, padx=5, pady=5)

        # Search Button
        self.searchButton = customtkinter.CTkButton(searchStudentDetailsFrame, text='SEARCH',
                                                    text_color='#FFFFFF',
                                                    fg_color='#36719F', height=25, corner_radius=25, width=50,
                                                    cursor='hand2', hover_color='#FF4505', font=('arial', 12))
        self.searchButton.grid(row=0, column=3, padx=5, ipadx=5)

        # Show All Button
        self.showAllButton = customtkinter.CTkButton(searchStudentDetailsFrame, text='SHOW ALL',
                                                     text_color='#FFFFFF',
                                                     fg_color='#36719F', height=25, corner_radius=25, width=50,
                                                     cursor='hand2', hover_color='#FF4505', font=('arial', 12))
        self.showAllButton.grid(row=0, column=4, padx=5, ipadx=5)

        searchStudentDetailsFrame.place(x=5, y=190, height=60, width=600)
        # *******end of it******

        # Table
        tableFrame = Frame(studentDetailsFrame, relief=GROOVE, bg="white", borderwidth=2, )

        xScrollBar = ttk.Scrollbar(tableFrame, orient=HORIZONTAL)
        yScrollBar = ttk.Scrollbar(tableFrame, orient=VERTICAL)

        style = ttk.Style(self.window)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background='Light green', relief='Flat', font=font2)
        style.configure("Treeview", background='#000', foreground='#FFF', font=font1, fieldbackground='#313837')

        items = ("department", "courses", "year", "semester", "studentID", "studentName", "classDiv",
                 "rollNo", "gender", "d.o.b", "email", "phoneNo", "address", "photo")

        self.table = ttk.Treeview(tableFrame, height=10, xscrollcommand=xScrollBar.set, yscrollcommand=yScrollBar.set)

        xScrollBar.pack(fill=X, side=BOTTOM)
        yScrollBar.pack(fill=Y, side=RIGHT)
        xScrollBar.config(command=self.table.xview)
        yScrollBar.config(command=self.table.yview)
        # self.table["column"] = ("department", "courses", "year", "semester", "studentID", "studentName", "classDiv", 
        #                         "rollNo", "gender", "d.o.b", "email", "phoneNo", "address", "photo")
        self.table["column"] = items

        for i in items:
            self.table.column(i, width=100)

        # self.table.column("#0", width=0, stretch=tk.NO)
        # self.table.column("Department", anchor=tk.CENTER, width=80)
        # self.table.column("Course", anchor=tk.CENTER, width=60)
        # self.table.column("Year", anchor=tk.CENTER, width=60)
        # self.table.column("Semester", anchor=tk.CENTER, width=60)
        # self.table.column("Student ID", anchor=tk.CENTER, width=80)
        # self.table.column("Student Name", anchor=tk.CENTER, width=90)
        # self.table.column("Class Div", anchor=tk.CENTER, width=70)
        # self.table.column("Roll No", anchor=tk.CENTER, width=80)

        self.table.heading("department", text="Department")
        self.table.heading("courses", text="Courses")
        self.table.heading("year", text="Year")
        self.table.heading("semester", text="Semester")
        self.table.heading("studentID", text="Student ID")
        self.table.heading("studentName", text="Student Name")
        self.table.heading("classDiv", text="Class Div")
        self.table.heading("rollNo", text="Roll No")
        self.table.heading("gender", text="Gender")
        self.table.heading("d.o.b", text="D.O.B")
        self.table.heading("email", text="Email")
        self.table.heading("phoneNo", text="Phone NO")
        self.table.heading("address", text="address")
        self.table.heading("photo", text="Photo")
        self.table["show"] = "headings"

        self.table.pack(fill=BOTH, expand=1)
        tableFrame.place(x=5, y=260, height=250, width=600)

        studentDetailsFrame.place(x=725, y=175, height=555, width=620)
        # ********* End **********

        # studentMainFrame.place(x=10, y=172, width=1480, height=600)
        # ******************  End of the MainFrame *********************

    def __init__(self, mainWindow):
        self.backMethod = self.backMethod
        self.backButton = None
        self.courseComboBox = None
        self.resetMethod = self.resetMethod
        self.searchButton = None
        self.searchEntry = None
        self.studentImage6 = None
        self.showAllButton = None
        self.uploadSampleButton = None
        self.studentPhoneEntry = None
        self.addSampleButton = None
        self.saveButton = None
        self.updateButton = None
        self.studentDobEntry = None
        self.studentRollNoEntry = None
        self.studentIdNoEntry = None
        self.studentNameEntry = None
        self.resetButton = None
        self.addressEntry = None
        self.emailEntry = None
        self.classDivisionCombobox = None
        self.table = None
        self.genderCombobox = None
        self.buttonsFrame = None
        self.deleteButton = None
        self.semesterDropdown = None
        self.courseDropdown = None
        self.yearDropdown = None
        self.departmentDropdown = None
        self.studentPicsFrame = None
        self.timeLabel = None
        self.photoImage3 = None
        self.photoImage2 = None
        self.photoImage4 = None
        self.photoImage = None

        # ********************************** variable Declarations ******************************
        self.var_department = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_course = StringVar()
        self.var_regNo = StringVar()
        self.var_classDiv = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_studentName = StringVar()
        self.var_rollNo = StringVar()
        self.var_dob = StringVar()
        self.var_phoneNo = StringVar()
        self.var_searchCourse = StringVar()
        self.var_searchCourseEntry = StringVar()
        self.var_radio1 = StringVar()

        # ********************************** end of variable Declarations *********************

        self.window = mainWindow
        # self.window.overrideredirect(True)
        self.window.geometry("1366x790+-3+1")
        self.window.iconbitmap("images/favicon (2).ico")
        self.window.grab_set()
        self.window.title("Student Management System. Powered by:   ******* Developer Isaac *******")

        self.studentMethod()

        self.window.mainloop()

    # ******************************* buttons functions *********************
    def resetMethod(self):
        self.studentIdNoEntry.delete(0, END)
        self.emailEntry.delete(0, END)
        self.addressEntry.delete(0, END)
        self.studentNameEntry.delete(0, END)
        self.studentRollNoEntry.delete(0, END)
        self.studentDobEntry.delete(0, END)
        self.studentPhoneEntry.delete(0, END)
        self.searchEntry.delete(0, END)

        self.departmentDropdown.current(0)
        self.yearDropdown.current(0)
        self.courseDropdown.current(0)
        self.semesterDropdown.current(0)
        self.classDivisionCombobox.current(0)
        self.genderCombobox.current(0)
        self.courseComboBox.current(0)

        for item in self.table.get_children():
            self.table.delete(item)

    def backMethod(self):
        self.window.destroy()


if __name__ == '__main__':
    root2 = Tk()
    StudentWindow(root2)
