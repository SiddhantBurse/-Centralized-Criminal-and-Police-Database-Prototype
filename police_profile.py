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
    load = Image.open(r"C:\Users\dell\Desktop\dbms project\new.png")
    load = load.resize((200, 200), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(load)
    img1 = Label(t, image=photo, borderwidth=2, relief="solid")
    img1.image = photo

    load2 = Image.open(r"C:\Users\dell\Desktop\dbms project\new.png")
    load2 = load2.resize((40, 40), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(load2)
    img2 = Button(t, image=photo2, borderwidth=2, relief="solid")
    img2.image = photo2

    pid1 = Label(t, text='DDR8454518', borderwidth=2, relief="solid")
    email1 = Label(t, text='cpmumbai@police.com', borderwidth=2, relief="solid")
    fname1 = Label(t, text='Vijay', borderwidth=2, relief="solid")
    mname1 = Label(t, text='Dinanath', borderwidth=2, relief="solid")
    lname1 = Label(t, text='Chavan', borderwidth=2, relief="solid")
    contact1 = Label(t, text='9876541203', borderwidth=2, relief="solid")
    juris1 = Label(t, text='Colaba West', borderwidth=2, relief="solid")
    day = Label(t, text='24', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    mth = Label(t, text='September', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    year = Label(t, text='1962', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    gender = Label(t, text='Male', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    marital = Label(t, text='Married', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2,relief="solid")
    batch1 = Label(t, text='1987', borderwidth=2, relief="solid")
    rank1 = Label(t, text='IPS', borderwidth=2, relief="solid")
    address1=Label(t, text = 'Santacruz, Maharashtra, India', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

    '''img2.place(x=50,y=50,width=40, height=40)
    img1.place(x=1200, y=70, width=200, height=200)'''

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

    day.place(x=50, y=500, width=100, height=70)
    mth.place(x=160, y=500, width=200, height=70)
    year.place(x=370, y=500, width=200, height=70)
    gender.place(x=750, y=500, width=200, height=70)
    marital.place(x=1200, y=500, width=200, height=70)

    batch.place(x=50, y=600, width=200, height=70)
    batch1.place(x=300, y=600, width=200, height=70)
    rank.place(x=600, y=600, width=200, height=70)
    rank1.place(x=850, y=600, width=200, height=70)

    address.place(x=50, y=700, width=200, height=70)
    address1.place(x=300, y=700, width=1100, height=70)
    return

pid=Label(t, text='POLICE_ID', borderwidth=2, relief="solid")
email=Label(t, text='Email_ID', borderwidth=2, relief="solid")
fname=Label(t, text='First Name', borderwidth=2, relief="solid")
mname=Label(t, text='Middle Name', borderwidth=2, relief="solid")
lname=Label(t, text='Last Name', borderwidth=2, relief="solid")
contact=Label(t, text='Mobile_Number', borderwidth=2, relief="solid")
juris=Label(t, text='Jurisdiction', borderwidth=2, relief="solid")
batch=Label(t, text='Batch', borderwidth=2, relief="solid")
rank=Label(t, text='Rank', borderwidth=2, relief="solid")
address=Label(t, text='Address', borderwidth=2, relief="solid")


display_details()

mainloop()
