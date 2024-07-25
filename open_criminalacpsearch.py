from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk
from open_criminaledit import*
import datetime
import os





def test(j, j1, j2, j3,photoPath):
    t = tk.Tk()
    t.title('CRIMINAL')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))

    born1 = j[0][4]
    sss = born1.split('-')
    mmm = datetime.datetime.today()

    b = mmm.year - int(sss[0])

    def edit():
     t.destroy()
     test1(j, j1, j2, j2,photoPath)
     #os.system('python open_criminaledit.py')
     return

    fname = Label(t, text='Full Name',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    fname1 = Label(t, text=j[0][1], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    mname1 = Label(t, text=j[0][2], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    lname1 = Label(t, text=j[0][3], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    priority = Label(t, text='Priority',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    c_id = Label(t, text='Criminal ID',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    status = Label(t, text='status',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    c_id1 = Label(t, text=j[0][0], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    status1 = Label(t, text=j[0][6], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    priority1 = Label(t, text=j[0][7], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                      relief="solid")
    gender = Label(t, text='Gender', font=tkFont.Font(family="Times New Roman", size=16),borderwidth=2, relief="solid")
    gender1 = Label(t, text=j[0][8], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                    relief="solid")
    bloodgrp = Label(t, text='BLDGRP',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    bloodgrp1 = Label(t, text=j[0][5], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                      relief="solid")
    OptionList = [j1[0][1]]
    v = tk.StringVar(t)
    v.set('INDENTIFICATION MARKS ')
    marks = tk.OptionMenu(t, v, *OptionList)
    OptionList2 = [j2[0][1]]
    OptionList3 = [j3[0][1]]
    v2 = tk.StringVar(t)
    v2.set('ADDRESS')
    address = tk.OptionMenu(t, v2, *OptionList2)
    v3 = tk.StringVar(t)
    v3.set('CONTACT')
    hideout = tk.OptionMenu(t, v3, *OptionList3)
    dob = Label(t, text='DATE OF BIRTH',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    dob1 = Label(t, text=j[0][4], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    age = Label(t, text='AGE',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    age1 = Label(t, text=b, font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                 relief="solid")
    editt = Button(t, text='edit',font=tkFont.Font(family="Times New Roman", size=16), command=edit, borderwidth=2, relief="solid")

    t.load = Image.open(photoPath)
    t.load = t.load.resize((250, 350), Image.ANTIALIAS)
    t.photo1 = ImageTk.PhotoImage(t.load, master=t)
    t.img1 = Label(t, image=t.photo1)
    t.img1.image = t.photo1
    t.img1.place(x=1090, y=30, width=230, height=200)

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

    marks.place(x=50, y=350, width=300, height=70)
    address.place(x=400, y=350, width=300, height=70)
    hideout.place(x=750, y=350, width=300, height=70)
    gender.place(x=550, y=450, width=200, height=70)
    gender1.place(x=775, y=450, width=200, height=70)
    dob.place(x=50, y=450, width=200, height=70)
    dob1.place(x=275, y=450, width=200, height=70)
    age.place(x=50, y=250, width=200, height=70)
    age1.place(x=275, y=250, width=200, height=70)
    bloodgrp.place(x=525, y=250, width=200, height=70)
    bloodgrp1.place(x=750, y=250, width=100, height=70)
    editt.place(x=1025, y=450, width=100, height=70)
    mainloop()