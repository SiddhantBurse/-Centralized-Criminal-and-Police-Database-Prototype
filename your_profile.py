from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import sqlite3
from datetime import datetime
connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()


def police(j,photoPath):
    t = tk.Tk()
    t.title('NCDS POLICE PROFILE ')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))
    t.load = Image.open(photoPath)
    t.load = t.load.resize((250, 350), Image.ANTIALIAS)
    t.photo1 = ImageTk.PhotoImage(t.load, master=t)
    t.img1 = Label(t, image=t.photo1)
    t.img1.image = t.photo1
    t.img1.place(x=975, y=50, width=200, height=225)



    p = cursor.execute('SELECT * FROM POLICE1 where POLICEID=?', (j,))
    u = p.fetchall()
    p1 = cursor.execute('SELECT * FROM POLICE2 where POLICEID=?', (j,))
    u1 = p1.fetchall()

    pid1 = Label(t, text=u[0][0], borderwidth=2, relief="solid")
    email1 = Label(t, text=u[0][7], borderwidth=2, relief="solid")
    fname1 = Label(t, text=u[0][2], borderwidth=2, relief="solid")
    mname1 = Label(t, text=u[0][3], borderwidth=2, relief="solid")
    lname1 = Label(t, text=u[0][4], borderwidth=2, relief="solid")
    contact1 = Label(t, text=u1[0][1], borderwidth=2, relief="solid")
    juris1 = Label(t, text=u[0][8], borderwidth=2, relief="solid")
    dob1 = Label(t, text=u[0][5], font=tkFont.Font(family="Times New Roman", size=15), borderwidth=2, relief="solid")

    gender = Label(t, text=u[0][9], font=tkFont.Font(family="Times New Roman", size=15), borderwidth=2,
                   relief="solid")
    marital = Label(t, text=u[0][6], font=tkFont.Font(family="Times New Roman", size=15), borderwidth=2,
                    relief="solid")
    batch1 = Label(t, text=u[0][10], borderwidth=2, relief="solid")
    rank1 = Label(t, text=u[0][11], borderwidth=2, relief="solid")
    #address1 = Label(t, text=u[0][], font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

    # img2.place(x=50,y=50,width=40, height=40)
    # img1.place(x=1200, y=70, width=200, height=200)
    pid = Label(t, text='POLICE_ID', borderwidth=2, relief="solid")
    email = Label(t, text='Email_ID', borderwidth=2, relief="solid")
    fname = Label(t, text='First Name', borderwidth=2, relief="solid")
    mname = Label(t, text='Middle Name', borderwidth=2, relief="solid")
    lname = Label(t, text='Last Name', borderwidth=2, relief="solid")
    contact = Label(t, text='Mobile_Number', borderwidth=2, relief="solid")
    juris = Label(t, text='Jurisdiction', borderwidth=2, relief="solid")
    batch = Label(t, text='Batch', borderwidth=2, relief="solid")
    rank = Label(t, text='Rank', borderwidth=2, relief="solid")
    # address = Label(t, text='Address', borderwidth=2, relief="solid")
    dob = Label(t, text='Date of Birth', borderwidth=2, relief="solid")

    pid.place(x=50, y=100, width=200, height=70)
    pid1.place(x=200, y=100, width=200, height=70)

    email.place(x=50, y=200, width=200, height=70)
    email1.place(x=200, y=200, width=400, height=70)

    fname.place(x=50, y=300, width=200, height=70)
    mname.place(x=500, y=300, width=200, height=70)
    lname.place(x=950, y=300, width=200, height=70)
    fname1.place(x=275, y=300, width=200, height=70)
    mname1.place(x=725, y=300, width=200, height=70)
    lname1.place(x=1175, y=300, width=200, height=70)

    contact.place(x=50, y=400, width=200, height=70)
    contact1.place(x=300, y=400, width=300, height=70)
    juris.place(x=670, y=400, width=200, height=70)
    juris1.place(x=900, y=400, width=500, height=70)

    dob1.place(x=175, y=500, width=100, height=70)
    dob.place(x=50, y=500, width=100, height=70)
    gender.place(x=750, y=500, width=200, height=70)
    marital.place(x=1200, y=500, width=200, height=70)

    batch.place(x=50, y=600, width=200, height=70)
    batch1.place(x=300, y=600, width=200, height=70)
    rank.place(x=600, y=600, width=200, height=70)
    rank1.place(x=850, y=600, width=200, height=70)

    # address.place(x=50, y=700, width=200, height=70)
    # address1.place(x=300, y=700, width=1100, height=70)




    mainloop()