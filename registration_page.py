from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
from tkinter import filedialog
import os

t=tk.Tk()
t.title('NCDS - Register ')
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (w, h))

def submit_details():
    tkinter.messagebox.showinfo('Title', 'User Created')
    t.destroy()
    os.system('python login_page_first.py')
    return
def clear_details():
    t.destroy()
    os.system('python registration_page.py')
    return
def selectimg():
    t.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    print(t.filename)
    load = Image.open(t.filename)
    load = load.resize((175, 175), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(load)
    img1 = Button(t, image=photo, command=selectimg)
    img1.image = photo
    img1.place(x=800, y=450, width=175, height=175)
    return
#fontStyle = tkFont.Font(family="Times New Roman", size=60)
#signup=Label(t, text='SIGN UP', borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=60))
fname=Label(t, text='First Name', borderwidth=2, relief="solid")
mname=Label(t, text='Middle Name', borderwidth=2, relief="solid")
lname=Label(t, text='Last Name', borderwidth=2, relief="solid")
fname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
mname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
lname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
email=Label(t, text='Email_ID', borderwidth=2, relief="solid")
contact=Label(t, text='Mobile_Number', borderwidth=2, relief="solid")
email1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
contact1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
dayOptionList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]#check for february and invalid details
d = tk.IntVar(t)
d.set('Day')
day = tk.OptionMenu(t, d, *dayOptionList)
monthOptionList=['January','February', 'March','April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']#check for february and invalid details
mth = tk.StringVar(t)
mth.set('Month')
month = tk.OptionMenu(t, mth, *monthOptionList)
yearOptionList=[]
for i in range(1900,2002):
    yearOptionList.append(i)
y = tk.IntVar(t)
y.set('Year')
year = tk.OptionMenu(t, y, *yearOptionList)
OptionList=['Male','Female','Others']
v = tk.StringVar(t)
v.set('Select Gender')
gender = tk.OptionMenu(t, v, *OptionList)
OptionList2=['Married','Unmarried','Rather Not Say']
v2 = tk.StringVar(t)
v2.set('Marital Status')
marital = tk.OptionMenu(t, v2, *OptionList2)
address=Label(t, text='Address', borderwidth=2, relief="solid")
address1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
#dob=Label(t, text='First Name', borderwidth=2, relief="solid")
occupation=Label(t, text='Occupation', borderwidth=2, relief="solid")
occupation1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

image=Button(t, text='Choose Photo', command=selectimg, borderwidth=2, relief="solid")

user=Label(t, text='USER_ID', borderwidth=2, relief="solid")
password=Label(t, text='Password', borderwidth=2, relief="solid")
uid=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
pswd=Entry(t,show='*',font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
pswd2=Entry(t,show='*',font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")



submit=Button(t, text='Submit', command=submit_details, borderwidth=2, relief="solid")
reset=Button(t, text='Clear', command=clear_details, borderwidth=2, relief="solid")


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
month.place(x=300, y=250, width=250, height=70)
year.place(x=550, y=250, width=250, height=70)
gender.place(x=900, y=250, width=200, height=70)
marital.place(x=1200, y=250, width=200, height=70)
address.place(x=50, y=350, width=200, height=70)
address1.place(x=300, y=350, width=1100, height=70)
occupation.place(x=50, y=450, width=200, height=70)
occupation1.place(x=300, y=450, width=400, height=70)
image.place(x=800, y=450, width=175, height=175)

user.place(x=50, y=550, width=200, height=70)
password.place(x=50, y=650, width=200, height=70)
uid.place(x=300, y=550, width=400, height=70)
pswd.place(x=300, y=650, width=400, height=70)
pswd2.place(x=750, y=650, width=400, height=70)
submit.place(x=1275, y=450, width=125, height=125)
reset.place(x=1275, y=650, width=125, height=125)

mainloop()