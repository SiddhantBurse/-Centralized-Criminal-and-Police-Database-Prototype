from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
t=tk.Tk()
t.title('NCDS - Register ')
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (w, h))

def display_details():
    load2 = Image.open(r"C:\Users\RAJ P BORA\Downloads\edit.jpg")
    load2 = load2.resize((40, 40), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(load2)
    img2 = Button(t, image=photo2, borderwidth=2, relief="solid")
    img2.image = photo2


    fname1 = Label(t, text = 'Raj', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    mname1 = Label(t, text = 'P', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    lname1 = Label(t, text = 'Bora', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    email1 = Label(t, text = 'Rajbora1000@gmail.com', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    contact1 = Label(t, text = '8308763611', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    day=Label(t, text = '24', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    mth=Label(t, text = 'September', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    year=Label(t, text = '2000', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    gender = Label(t, text = 'Male', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    marital = Label(t, text = 'Unmarried', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    address1=Label(t, text = 'Dhule, Maharashtra, India', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    occupation1 = Label(t, text='Student', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    uid = Label(t, text='raj', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

    fname.place(x=50, y=50, width=200, height=70)
    mname.place(x=500, y=50, width=200, height=70)
    lname.place(x=950, y=50, width=200, height=70)
    fname1.place(x=275, y=50, width=200, height=70)
    mname1.place(x=725, y=50, width=200, height=70)
    lname1.place(x=1175, y=50, width=200, height=70)
    email.place(x=50, y=150, width=175, height=70)
    contact.place(x=950, y=150, width=190, height=70)
    email1.place(x=250, y=150, width=600, height=70)
    contact1.place(x=1150, y=150, width=250, height=70)
    day.place(x=50, y=250, width=250, height=70)
    mth.place(x=300, y=250, width=250, height=70)
    year.place(x=550, y=250, width=250, height=70)
    gender.place(x=900, y=250, width=200, height=70)
    marital.place(x=1200, y=250, width=200, height=70)
    address.place(x=50, y=350, width=200, height=70)
    address1.place(x=300, y=350, width=1100, height=70)
    occupation.place(x=50, y=450, width=200, height=70)
    occupation1.place(x=300, y=450, width=400, height=70)
    user.place(x=50, y=550, width=200, height=70)
    uid.place(x=300, y=550, width=400, height=70)
    img2.place(x=1370, y=550, width=40, height=40)

fname=Label(t, text='First Name', borderwidth=2, relief="solid")
mname=Label(t, text='Middle Name', borderwidth=2, relief="solid")
lname=Label(t, text='Last Name', borderwidth=2, relief="solid")

email=Label(t, text='Email_ID', borderwidth=2, relief="solid")
contact=Label(t, text='Mobile_Number', borderwidth=2, relief="solid")


address=Label(t, text='Address', borderwidth=2, relief="solid")

#dob=Label(t, text='First Name', borderwidth=2, relief="solid")
occupation=Label(t, text='Occupation', borderwidth=2, relief="solid")

user=Label(t, text='USER_ID', borderwidth=2, relief="solid")


display_details()



mainloop()