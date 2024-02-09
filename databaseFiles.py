import pymysql


def createTable():
    conn = pymysql.connect(host="localhost", user="root", password="isaac")

    cursor = conn.cursor()

    cursor.execute("create database if not exists students ")

    cursor.execute("use students")

    query = '''
                                     create table if not exists students_details(
                                     department varchar(50),
                                     course varchar(50),
                                     year varchar(50),
                                     semester varchar(20),
                                     studentId int primary key not null,
                                     studentName varchar(50),
                                     classDiv varchar(50),
                                     rollNo int,
                                     gender varchar(50),
                                     dob varchar(50),
                                     email varchar(50),
                                     phoneNo int,
                                     address varchar(50),
                                     photo varchar(50)
                                     )
                                     '''

    cursor.execute(query)
    conn.commit()
    conn.close()


def updateDatabaseMethod(department, course_drop, year, semester, studentName, division, studentRollNo,
                         gender, dob, email, phone, address, var_radio1, studentId):
    items = (department, course_drop, year, semester, studentName, division, studentRollNo,
             gender, dob, email, phone, address, var_radio1, studentId)

    conn = pymysql.connect(host="localhost", user="root", password="isaac")

    cursor = conn.cursor()

    cursor.execute("use students")

    query = '''
                update students_details
                set 
                department=%s,
                course=%s,
                year=%s,
                semester=%s,
                studentName=%s,
                classDiv=%s,
                rollNo=%s,
                gender=%s,
                dob=%s,
                email=%s,
                phoneNo=%s,
                address=%s,
                photo=%s
                where studentId=%s
            '''
    cursor.execute(query, items)
    conn.commit()
    print("success")
    conn.close()


def userExists(studentIdNo):
    conn = pymysql.connect(host="localhost", user="root", password="isaac")

    cursor = conn.cursor()

    cursor.execute("use students")
    query = '''
                       SELECT * FROM students_details WHERE studentId = %s
                       '''
    cursor.execute(query, (studentIdNo,))
    rows = cursor.fetchone()
    conn.close()
    return rows


def databaseInsertion(department,
                      course_dropdown,
                      year,
                      semester,
                      studentIdNo,
                      studentName,
                      division,
                      rollNo,
                      gender,
                      selectedDate,
                      email,
                      phoneNo,
                      address,
                      var_radio1):
    conn = pymysql.connect(host="localhost", user="root", password="isaac")

    cursor = conn.cursor()

    cursor.execute("use students")
    query = '''insert into students_details values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

    cursor.execute(query, (
        department,
        course_dropdown,
        year,
        semester,
        studentIdNo,
        studentName,
        division,
        rollNo,
        gender,
        selectedDate,
        email,
        phoneNo,
        address,
        var_radio1
    ))
    conn.commit()
    conn.close()


def fetchingData():
    conn = pymysql.connect(host="localhost", user="root", password="isaac")

    cursor = conn.cursor()
    cursor.execute("use students")
    query = ''' select * from students_details '''
    cursor.execute(query)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data


def deleteItem(studentId):
    conn = pymysql.connect(host="localhost", user="root", password="isaac")

    cursor = conn.cursor()
    cursor.execute("use students")
    query = ''' delete from students_details where studentId=%s'''
    cursor.execute(query, (studentId,))
    conn.commit()
    conn.close()
