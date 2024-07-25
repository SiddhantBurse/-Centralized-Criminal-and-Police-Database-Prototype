from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import os
t=tk.Tk()
t.title('CASE')
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (w, h))

def edit():
    t.destroy()
    os.system('python open_caseedit.py')
    return

victim=Label(t, text='Name of victim', borderwidth=2, relief="solid")
od=Label(t, text='OPENING DATE', borderwidth=2, relief="solid")
address=Label(t, text='CASE ID', borderwidth=2, relief="solid")
victim1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
od1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
address1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
#=Label(t, text='FIR', borderwidth=2, relief="solid")
case_id=Label(t, text='Criminal ID', borderwidth=2, relief="solid")
status=Label(t, text='status', borderwidth=2, relief="solid")
case_id1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
status1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
#=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
desc=Label(t, text='DESCRIPTION', borderwidth=2, relief="solid")
desc1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
cd=Label(t, text='CLOSING DATE', borderwidth=2, relief="solid")
cd1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
OptionList=['A034','GD2745','VSF2628']
v = tk.StringVar(t)
v.set('FIR NUMBER ')
fir= tk.OptionMenu(t, v, *OptionList)
OptionList2=['103345','17354','3727354']
OptionList3=['IPC340','IPC420','CRPC6452']
v2 = tk.StringVar(t)
v2.set('POLICE ID')
police_id= tk.OptionMenu(t, v2, *OptionList2)
v3 = tk.StringVar(t)
v3.set('PENAL NUMBER')
penal_no=tk.OptionMenu(t, v3, *OptionList3)
ps=Label(t, text='POLICE STATION', borderwidth=2, relief="solid")
ps1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
age=Label(t, text='AGE', borderwidth=2, relief="solid")
age1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
editt=Button(t, text='edit',command=edit, borderwidth=2, relief="solid")


victim.place(x=50, y=150, width=150, height=70)
age.place(x=400, y=150, width=150, height=70)
address.place(x=750, y=150, width=150, height=70)
victim1.place(x=225, y=150, width=150, height=70)
age1.place(x=575, y=150, width=150, height=70)
address1.place(x=925, y=150, width=150, height=70)
case_id.place(x=50, y=50, width=175, height=70)
fir.place(x=525,y=50,width=200,height=70)
case_id1.place(x=275, y=50, width=200, height=70)
police_id.place(x=750,y=50,width=100,height=70)
status.place(x=900, y=250, width=100, height=70)
status1.place(x=1025, y=250, width=100, height=70)

#marks.place(x=50, y=350, width=300, height=70)
#address.place(x=400, y=350, width=300, height=70)
penal_no.place(x=800, y=350, width=200, height=70)
desc.place(x=550, y=350, width=100, height=70)
desc1.place(x=675, y=350, width=100, height=70)
ps.place(x=50, y=350, width=200, height=70)
ps1.place(x=275, y=350, width=200, height=70)
od.place(x=50, y=250, width=200, height=70)
od1.place(x=275, y=250, width=200, height=70)
cd.place(x=525,y=250,width=200,height=70)
cd1.place(x=750,y=250,width=100,height=70)
editt.place(x=1025, y=350, width=100, height=70)
mainloop()