from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import os
t=tk.Tk()
t.title('CRIMINAL')
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (w, h))

def edit():
    t.destroy()
    os.system('python open_criminaledit.py')
    return
fname=Label(t, text='Full Name', borderwidth=2, relief="solid")
fname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
mname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
lname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
priority=Label(t, text='Priority', borderwidth=2, relief="solid")
c_id=Label(t, text='Criminal ID', borderwidth=2, relief="solid")
status=Label(t, text='status', borderwidth=2, relief="solid")
c_id1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
status1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
priority1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
gender=Label(t, text='Gender', borderwidth=2, relief="solid")
gender1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
bloodgrp=Label(t, text='BLDGRP', borderwidth=2, relief="solid")
bloodgrp1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
OptionList=['blind','deaf','sgdhh']
v = tk.StringVar(t)
v.set('INDENTIFICATION MARKS ')
marks= tk.OptionMenu(t, v, *OptionList)
OptionList2=['delhi','mumbai','dhule']
OptionList3=['kalyan','worli','andheri']
v2 = tk.StringVar(t)
v2.set('ADDRESS')
address= tk.OptionMenu(t, v2, *OptionList2)
v3 = tk.StringVar(t)
v3.set('HIDEOUTS')
hideout=tk.OptionMenu(t, v3, *OptionList3)
dob=Label(t, text='DATE OF BIRTH', borderwidth=2, relief="solid")
dob1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
age=Label(t, text='AGE', borderwidth=2, relief="solid")
age1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
editt=Button(t, text='edit',command=edit, borderwidth=2, relief="solid")



fname.place(x=50, y=150, width=200, height=70)
fname1.place(x=275, y=150, width=200, height=70)
mname1.place(x=500, y=150, width=200, height=70)
lname1.place(x=725, y=150, width=200, height=70)
c_id.place(x=50, y=50, width=175, height=70)
priority.place(x=525,y=50,width=200,height=70)
c_id1.place(x=275, y=50, width=200, height=70)
priority1.place(x=750,y=50,width=100,height=70)
status.place(x=900, y=250, width=100, height=70)
status1.place(x=1025, y=250, width=100, height=70)


marks.place(x=50, y=350, width=300, height=70)
address.place(x=400, y=350, width=300, height=70)
hideout.place(x=750, y=350, width=300, height=70)
gender.place(x=550, y=450, width=200, height=70)
gender1.place(x=775, y=450, width=200, height=70)
dob.place(x=50, y=450, width=200, height=70)
dob1.place(x=275, y=450, width=200, height=70)
age.place(x=50, y=250, width=200, height=70)
age1.place(x=275, y=250, width=200, height=70)
bloodgrp.place(x=525,y=250,width=200,height=70)
bloodgrp1.place(x=750,y=250,width=100,height=70)
mainloop()