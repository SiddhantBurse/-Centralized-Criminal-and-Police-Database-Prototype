from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import os

t=tk.Tk()
t.title('NCDS - Civilian ')
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (w, h))

def enter_profile():
    os.system('python disp_profile.py')
    return
def complaint():
    os.system('python complaintform.py')
    return
def status():
    os.system('python complaint_status.py')
    return
def data_analysis():
    return
def locate_ps():
    return
def logout():
    t.destroy()
    os.system('python login_page_first.py')
t.configure(background = 'grey')

name=Label(t, text='Arjun Rathore', fg='orange',font=tkFont.Font(family="Times New Roman", size=40), borderwidth=2, relief="solid")
profile=Button(t, text='Your Profile', command=enter_profile, borderwidth=2, relief="solid")
complain=Button(t, text='Register Complaint', command=complaint, borderwidth=2, relief="solid")
track=Button(t, text='Track Complaint Status', command=status, borderwidth=2, relief="solid")
view=Button(t, text='View Data', command=data_analysis, borderwidth=2, relief="solid")
locate=Button(t, text='Locate P S ', command=locate_ps, borderwidth=2, relief="solid")
logout=Button(t, text='Logout ', command=logout, borderwidth=2, relief="solid")

load = Image.open(r"C:\Users\RAJ P BORA\Downloads\dawood.png")
load = load.resize((w,h),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(load)
img1 = Label(t, image=photo)
img1.image = photo
#img1.place(x=0, y=0, relwidth=1, relheight=1)


name.place(x=0, y=50, width=w, height=100)
profile.place(x=0.8*w, y=200, width=0.175*w, height=100)
logout.place(x=0.8*w, y=350, width=0.175*w, height=100)
complain.place(x=50, y=200, width=0.175*w, height=100)
track.place(x=50, y=350, width=0.175*w, height=100)
view.place(x=50, y=500, width=0.175*w, height=100)
locate.place(x=50, y=650, width=0.175*w, height=100)

mainloop()