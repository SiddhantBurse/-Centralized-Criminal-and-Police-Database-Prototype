from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk
import os
import sqlite3
connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()

def add1():
    t = tk.Tk()
    t.title('CRIMEADD')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))
    def add():
        cursor.execute('CREATE TABLE IF NOT EXISTS CRIME(FIRNO number PRIMARY KEY,DAMAGEAMOUNT number,INJURED number,DEATHS number,DATEOFCRIME text,PLACEOFCRIME text)')
        cursor.execute("INSERT INTO CRIME VALUES(?,?,?,?,?,?)", (fir_no1.get(), da1.get(), noi1.get(), nod1.get(), doc1.get(), poc1.get()))
        connection.commit()
        cursor.execute('CREATE TABLE IF NOT EXISTS CRIME2(FIRNO number PRIMARY KEY,CRIMINALID number)')
        cursor.execute("INSERT INTO CRIME2 VALUES(?,?)", (fir_no1.get(),ci1.get()))
        connection.commit()
        cursor.execute('CREATE TABLE IF NOT EXISTS CRIME3(FIRNO number PRIMARY KEY,PENALCODETYPE text,SECTIONNUMBER number)')
        cursor.execute("INSERT INTO CRIME3 VALUES(?,?,?)", (fir_no1.get(), pc1.get(),sn1.get()))
        connection.commit()
        connection.close()
        tkinter.messagebox.showinfo('Confirmation', 'created')

    noi=Label(t, text='NUMBER OF INJURIES', borderwidth=2, relief="solid")
    nod=Label(t, text='NUMBER OF DEATHS', borderwidth=2, relief="solid")
    #name1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    noi1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    nod1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")

    fir_no=Label(t, text='FIR', borderwidth=2, relief="solid")
    poc=Label(t, text='PLACE OF CRIME', borderwidth=2, relief="solid")
    fir_no1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30),   borderwidth=2, relief="solid")
    poc1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    ci = Label(t, text='CRIMINAL ID', borderwidth=2, relief="solid")
    ci1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2,
                 relief="solid")
    # OptionList=[k1[0][1]]
    #v = tk.StringVar(t)
    #v.set('CRIMINAL')
    #c_id= tk.OptionMenu(t, v, *OptionList)
    doc=Label(t, text='DATE OF CRIME', borderwidth=2, relief="solid")
    doc1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    sn = Label(t, text='SECTION NO', borderwidth=2, relief="solid")
    sn1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    pc = Label(t, text='PENAL CODE', borderwidth=2, relief="solid")
    pc1 = Entry(t, font=tkFont.Font(family="PENAL CODE", size=30),  borderwidth=2, relief="solid")
    #OptionList2=[k2[0][1]]
    #OptionList3=[k2[0][2]]
    #v2 = tk.StringVar(t)
    #v2.set('SECTION NO')
    #sn= tk.OptionMenu(t, v2, *OptionList2)
    #v3 = tk.StringVar(t)
    #v3.set('PENAL CODE')
    #pc=tk.OptionMenu(t, v3, *OptionList3)

    da=Label(t, text='DAMAGE AMOUNT', borderwidth=2, relief="solid")
    da1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")

    submit=Button(t,text='submit',command=add, borderwidth=2, relief="solid")
    # name.place(x=50, y=150, width=150, height=70)
    noi.place(x=750, y=450, width=150, height=70)
    nod.place(x=750, y=350, width=150, height=70)
    # name1.place(x=225, y=150, width=150, height=70)
    noi1.place(x=950, y=450, width=150, height=70)
    nod1.place(x=950, y=350, width=150, height=70)
    fir_no.place(x=50, y=50, width=200, height=70)

    fir_no1.place(x=280, y=50, width=200, height=70)

    poc.place(x=900, y=250, width=100, height=70)
    poc1.place(x=1025, y=250, width=100, height=70)

    pc.place(x=50, y=450, width=300, height=70)
    pc1.place(x=400, y=450, width=300, height=70)
    sn.place(x=50, y=350, width=300, height=70)
    sn1.place(x=400, y=350, width=300, height=70)
    ci.place(x=50, y=150, width=300, height=70)
    ci1.place(x=400, y=150, width=300, height=70)

    da.place(x=50, y=250, width=200, height=70)
    da1.place(x=275, y=250, width=200, height=70)
    doc.place(x=525, y=250, width=200, height=70)
    doc1.place(x=750, y=250, width=100, height=70)

    submit.place(x=1175, y=550, width=100, height=70)
    mainloop()

