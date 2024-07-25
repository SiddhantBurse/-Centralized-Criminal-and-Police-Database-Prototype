from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import os

t=tk.Tk()
t.title('NCDS - Constable ')
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (w, h))

def enter_profile():
    os.system('python police_profile.py')
    return
def dashboard():
    return
def search():
    t.destroy()
    os.system('python police_search.py')
    return
def last():
    tkinter.messagebox.showinfo('Title', 'Last Login Session was recorded on 02/28/2020 05:57:51 ')
    return
def logout():
    t.destroy()
    os.system('python login_page_first.py')

t.configure(background = 'grey')

name=Label(t, text='Constable - Chulbul Pandey', fg='orange',font=tkFont.Font(family="Times New Roman", size=40), borderwidth=2, relief="solid")
profile=Button(t, text='Your Profile', command=enter_profile, borderwidth=2, relief="solid")
dash=Button(t, text='Dashboard', command=dashboard, borderwidth=2, relief="solid")
access=Button(t, text='Access Records', command=search, borderwidth=2, relief="solid")
last=Button(t, text='Last Login Details', command=last, borderwidth=2, relief="solid")
logout=Button(t, text='Logout ', command=logout, borderwidth=2, relief="solid")

name.place(x=0, y=50, width=w, height=100)
profile.place(x=0.8*w, y=200, width=0.175*w, height=100)
logout.place(x=0.8*w, y=350, width=0.175*w, height=100)
dash.place(x=50, y=200, width=0.175*w, height=100)
access.place(x=50, y=350, width=0.175*w, height=100)
last.place(x=50, y=500, width=0.175*w, height=100)

mainloop()