from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox
from PIL import Image,ImageTk

def updated_user():
    if True:
        tkinter.messagebox.showinfo('Confirmation','User Updated')
    else:
        tkinter.messagebox.showinfo('Error Message','Updation Unsuccessfull')


t=Tk()
t.title('Add User Page')
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (w, h))
l_first_name=Label(t, text='First Name :',anchor='w', borderwidth=2, relief="solid", width=12, height=2).place(x=50, y=10)
l_middle_name=Label(t, text='Middle Name :',anchor='w', borderwidth=2, relief="solid", width=12, height=2).place(x=50, y=50)
l_last_name=Label(t, text='Last Name :',anchor='w', borderwidth=2, relief="solid", width=12, height=2).place(x=50, y=90)
v = StringVar()
gender=Label(t, text='Gender :',anchor='w', borderwidth=2, relief="solid", width=12, height=2).place(x=50, y=130)
Radiobutton(t, text='Male', variable=v, value='Male').place(x=200, y=140)
Radiobutton(t, text='Female', variable=v, value='Female').place(x=270, y=140)
Radiobutton(t, text='Other', variable=v, value='Other').place(x=350, y=140)
l_date_of_birth=Label(t, text='Date of Birth :',anchor='w', borderwidth=2, relief="solid", width=12, height=2).place(x=50, y=170)
dayOptionList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]#check for february and invalid details
d = IntVar(t)
day = OptionMenu(t, d, *dayOptionList)
monthOptionList=['January','February', 'March','April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']#check for february and invalid details
mth = StringVar(t)
month = OptionMenu(t, mth, *monthOptionList)
yearOptionList=[]
for i in range(1900,2002):
    yearOptionList.append(i)
y = IntVar(t)
year = OptionMenu(t, y, *yearOptionList)
day.place(x=200, y=170)
month.place(x=270, y=170)
year.place(x=350, y=170)
l_police_id=Label(t, text='Police ID :',anchor='w', borderwidth=2, relief="solid", width=12, height=2).place(x=50, y=210)
l_email_id=Label(t, text='Email I.D. :',anchor='w', borderwidth=2, relief="solid", width=12, height=2).place(x=50, y=250)
l_jurisdiction=Label(t, text='Jurisdiction :',anchor='w', borderwidth=2, relief="solid", width=12, height=2).place(x=50, y=290)
v2 = StringVar(t)
rank_options = ['Commissioner','Constable','System Administrator']
l_rank=Label(t, text='Rank :',anchor='w', borderwidth=2, relief="solid", width=12, height=2).place(x=50, y=330)
rank_menu = OptionMenu(t, v2, *rank_options)
rank_menu.place(x=200, y=330)
l_identification_marks=Label(t, text='Identification\n Marks :',anchor='w', borderwidth=2, relief="solid", width=12, height=2).place(x=50, y=370)
l_contact_number_1=Label(t, text='Contact \nNumber 1 :',anchor='w', borderwidth=2, relief="solid", width=12, height=2).place(x=50, y=410)
l_contact_number_2=Label(t, text='Contact \nNumber 2 :',anchor='w', borderwidth=2, relief="solid", width=12, height=2).place(x=50, y=450)
l_batch=Label(t, text='Batch :',anchor='w', borderwidth=2, relief="solid", width=12, height=2).place(x=50, y=490)
l_password=Label(t, text='Password :',anchor='w', borderwidth=2, relief="solid", width=12, height=2).place(x=50, y=530)
a=StringVar(t)
first_name=Entry(t,font=tkFont.Font(family="Times New Roman", size=20),textvariable=a, borderwidth=2, relief="solid").place(x=200, y=10)
a.set("Sarvesh")
middle_name=Entry(t,font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid").place(x=200, y=50)
last_name=Entry(t,font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid").place(x=200, y=90)
police_id=Entry(t,font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid").place(x=200, y=210)
email_id=Entry(t,font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid").place(x=200, y=250)
jurisdiction=Entry(t,font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid").place(x=200, y=290)
identification_marks=Entry(t,font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid").place(x=200, y=370)
contact_number_1=Entry(t,font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid").place(x=200, y=410)
contact_number_2=Entry(t,font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid").place(x=200, y=450)
batch=Entry(t,font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid").place(x=200, y=490)
password=Entry(t,font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid").place(x=200, y=530)
update_user_2_button=Button(t, text='Update User', command=updated_user,borderwidth=2, relief="solid", width=26,height=2).place(x=216, y=620)
mainloop()