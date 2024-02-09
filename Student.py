import re
import tkinter
from datetime import datetime
from tkinter import *
from tkinter import ttk, messagebox
import customtkinter
from PIL import ImageTk, Image
from tkcalendar import DateEntry
import databaseFiles


def resize_method(imagePath, imageSize):
    currentImage = Image.open(imagePath)
    resizedImage = currentImage.resize(imageSize)
    return ImageTk.PhotoImage(resizedImage)


def is_valid_email(email):
    email_regex = (
        r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    )
    return re.match(email_regex, email)


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
                                               textvariable=self.department)
        # self.departmentDropdown.set("Select Department Option")
        self.departmentDropdown["values"] = (
            "Select Department", "Computer", "IT", "Civil", "Mechanical", "Business", "Education")
        self.departmentDropdown.current(0)
        self.departmentDropdown.place(x=110, y=7, width=200, height=23)

        Label(courseInformationFrame, text="Year:", font=font1, fg="Black", bg="white").place(x=5, y=38, width=100)
        self.yearDropdown = ttk.Combobox(courseInformationFrame, width=13, font=font2, state="readonly",
                                         textvariable=self.year)
        # self.yearDropdown.set("Select Year")
        self.yearDropdown["values"] = ("Select Year", "year 1", "year 2", "year 3", "year 4")
        self.yearDropdown.current(0)
        self.yearDropdown.place(x=110, y=41, width=200, height=23)

        Label(courseInformationFrame, text="Course:", font=font1, fg="Black", bg="white", ).place(x=340, y=3, width=100)
        self.courseDropdown = ttk.Combobox(courseInformationFrame, width=13, font=font2, state="readonly",
                                           textvariable=self.course_dropdown)
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
                                             textvariable=self.semester)
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
                                                       textvariable=self.studentIdNo)
        self.studentIdNoEntry.grid(row=0, column=1, padx=5, pady=5)

        # class Division
        classDivisionComboboxLabel = Label(detailsFrame, text="Class Division:", font=font1, fg="Black", bg="white")
        classDivisionComboboxLabel.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        self.classDivisionCombobox = ttk.Combobox(detailsFrame, width=22, font=font2, state="readonly",
                                                  textvariable=self.division)
        self.classDivisionCombobox["values"] = ("Select Class Division", "Division1", "Division2")
        self.classDivisionCombobox.current(0)
        self.classDivisionCombobox.grid(row=1, column=1, pady=5)

        # Gender
        genderComboboxLabel = Label(detailsFrame, text="Gender:", font=font1, fg="Black", bg="white")
        genderComboboxLabel.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        self.genderCombobox = ttk.Combobox(detailsFrame, width=22, font=font2, state="readonly",
                                           textvariable=self.gender)
        self.genderCombobox["values"] = ("Select Gender", "Male", "Female", "Other")
        self.genderCombobox.current(0)
        self.genderCombobox.grid(row=2, column=1, pady=5)

        # Email
        emailLabel = Label(detailsFrame, text="Email:", font=font1, fg="Black", bg="white")
        emailLabel.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        self.emailEntry = customtkinter.CTkEntry(detailsFrame, width=180, font=font3, corner_radius=15,
                                                 bg_color="white", text_color="#000000", height=25,
                                                 )
        self.emailEntry.grid(row=3, column=1, padx=5, pady=5)

        # Address
        addressLabel = Label(detailsFrame, text="Address:", font=font1, fg="Black", bg="white")
        addressLabel.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        self.addressEntry = customtkinter.CTkEntry(detailsFrame, width=180, font=font3, corner_radius=15,
                                                   bg_color="white", text_color="#000000", height=25,
                                                   )
        self.addressEntry.grid(row=4, column=1, padx=5, pady=5)

        # Student Name
        studentNameLabel = Label(detailsFrame, text="Student Name:", font=font1, fg="Black", bg="white")
        studentNameLabel.grid(row=0, column=2, padx=15, pady=5, sticky=W)

        self.studentNameEntry = customtkinter.CTkEntry(detailsFrame, width=180, font=font3, corner_radius=15,
                                                       bg_color="white", text_color="#000000", height=25,
                                                       textvariable=self.studentName)
        self.studentNameEntry.grid(row=0, column=3, padx=0, pady=5)

        # Roll No.
        studentRollNoLabel = Label(detailsFrame, text="Roll No.", font=font1, fg="Black", bg="white")
        studentRollNoLabel.grid(row=1, column=2, padx=15, pady=5, sticky=W)

        self.studentRollNoEntry = customtkinter.CTkEntry(detailsFrame, width=180, font=font3, corner_radius=15,
                                                         bg_color="white", text_color="#000000", height=25,
                                                         textvariable=self.rollNo)
        self.studentRollNoEntry.grid(row=1, column=3, padx=0, pady=5)

        # D.O.B
        studentDobLabel = Label(detailsFrame, text="D.O.B:", font=font1, fg="Black", bg="white")
        studentDobLabel.grid(row=2, column=2, padx=15, pady=5, sticky=W)

        # self.studentDobEntry = customtkinter.CTkEntry(detailsFrame, width=180, font=font3, corner_radius=15,
        #                                               bg_color="white", text_color="#000000", height=25,
        #                                               textvariable=self.dob)

        self.studentDobEntry = DateEntry(detailsFrame, width=25, background='dark blue', height=30,
                                         foreground='white', borderwidth=2, date_pattern='dd-MM-yyyy',
                                         showweeknumbers=False, year=2000,
                                         selectbackground='lightblue', selectforeground='black',
                                         weekendforeground='red')
        self.studentDobEntry.grid(row=2, column=3, padx=0, pady=5)

        # Phone No.
        studentPhoneLabel = Label(detailsFrame, text="Phone No.", font=font1, fg="Black", bg="white")
        studentPhoneLabel.grid(row=3, column=2, padx=15, pady=5, sticky=W)

        self.studentPhoneEntry = customtkinter.CTkEntry(detailsFrame, width=180, font=font3, corner_radius=15,
                                                        bg_color="white", text_color="#000000", height=25,
                                                        textvariable=self.phoneNo)
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
                                                  text_color='#FFFFFF', command=self.saveToDatabaseMethod,
                                                  fg_color='#36719F', height=25, corner_radius=25, width=150,
                                                  cursor='hand2', hover_color='#FF4505', font=('arial', 14))
        self.saveButton.grid(row=0, column=0, padx=5, ipadx=5)

        # update button
        self.updateButton = customtkinter.CTkButton(self.buttonsFrame, text='UPDATE',
                                                    text_color='#FFFFFF', command=self.updateMethod,
                                                    fg_color='#36719F', height=25, corner_radius=25, width=150,
                                                    cursor='hand2', hover_color='#FF4505', font=('arial', 14))
        self.updateButton.grid(row=0, column=1, padx=5, ipadx=5)

        # deleteButton
        self.deleteButton = customtkinter.CTkButton(self.buttonsFrame, text='DELETE',
                                                    text_color='#FFFFFF', command=self.deleteMethod,
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
                                           )
        # self.courseComboBox.set("Select Option")
        self.courseComboBox["values"] = ("Select Option", "Roll No", "Mobile No", "name")
        self.courseComboBox.current(0)
        self.courseComboBox.grid(row=0, column=1, padx=2)

        # Search Entry
        self.searchEntry = customtkinter.CTkEntry(searchStudentDetailsFrame, width=150, font=font3, corner_radius=15,
                                                  bg_color="white", text_color="#000000", height=25,
                                                  )
        self.searchEntry.grid(row=0, column=2, padx=5, pady=5)

        # Search Button
        self.searchButton = customtkinter.CTkButton(searchStudentDetailsFrame, text='SEARCH',
                                                    text_color='#FFFFFF',
                                                    fg_color='#36719F', height=25, corner_radius=25, width=50,
                                                    cursor='hand2', hover_color='#FF4505', font=('arial', 12))
        self.searchButton.grid(row=0, column=3, padx=5, ipadx=5)

        # Show All Button
        self.showAllButton = customtkinter.CTkButton(searchStudentDetailsFrame, text='SHOW ALL',
                                                     text_color='#FFFFFF', command=self.fetchData,
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
        style.configure("Treeview.Heading", background='Light green', font=font2,
                        borderwidth=1, relief="solid", bordercolor="green")
        style.configure("Treeview", background='#000', foreground='#FFF', font=font1, fieldbackground='#313837',
                        )
        style.map("Treeview", background=[("selected", '#1A8F2D')])

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

        # for i in items:
        #     self.table.column(i, width=170)

        for col in (
                "department", "courses", "year", "semester", "studentID", "studentName", "classDiv", "rollNo", "gender",
                "d.o.b", "email", "phoneNo", "address", "photo"):
            self.table.column(col, stretch=NO)

        self.table.column("#0", width=0, stretch=tkinter.NO)
        self.table.column("department", anchor=tkinter.W, width=150)
        self.table.column("courses", anchor=tkinter.W, width=200)
        self.table.column("year", anchor=tkinter.W, width=150)
        self.table.column("semester", anchor=tkinter.W, width=150)
        self.table.column("studentID", anchor=tkinter.W, width=150)
        self.table.column("studentName", anchor=tkinter.W, width=170)
        self.table.column("classDiv", anchor=tkinter.W, width=150)
        self.table.column("rollNo", anchor=tkinter.W, width=100)
        self.table.column("gender", anchor=tkinter.W, width=100)
        self.table.column("d.o.b", anchor=tkinter.W, width=150)
        self.table.column("email", anchor=tkinter.W, width=200)
        self.table.column("phoneNo", anchor=tkinter.W, width=150)
        self.table.column("address", anchor=tkinter.W, width=150)
        self.table.column("photo", anchor=tkinter.W, width=100)

        self.table.heading("department", text="Department", anchor=tkinter.W)
        self.table.heading("courses", text="Courses", anchor=tkinter.W)
        self.table.heading("year", text="Year", anchor=tkinter.W)
        self.table.heading("semester", text="Semester", anchor=tkinter.W)
        self.table.heading("studentID", text="Student ID", anchor=tkinter.W)
        self.table.heading("studentName", text="Student Name", anchor=tkinter.W)
        self.table.heading("classDiv", text="Class Div", anchor=tkinter.W)
        self.table.heading("rollNo", text="Roll No", anchor=tkinter.W)
        self.table.heading("gender", text="Gender", anchor=tkinter.W)
        self.table.heading("d.o.b", text="D.O.B", anchor=tkinter.W)
        self.table.heading("email", text="Email", anchor=tkinter.W)
        self.table.heading("phoneNo", text="Phone NO", anchor=tkinter.W)
        self.table.heading("address", text="Address", anchor=tkinter.W)
        self.table.heading("photo", text="Photo", anchor=tkinter.W)
        self.table["show"] = "headings"

        self.table.bind("<ButtonRelease>", lambda event: self.displayData(event))
        self.table.pack(fill=BOTH, expand=1)
        tableFrame.place(x=5, y=260, height=250, width=600)

        studentDetailsFrame.place(x=725, y=175, height=555, width=620)
        # ********* End **********

        # studentMainFrame.place(x=10, y=172, width=1480, height=600)
        # ******************  End of the MainFrame *********************

        self.studentIdNo = self.studentIdNoEntry.get()
        self.email = self.emailEntry.get()
        self.address = self.addressEntry.get()
        self.studentName = self.studentNameEntry.get()
        self.rollNo = self.studentRollNoEntry.get()
        self.phoneNo = self.studentPhoneEntry.get()
        self.selectedDate = self.studentDobEntry.get_date()

    def __init__(self, mainWindow):
        self.photo = None
        self.displayData = self.displayData
        self.selectedDate = False
        self.course_dropdown = None
        self.searchEntry_variable = None
        self.course = None
        self.gender = None
        self.semester = None
        self.year = None
        self.department = None
        self.division = None
        self.phoneNo = None
        self.email = None
        self.address = None
        self.studentName = None
        self.rollNo = None
        self.studentIdNo = None
        self.saveToDatabaseMethod = self.saveToDatabaseMethod
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
        self.department = StringVar()
        self.year = StringVar()
        self.semester = StringVar()
        self.course_dropdown = StringVar()
        self.division = StringVar()
        self.gender = StringVar()
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
        self.studentDobEntry.set_date("01/01/2000")
        self.studentPhoneEntry.delete(0, END)
        self.searchEntry.delete(0, END)

        self.departmentDropdown.current(0)
        self.yearDropdown.current(0)
        self.courseDropdown.current(0)
        self.semesterDropdown.current(0)
        self.classDivisionCombobox.current(0)
        self.genderCombobox.current(0)
        # self.courseComboBox.current(0)
        for i in self.table.get_children():
            self.table.delete(i)

    def backMethod(self):
        self.window.destroy()

    def saveToDatabaseMethod(self):
        self.studentIdNo = self.studentIdNoEntry.get()
        self.email = self.emailEntry.get()
        self.address = self.addressEntry.get()
        self.studentName = self.studentNameEntry.get()
        self.rollNo = self.studentRollNoEntry.get()
        self.phoneNo = self.studentPhoneEntry.get()
        self.searchEntry_variable = self.searchEntry.get()
        self.selectedDate = self.studentDobEntry.get_date()

        # Data validation before insertion to the database

        if (
                self.departmentDropdown.current() == 0 or
                self.yearDropdown.current() == 0 or
                self.semesterDropdown.current() == 0 or
                self.courseDropdown.current() == 0 or
                self.studentIdNo == '' or
                self.classDivisionCombobox.current() == 0 or
                self.genderCombobox.current() == 0 or
                self.email == '' or
                self.address == '' or
                self.studentName == '' or
                self.rollNo == '' or
                self.phoneNo == ''
        ):
            messagebox.showerror("Error", "Please fill all the fields")
            return

        # regNO checking
        if not self.studentIdNo.isdigit():
            messagebox.showerror("Error", "Student Registration number must be an integer")
            return

        # Email checking
        if not is_valid_email(self.email):
            messagebox.showerror("Error", "Invalid email format")
            return

        #         phone number checking
        if not self.phoneNo.isdigit():
            messagebox.showerror("Error", "Phone number should be a valid integer")
            return

        # roll number checking
        if not self.rollNo.isdigit():
            messagebox.showerror("Error", "Roll number should be a valid integer")
            return

        else:
            try:

                databaseFiles.createTable()

                department = self.department.get()
                course_dropdown = self.course_dropdown.get()
                year = self.year.get()
                semester = self.semester.get()
                studentIdNo = self.studentIdNo
                studentName = self.studentName
                division = self.division.get()
                rollNo = self.rollNo
                gender = self.gender.get()
                selectedDate = self.selectedDate
                email = self.email
                phoneNo = self.phoneNo
                address = self.address
                var_radio = self.var_radio1.get()

                if not databaseFiles.userExists(studentIdNo):
                    self.dataInsertion()

                    databaseFiles.databaseInsertion(department, course_dropdown, year, semester, studentIdNo,
                                                    studentName, division, rollNo, gender, selectedDate, email,
                                                    phoneNo, address, var_radio
                                                    )

                    messagebox.showinfo("Success", "Student details added successfully")
                    self.clearMethod()

                else:
                    messagebox.showerror("Error", "User already exists")

            except Exception as e:
                print(e)
                messagebox.showerror("Error", f"{e}")

    def dataInsertion(self):

        for m in self.table.get_children():
            self.table.delete(m)

        self.table.insert("", "end", values=(self.departmentDropdown.get(),
                                             self.courseDropdown.get(),
                                             self.yearDropdown.get(),
                                             self.semesterDropdown.get(),
                                             self.studentIdNoEntry.get(),
                                             self.studentNameEntry.get(),
                                             self.classDivisionCombobox.get(),
                                             self.studentRollNoEntry.get(),
                                             self.genderCombobox.get(),
                                             self.selectedDate,
                                             self.emailEntry.get(),
                                             self.studentPhoneEntry.get(),
                                             self.addressEntry.get(),
                                             self.var_radio1.get()
                                             ))

    def clearMethod(self):
        self.studentIdNoEntry.delete(0, END)
        self.emailEntry.delete(0, END)
        self.addressEntry.delete(0, END)
        self.studentNameEntry.delete(0, END)
        self.studentRollNoEntry.delete(0, END)
        self.studentDobEntry.delete(0, END)
        self.studentDobEntry.set_date("01/01/2000")

        self.studentPhoneEntry.delete(0, END)
        self.searchEntry.delete(0, END)

        self.departmentDropdown.current(0)
        self.yearDropdown.current(0)
        self.courseDropdown.current(0)
        self.semesterDropdown.current(0)
        self.classDivisionCombobox.current(0)
        self.genderCombobox.current(0)
        self.courseComboBox.current(0)

    def displayData(self, event):

        selected_item = self.table.focus()
        if selected_item:
            row = self.table.item(selected_item)['values']
            self.clearMethod()
            self.studentDobEntry.delete(0, END)
            self.department.set(row[0]),
            self.course_dropdown.set(row[1]),
            self.year.set(row[2]),
            self.semester.set(row[3]),
            self.studentIdNoEntry.insert(0, row[4]),
            self.studentNameEntry.insert(0, row[5]),
            self.division.set(row[6]),
            self.studentRollNoEntry.insert(0, row[7]),
            self.gender.set(row[8]),
            self.studentDobEntry.insert(0, row[9]),
            self.emailEntry.insert(0, row[10]),
            self.studentPhoneEntry.insert(0, row[11]),
            self.addressEntry.insert(0, row[12]),
            self.var_radio1.set(row[13])

    def fetchData(self):
        data = databaseFiles.fetchingData()
        if len(data) != 0:
            self.table.delete(*self.table.get_children())
            for i in data:
                self.table.insert("", END, values=i)

    def updateMethod(self):

        # Extracting values from the entry widgets and other controls
        department = self.department.get()
        course_dropdown = self.course_dropdown.get()
        year = self.year.get()
        semester = self.semester.get()
        studentIdNo = self.studentIdNoEntry.get()

        studentName = self.studentNameEntry.get()
        division = self.division.get()
        rollNo = self.studentRollNoEntry.get()
        gender = self.gender.get()
        selectedDate = self.selectedDate
        email = self.emailEntry.get()
        phoneNo = self.studentPhoneEntry.get()
        address = self.addressEntry.get()
        var_radio = self.var_radio1.get()

        # Getting the selected item in the table
        selectedItem = self.table.focus()

        if not selectedItem:
            messagebox.showerror("Error", "Choose a student to update")

        else:
            try:
                self.studentIdNo = self.studentIdNoEntry.get()
                self.email = self.emailEntry.get()
                self.address = self.addressEntry.get()
                self.studentName = self.studentNameEntry.get()
                self.rollNo = self.studentRollNoEntry.get()
                self.phoneNo = self.studentPhoneEntry.get()
                self.searchEntry_variable = self.searchEntry.get()
                self.selectedDate = self.studentDobEntry.get_date()

                # Data validation before insertion to the database

                if (
                        self.departmentDropdown.current() == 0 or
                        self.yearDropdown.current() == 0 or
                        self.semesterDropdown.current() == 0 or
                        self.courseDropdown.current() == 0 or
                        self.studentIdNo == '' or
                        self.classDivisionCombobox.current() == 0 or
                        self.genderCombobox.current() == 0 or
                        self.email == '' or
                        self.address == '' or
                        self.studentName == '' or
                        self.rollNo == '' or
                        self.phoneNo == ''
                ):
                    messagebox.showerror("Error", "Please fill all the fields")
                    return

                # regNO checking
                if not self.studentIdNo.isdigit():
                    messagebox.showerror("Error", "Student Registration number must be an integer")
                    return

                # Email checking
                if not is_valid_email(self.email):
                    messagebox.showerror("Error", "Invalid email format")
                    return

                #         phone number checking
                if not self.phoneNo.isdigit():
                    messagebox.showerror("Error", "Phone number should be a valid integer")
                    return

                # roll number checking
                if not self.rollNo.isdigit():
                    messagebox.showerror("Error", "Roll number should be a valid integer")
                    return

                else:
                    # Corrected order of parameters in the function call
                    databaseFiles.updateDatabaseMethod(department, course_dropdown, year, semester,
                                                       studentName, division, rollNo, gender, selectedDate, email,
                                                       phoneNo, address, var_radio, studentIdNo)
                    # Insert the updated data into the treeview
                    self.dataInsertion()

                    messagebox.showinfo('Success', 'Data has been updated.')
                    self.clearMethod()
            except Exception as e:
                print(e)
                messagebox.showerror("Error", f"Error occurred\n {e}")

    def deleteMethod(self):
        selectedItem = self.table.focus()
        if not selectedItem:
            messagebox.showerror("Error", "Please select a record to delete.")
            return
        else:
            response = messagebox.askyesno(
                "Confirm", "Do you really want to delete the record? \n Note: The Record will be deleted permanently."
            )

            if response:
                try:
                    results = self.table.item(selectedItem, 'values')[4]
                    databaseFiles.deleteItem(results)
                    messagebox.showinfo("Success", "Record deleted successfully")
                    self.resetMethod()
                    self.fetchData()

                except Exception as e:
                    print(e)
                    messagebox.showerror("Error", f"{e}")


if __name__ == '__main__':
    root2 = Tk()
    StudentWindow(root2)
