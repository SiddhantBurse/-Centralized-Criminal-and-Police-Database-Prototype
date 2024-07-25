from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox
from PIL import Image,ImageTk

def deletion_message():
    if True:
        tkinter.messagebox.showinfo('Deletion Messege','I.D. Deleted')
    else:
        tkinter.messagebox.showinfo('No Deletion Messege','I.D. not Deleted')
t=Tk()
t.title('Enter User Page')
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (w, h))
l_user_id=Label(t, text='User I.D. :',anchor='w', borderwidth=2, relief="solid", width=12, height=2).place(x=620, y=300)
user_id=Entry(t,font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid").place(x=720, y=300)
next_1_button=Button(t, text='Delete the User', command=deletion_message ,borderwidth=2, relief="solid", width=26,height=2).place(x=750, y=450)

mainloop()