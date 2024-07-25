from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
from tkinter import filedialog
import os

t=tk.Tk()
t.title('NCDS - Complaint ')
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (w, h))

def submit_details():
    #after submitting details
    tkinter.messagebox.showinfo('Title', 'Complaint Registered. \nA corresponding officer will contact you within 48 hours')
    t.destroy()
    return
def clear_details():
    t.destroy()
    os.system('python complaintform.py')
    return

head=Label(t, text='R E G I S T E R   C O M P L A I N T',font=tkFont.Font(family="Times New Roman", size=50), borderwidth=2, relief="solid")
head.place(x=0, y=0, width=w, height=70)

userid=Label(t, text='User ID : 43635374', borderwidth=2, relief="solid")
userid.place(x=50, y=100, width=400, height=70)

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

day.place(x=500, y=100, width=100, height=70)
month.place(x=650, y=100, width=100, height=70)
year.place(x=800, y=100, width=100, height=70)

time=Label(t, text='Time of Crime', borderwidth=2, relief="solid")
time1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
time.place(x=950, y=100, width=200, height=70)
time1.place(x=1200, y=100, width=200, height=70)

city=Label(t, text='City', borderwidth=2, relief="solid")
city1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
city.place(x=50, y=200, width=200, height=70)
city1.place(x=300, y=200, width=400, height=70)

ps=Label(t, text='Police Station', borderwidth=2, relief="solid")
ps1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
ps.place(x=750, y=200, width=200, height=70)
ps1.place(x=1000, y=200, width=400, height=70)

place=Label(t, text='Place of Crime', borderwidth=2, relief="solid")
place1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
place.place(x=50, y=300, width=200, height=70)
place1.place(x=300, y=300, width=1100, height=70)

afname=Label(t, text='ACCUSED First Name', borderwidth=2, relief="solid")
amname=Label(t, text='Middle Name', borderwidth=2, relief="solid")
alname=Label(t, text='Last Name', borderwidth=2, relief="solid")
afname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
amname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
alname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

afname.place(x=50, y=400, width=200, height=70)
amname.place(x=500, y=400, width=200, height=70)
alname.place(x=950, y=400, width=200, height=70)
afname1.place(x=275, y=400, width=200, height=70)
amname1.place(x=725, y=400, width=200, height=70)
alname1.place(x=1175, y=400, width=200, height=70)


vfname=Label(t, text='VICTIM First Name', borderwidth=2, relief="solid")
vmname=Label(t, text='Middle Name', borderwidth=2, relief="solid")
vlname=Label(t, text='Last Name', borderwidth=2, relief="solid")
vfname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
vmname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
vlname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

vfname.place(x=50, y=500, width=200, height=70)
vmname.place(x=500, y=500, width=200, height=70)
vlname.place(x=950, y=500, width=200, height=70)
vfname1.place(x=275, y=500, width=200, height=70)
vmname1.place(x=725, y=500, width=200, height=70)
vlname1.place(x=1175, y=500, width=200, height=70)

desc=Label(t, text='Crime Description', borderwidth=2, relief="solid")
description=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
desc.place(x=50, y=600, width=200, height=70)
description.place(x=300, y=600, width=1100, height=70)

#image=Button(t, text='Choose Photo', command=selectimg, borderwidth=2, relief="solid")

submit=Button(t, text='Submit', command=submit_details, borderwidth=2, relief="solid")
reset=Button(t, text='Clear', command=clear_details, borderwidth=2, relief="solid")

submit.place(x=50, y=700, width=300, height=70)
reset.place(x=500, y=700, width=125, height=70)

mainloop()