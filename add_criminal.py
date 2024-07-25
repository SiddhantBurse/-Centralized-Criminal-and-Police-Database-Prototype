from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import sqlite3
connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()

def add2():
    t = tk.Tk()
    t.title('CRIMINALADD')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))

    def image_choose():
        t.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                filetypes=(("jpeg files", ".jpg"), ("all files", ".*")))
        print(t.filename)
        t.load = Image.open(t.filename)
        t.load = t.load.resize((230, 200), Image.ANTIALIAS)
        t.photo = ImageTk.PhotoImage(t.load)
        t.img1 = Button(t, image=t.photo, command=image_choose)
        t.img1.image = t.photo
        t.img1.place(x=1090, y=30, width=230, height=200)

    def convertToBinaryData(filena):
        with open(filena, 'rb') as file:
            blobData = file.read()
        return blobData

    def add3():
        empPhoto = convertToBinaryData(t.filename)
        cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL(CRIMINALID number PRIMARY KEY,FNAME text,MNAME text,LNAME text,DOB text,BLOODGROUP text,STATUS number,PRIORITY number,GENDER text,PHOTO BLOB)')
        cursor.execute("INSERT INTO CRIMINAL VALUES(?,?,?,?,?,?,?,?,?,?)", (c_id1.get(), fname1.get(), mname1.get(), lname1.get(), u,bloodgrp1.get(), status1.get(),priority1.get(),gender1.get(),empPhoto))
        connection.commit()
        cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL1(CRIMINALID number PRIMARY KEY,IDENTIFICATIONMARKS text)')
        cursor.execute("INSERT INTO CRIMINAL1 VALUES(?,?)", (c_id1.get(), im1.get()))
        connection.commit()
        cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL2(CRIMINALID number PRIMARY KEY,ADDRESS text)')
        cursor.execute("INSERT INTO CRIMINAL2 VALUES(?,?)", (c_id1.get(), ad1.get()))
        connection.commit()
        cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL3(CRIMINALID number PRIMARY KEY,CONTACT text)')
        cursor.execute("INSERT INTO CRIMINAL3 VALUES(?,?)",(c_id1.get(), hd1.get()))
        connection.commit()
        connection.commit()
        connection.close()
        tkinter.messagebox.showinfo('Confirmation', 'created')

    fname = Label(t, text='Full Name', borderwidth=2, relief="solid")
    fname1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2,
                   relief="solid")
    mname1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                   relief="solid")
    lname1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                   relief="solid")
    priority = Label(t, text='Priority', borderwidth=2, relief="solid")
    c_id = Label(t, text='Criminal ID', borderwidth=2, relief="solid")
    status = Label(t, text='status', borderwidth=2, relief="solid")
    c_id1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                  relief="solid")
    status1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                    relief="solid")
    priority1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                      relief="solid")
    gender = Label(t, text='Gender', borderwidth=2, relief="solid")
    gender1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                    relief="solid")
    bloodgrp = Label(t, text='BLDGRP', borderwidth=2, relief="solid")
    bloodgrp1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                      relief="solid")
    im = Label(t, text='INDENTIFICATION MARKS', borderwidth=2, relief="solid")
    im1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                relief="solid")
    ad = Label(t, text='ADDRESS', borderwidth=2, relief="solid")
    ad1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                relief="solid")
    hd = Label(t, text='CONTACT', borderwidth=2, relief="solid")
    hd1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2,
                relief="solid")

    # OptionList = [j1[0][1]]
    # v = tk.StringVar(t)
    # v.set('INDENTIFICATION MARKS ')
    # marks = tk.OptionMenu(t, v, *OptionList)
    # OptionList2 = [j2[0][1]]
    # OptionList3 = [j3[0][1]]
    # v2 = tk.StringVar(t)
    # v2.set('ADDRESS')
    # address = tk.OptionMenu(t, v2, *OptionList2)
    # v3 = tk.StringVar(t)
    # v3.set('HIDEOUTS')
    # hideout = tk.OptionMenu(t, v3, *OptionList3)
    dob = Label(t, text='DATE OF BIRTH', borderwidth=2, relief="solid")
    #dob1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    dayOptionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,28,29, 30, 31]  # check for february and invalid details
    d = IntVar(t)
    d.set('Day')
    day = OptionMenu(t, d, *dayOptionList)
    monthOptionList = ['01','02','03','04','05','06','07','08','09','10','11','12']  # check for february and invalid details
    mth = IntVar(t)
    mth.set('Month')
    month = OptionMenu(t, mth, *monthOptionList)
    yearOptionList = []
    for i in range(1900, 2002):
        yearOptionList.append(i)
    y = IntVar(t)
    y.set('Year')
    u=str(y)+'-'+str(mth)+'-'+str(d)
    print(u)
    year = OptionMenu(t, y, *yearOptionList)
    day.place(x=260, y=460)
    month.place(x=320, y=460)
    year.place(x=390, y=460)

    age = Label(t, text='AGE', borderwidth=2, relief="solid")
    age1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                 relief="solid")

    submitt = Button(t, text='submit', command=add3, borderwidth=2, relief="solid")
    image_button = Button(t, text='Choose image file', command=image_choose, borderwidth=2, relief="solid")

    fname.place(x=50, y=150, width=200, height=70)
    fname1.place(x=275, y=150, width=200, height=70)
    mname1.place(x=500, y=150, width=200, height=70)
    lname1.place(x=725, y=150, width=200, height=70)
    c_id.place(x=50, y=50, width=175, height=70)
    priority.place(x=525, y=50, width=200, height=70)
    c_id1.place(x=275, y=50, width=200, height=70)
    priority1.place(x=750, y=50, width=100, height=70)
    status.place(x=900, y=250, width=100, height=70)
    status1.place(x=1025, y=250, width=100, height=70)


    hd.place(x=50, y=550, width=300, height=70)
    hd1.place(x=370, y=550, width=300, height=70)
    ad.place(x=700, y=350, width=300, height=70)
    ad1.place(x=1020, y=350, width=300, height=70)
    im.place(x=50, y=350, width=300, height=70)
    im1.place(x=370, y=350, width=300, height=70)
    # address.place(x=400, y=350, width=300, height=70)
    # hideout.place(x=750, y=350, width=300, height=70)
    gender.place(x=550, y=450, width=200, height=70)
    gender1.place(x=775, y=450, width=200, height=70)
    dob.place(x=50, y=450, width=200, height=70)
    #dob1.place(x=275, y=450, width=200, height=70)
    age.place(x=50, y=250, width=200, height=70)
    age1.place(x=275, y=250, width=200, height=70)
    bloodgrp.place(x=525, y=250, width=200, height=70)
    bloodgrp1.place(x=750, y=250, width=100, height=70)
    submitt.place(x=1170, y=450, width=100, height=70)
    image_button.place(x=1090, y=30, width=230, height=200)

    '''cursor.execute("SELECT * FROM CRIMINAL where CRIMINALID=?", (j,))
    for row in cursor.fetchall():
        print(row)

    cursor.execute("SELECT * FROM CRIMINAL1 where CRIMINALID=?", (j,))
    l = []
    for row1 in cursor.fetchall():
        l.append(row1[1])
        print(row1)
    cursor.execute("SELECT * FROM CRIMINAL2 where CRIMINALID=?", (j,))
    l = []
    for row1 in cursor.fetchall():
        l.append(row1[1])
        print(row1)
    cursor.execute("SELECT * FROM CRIMINAL3 where CRIMINALID=?", (j,))
    l = []
    for row1 in cursor.fetchall():
        l.append(row1[1])
        print(row1)'''



    mainloop()