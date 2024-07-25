from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
from open_caseedit import*
import os



def fest(i,i1,i2,i3):
    t=tk.Tk()
    t.title('CASE')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))

    def edit():
        t.destroy()
        fest1(i, i1, i2, i3)
        #os.system('python open_caseedit.py')
        #return
    victim=Label(t, text='Name of victim',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    od=Label(t, text='OPENING DATE',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    address=Label(t, text='CASE ID',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    victim1=Label(t,text=i2[0][1],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    od1=Label(t,text=i[0][6],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    address1=Label(t,text=i2[0][5],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")

    case_id=Label(t, text='Criminal ID',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    status=Label(t, text='status',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    case_id1=Label(t,text=i2[0][0],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    status1=Label(t,text=i[0][5],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")

    desc=Label(t, text='DESCRIPTION',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    desc1=Label(t,text=i[0][4],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    cd=Label(t, text='CLOSING DATE',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    cd1=Label(t,text=i[0][7],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    OptionList=[i3[0][1]]
    v = tk.StringVar(t)
    v.set('FIR NUMBER ')
    fir= tk.OptionMenu(t, v, *OptionList)
    OptionList2=[i1[0][1]]
    OptionList3=[i[0][1]]
    v2 = tk.StringVar(t)
    v2.set('POLICE ID')
    police_id= tk.OptionMenu(t, v2, *OptionList2)
    v3 = tk.StringVar(t)
    v3.set('PENAL NUMBER')
    penal_no=tk.OptionMenu(t, v3, *OptionList3)
    ps=Label(t, text='POLICE STATION',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    ps1=Label(t,text=i[0][3],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    age=Label(t, text='AGE',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    age1=Label(t,text=i2[0][4] ,font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    editt = Button(t, text='edit',font=tkFont.Font(family="Times New Roman", size=16), command=edit, borderwidth=2, relief="solid")

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