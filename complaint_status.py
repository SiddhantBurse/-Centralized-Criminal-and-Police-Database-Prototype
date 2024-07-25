from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import os

t=tk.Tk()
t.title('NCDS - Complaint Status ')
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (w, h))

#t.configure(background = 'grey')

def track_status():
    return

compno=Label(t, text='Enter Complaint Number', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
number=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
track=Button(t, text='Track Status',font=tkFont.Font(family="Times New Roman", size=30), command=track_status, borderwidth=2, relief="solid")

compno.place(x=450, y=50, width=600, height=100)
number.place(x=550, y=200, width=400, height=100)
track.place(x=625, y=350, width=250, height=100)

mainloop()