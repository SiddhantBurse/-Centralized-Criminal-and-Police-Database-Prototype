from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
import datetime
from PIL import Image,ImageTk
from your_profile import police

import sqlite3

import os


def acp_home(j):

    connection = sqlite3.connect('NCD.db')
    cursor = connection.cursor()
    q = cursor.execute('SELECT * FROM POLICE1 where POLICEID=?', (j,))
    u = q.fetchall()
    t = tk.Tk()
    t.title('NCDS - Commisioner ')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))


    def enter_profile():
        photo = u[0][13]

        photoPath = "E:\z" + str(20180829_004758) + ".jpg"
        with open(photoPath, 'wb') as file:
            file.write(photo)

        t.destroy()
        police(j, photoPath)

        return
    def dashboard():
        return
    def search():
        t.destroy()
        os.system('python police_search.py')
        return
    def add():
        t.destroy()
        os.system('python add_acp.py')
        return

    def last():
        tkinter.messagebox.showinfo('Last Login', u[0][12])
        return
    def logout():
        b = str(datetime.datetime.now())
        cursor.execute("UPDATE POLICE1 set LASTLOGIN=? where POLICEID=?", (b, j))
        connection.commit()
        t.destroy()
        os.system('python login_page_first.py')

    t.configure(background = 'grey')

    name=Label(t, text='Commissioner - Parambir Singh', fg='orange',font=tkFont.Font(family="Times New Roman", size=40), borderwidth=2, relief="solid")
    profile=Button(t, text='Your Profile', command=enter_profile, borderwidth=2, relief="solid")
    dash=Button(t, text='Dashboard', command=dashboard, borderwidth=2, relief="solid")
    access=Button(t, text='Access Records', command=search, borderwidth=2, relief="solid")
    last=Button(t, text='Last Login Details', command=last, borderwidth=2, relief="solid")
    logout=Button(t, text='Logout ', command=logout, borderwidth=2, relief="solid")
    add=Button(t, text='add',command=add, borderwidth=2, relief="solid")

    name.place(x=0, y=50, width=w, height=100)
    profile.place(x=0.8*w, y=200, width=0.175*w, height=100)
    logout.place(x=0.8*w, y=350, width=0.175*w, height=100)
    dash.place(x=50, y=200, width=0.175*w, height=100)
    access.place(x=50, y=350, width=0.175*w, height=100)
    last.place(x=50, y=500, width=0.175*w, height=100)
    add.place(x=0.8*w, y=500, width=0.175*w, height=100)

    mainloop()
acp_home(121)

