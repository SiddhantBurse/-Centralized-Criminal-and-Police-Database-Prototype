from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import os
t=tk.Tk()
t.title('CRIME')
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (w, h))

def edit():
    t.destroy()
    os.system('python open_crimeedit.py')
    return
name=Label(t, text='Victim name', borderwidth=2, relief="solid")
noi=Label(t, text='NUMBER OF INJURIES', borderwidth=2, relief="solid")
nod=Label(t, text='NUMBER OF DEATHS', borderwidth=2, relief="solid")
name1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
noi1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
nod1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

fir_no=Label(t, text='FIR', borderwidth=2, relief="solid")
poc=Label(t, text='PLACE OF CRIME', borderwidth=2, relief="solid")
fir_no1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
poc1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

OptionList=['1001','1020']
v = tk.StringVar(t)
v.set('CRIMINAL')
c_id= tk.OptionMenu(t, v, *OptionList)
doc=Label(t, text='DATE OF CRIME', borderwidth=2, relief="solid")
doc1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

OptionList2=['420','432','414']
OptionList3=['IPC','CRPC']
v2 = tk.StringVar(t)
v2.set('SECTION NO')
sn= tk.OptionMenu(t, v2, *OptionList2)
v3 = tk.StringVar(t)
v3.set('PENAL CODE')
pc=tk.OptionMenu(t, v3, *OptionList3)

da=Label(t, text='DAMAGE AMOUNT', borderwidth=2, relief="solid")
da1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
editt=Button(t, text='edit',command=edit, borderwidth=2, relief="solid")


name.place(x=50, y=150, width=150, height=70)
noi.place(x=400, y=150, width=150, height=70)
nod.place(x=750, y=150, width=150, height=70)
name1.place(x=225, y=150, width=150, height=70)
noi1.place(x=575, y=150, width=150, height=70)
nod1.place(x=925, y=150, width=150, height=70)
fir_no.place(x=100, y=50, width=200, height=70)

fir_no1.place(x=350, y=50, width=200, height=70)

poc.place(x=900, y=250, width=100, height=70)
poc1.place(x=1025, y=250, width=100, height=70)

pc.place(x=50, y=350, width=300, height=70)
sn.place(x=400, y=350, width=300, height=70)
c_id.place(x=600,y=50,width=300,height=70)


da.place(x=50, y=250, width=200, height=70)
da1.place(x=275, y=250, width=200, height=70)
doc.place(x=525,y=250,width=200,height=70)
doc1.place(x=750,y=250,width=100,height=70)
editt.place(x=1025, y=350, width=100, height=70)
mainloop()