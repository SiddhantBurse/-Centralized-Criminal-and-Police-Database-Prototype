from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
from open_crimeedit import*
import os


def best(k,k1,k2):
    t=tk.Tk()
    t.title('CRIME')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))

    def edit():
       # t.destroy()
       best1(k,k1,k2)
       #os.system('python open_crimeedit.py')
       #return

    noi=Label(t, text='NUMBER OF INJURIES',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    nod=Label(t, text='NUMBER OF DEATHS',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")

    noi1=Label(t,text=k[0][2],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    nod1=Label(t,text=k[0][3],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")

    fir_no=Label(t, text='FIR NUMBER',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    poc=Label(t, text='PLACE OF CRIME',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    fir_no1=Label(t,text=k[0][0],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    poc1=Label(t,text=k[0][5],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")

    OptionList=[k1[0][1]]
    v = tk.StringVar(t)
    v.set('CRIMINAL ID')
    c_id= tk.OptionMenu(t, v, *OptionList)
    doc=Label(t, text='DATE OF CRIME',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    doc1=Label(t,text=k[0][4],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")

    OptionList2=[k2[0][2]]
    OptionList3=[k2[0][1]]
    v2 = tk.StringVar(t)
    v2.set('SECTION NO')
    sn= tk.OptionMenu(t, v2, *OptionList2)
    v3 = tk.StringVar(t)
    v3.set('PENAL CODE')
    pc=tk.OptionMenu(t, v3, *OptionList3)

    da=Label(t, text='DAMAGE AMOUNT',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    da1=Label(t,text=k[0][1],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    editt = Button(t, text='edit',font=tkFont.Font(family="Times New Roman", size=16), command=edit, borderwidth=2, relief="solid")



    noi.place(x=50, y=150, width=150, height=70)
    nod.place(x=500, y=150, width=150, height=70)

    noi1.place(x=275, y=150, width=150, height=70)
    nod1.place(x=700, y=150, width=150, height=70)
    fir_no.place(x=50, y=50, width=200, height=70)

    fir_no1.place(x=275, y=50, width=200, height=70)

    poc.place(x=900, y=250, width=100, height=70)
    poc1.place(x=1025, y=250, width=100, height=70)

    pc.place(x=50, y=350, width=300, height=70)
    sn.place(x=375, y=350, width=300, height=70)
    c_id.place(x=700,y=350,width=300,height=70)


    da.place(x=50, y=250, width=200, height=70)
    da1.place(x=275, y=250, width=200, height=70)
    doc.place(x=525,y=250,width=200,height=70)
    doc1.place(x=750,y=250,width=100,height=70)
    editt.place(x=1025, y=350, width=100, height=70)

    mainloop()