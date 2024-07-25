from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import os

t=tk.Tk()
t.title('NCDS')
t.configure(background = 'grey')
t.geometry("1500x800+30+30")
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (w, h))
fontStyle = tkFont.Font(family="Times New Roman", size=60)
def enter():
    if v.get()=='Civilian' and uid.get()=='raj' and pswd.get()=='12345':
        tkinter.messagebox.showinfo('Title','Logged_In')
        clear()
        t.destroy()
        os.system('python civilian_home.py')
    elif v.get()=='Police' and uid.get()=='siddhant' and pswd.get()=='12345':
        tkinter.messagebox.showinfo('Title', 'Logged_In')
        clear()
        t.destroy()
        os.system('python acp_home.py')
    elif v.get()=='Police' and uid.get()=='naman' and pswd.get()=='12345':
        tkinter.messagebox.showinfo('Title', 'Logged_In')
        clear()
        t.destroy()
        os.system('python constable_home.py')
    elif v.get()=='Police' and uid.get()=='sarvesh' and pswd.get()=='12345':
        tkinter.messagebox.showinfo('Title', 'Logged_In')
        clear()
        t.destroy()
        os.system('python sys_home.py')
    else:
        tkinter.messagebox.showinfo('Title','Bhag Idhar se')
def clear():
    uid.delete(0, 'end')
    pswd.delete(0, 'end')
    v.set('User Type')
def register():
    t.destroy()   #find suspend way to regain the page for reuse
    os.system('python registration_page.py')
    #Open Registration page
    return
def close():
    t.destroy()
OptionList=['Police','Civilian']
v = tk.StringVar(t)
v.set('User Type')
opt = tk.OptionMenu(t, v, *OptionList)

impmsg=Label(t, text='WELCOME TO POLICE PORTAL', fg='red',font=tkFont.Font(family="Times New Roman", size=60), borderwidth=2, relief="solid")
wanted=Label(t, text='W A N T E D ', fg='red',font=tkFont.Font(family="Times New Roman", size=40), borderwidth=2, relief="solid")
detail=Label(t, text='Log In to Portal', borderwidth=2, relief="solid")

user=Label(t, text='USER_ID', borderwidth=2, relief="solid")
password=Label(t, text='Password', borderwidth=2, relief="solid")
uid=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
pswd=Entry(t,show='*',font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
submit=Button(t, text='Submit', command=enter, borderwidth=2, relief="solid")
reset=Button(t, text='Clear', command=clear, borderwidth=2, relief="solid")
signup=Button(t, text='Register', command=register, borderwidth=2, relief="solid")
close=Button(t, text='Exit', command=close, borderwidth=2, relief="solid")

load = Image.open(r"C:\Users\dell\Desktop\dbms project\new.png")
load = load.resize((200,200),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(load)

img1 = Label(t, image=photo)
img1.image = photo

img2 = Label(t, image=photo)
img2.image = photo

img3 = Label(t, image=photo)
img3.image = photo

load2 = Image.open(r"C:\Users\dell\Desktop\dbms project\new.png")
load2 = load2.resize((200,200),Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(load2)
img4 = Label(t, image=photo2)
img4.image = photo2

img5 = Label(t, image=photo2)
img5.image = photo2

img6 = Label(t, image=photo2)
img6.image = photo2

impmsg.place(x=0, y=50, width=w, height=100)

wanted.place(x=600, y=160, width=800, height=70)

detail.place(x=90 , y=200, width=410, height=75)

opt.place(x = 90, y = 300 , width=410, height=70)
user.place(x = 90, y = 380 , width=200, height=70)
uid.place(x = 300, y = 380 , width=200, height=70)
password.place(x = 90, y = 460 , width=200, height=70)
pswd.place(x = 300, y = 460 , width=200, height=70)

submit.place(x = 90, y = 540, width=200, height=70)
reset.place(x = 300, y = 540 , width=200, height=70)

signup.place(x= 90, y = 630, width = 200, height = 70)
close.place(x= 300, y = 630, width = 200, height = 70)

img1.place(x = 600, y = 250 , width=200, height=200)
img2.place(x = 900, y = 250 , width=200, height=200)
img3.place(x = 1200, y = 250 , width=200, height=200)
img4.place(x = 600, y = 500 , width=200, height=200)
img5.place(x = 900, y = 500 , width=200, height=200)
img6.place(x = 1200, y = 500 , width=200, height=200)
mainloop()