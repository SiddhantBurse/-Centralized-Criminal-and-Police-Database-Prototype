from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox
from PIL import Image,ImageTk
import os

t=Tk()
t.title('System Administrator')
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (w, h))
def add_user():
    #t.destroy()
    os.system('python add_user.py')
    pass
def update_user():
    # t.destroy()
    os.system('python choose_user.py')
    pass
def delete_user():
    # t.destroy()
    os.system('python del_user.py')
    pass
v = StringVar(t)
empty_box_1=Label(t, text='     ',font=tkFont.Font(family="Times New Roman", size=222) ,borderwidth=2, relief="solid").place(x=50,y=218)
finishing_1=Label(t, text='Controls',font=tkFont.Font(family="Times New Roman", size=15) ,borderwidth=2, relief="solid").place(x=200,y=175)


user_detail_1=Label(t, text='Name : ',font=tkFont.Font(family="Times New Roman", size=15) ,borderwidth=2, relief="solid",width=11,height=2).place(x=1100,y=425)
user_detail_2=Label(t, text='I.D. : ',font=tkFont.Font(family="Times New Roman", size=15) ,borderwidth=2, relief="solid", width=11,height=2).place(x=1100,y=485)
user_detail_3=Label(t, text='Date of Birth : ',font=tkFont.Font(family="Times New Roman", size=15) ,borderwidth=2, relief="solid", width=11,height=2).place(x=1100,y=545)
user_detail_4=Label(t, text='Rank : ',font=tkFont.Font(family="Times New Roman", size=15) ,borderwidth=2, relief="solid", width=11,height=2).place(x=1100,y=605)
user_detail_5=Label(t, text='Email I.D.',font=tkFont.Font(family="Times New Roman", size=15) ,borderwidth=2, relief="solid", width=11,height=2).place(x=1100,y=665)


add_user=Button(t, text='Add a New User', command=add_user, borderwidth=2, relief="solid", width=45,height=4)
update_user=Button(t, text='Update the User Information', command=update_user, borderwidth=2, relief="solid",width=45,height=4)
delete_user=Button(t, text='Delete the User', command=delete_user, borderwidth=2, relief="solid",width=45,height=4)

load2 = Image.open(r"C:\Users\RAJ P BORA\Downloads\dawood.png")
load2 = load2.resize((250,350),Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(load2)
img4 = Label(t, image=photo2)
img4.image = photo2

add_user.place(x = 70, y = 250)
delete_user.place(x = 70, y = 350)
update_user.place(x = 70, y = 450)
img4.place(x = 1100, y = 60)
mainloop()