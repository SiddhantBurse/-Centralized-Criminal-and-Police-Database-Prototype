from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk
import os
import sqlite3
connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()

def add4():
    t = tk.Tk()
    t.title('CRIMINALADD')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))
    def add5():
        cursor.execute( 'CREATE TABLE IF NOT EXISTS CASE1(CASENO number PRIMARY KEY,PENALCODETYPE text,SECTIONNUMBER number,POLICESTATION text,DESCRIPTION text,STATUS number,OPENDATE text,CLOSEDATE text)')
        cursor.execute("INSERT INTO CASE1  VALUES(?,?,?,?,?,?,?,?)", (case_id1.get(), pno1.get(), sn1.get(), ps1.get(), desc1.get(), status1.get(), od1.get(), cd1.get()))
        connection.commit()
        cursor.execute('CREATE TABLE IF NOT EXISTS CASE2(CASENO number PRIMARY KEY,POLICEID)')
        cursor.execute("INSERT INTO CASE2 VALUES(?,?)", (case_id1.get(), pi1.get()))
        connection.commit()
        cursor.execute('CREATE TABLE IF NOT EXISTS CASE3(CASENO number PRIMARY KEY,VFNAME text,VMNAME text,VLNAME text,VAGE number,VADDRESS text)')
        cursor.execute("INSERT INTO CASE3 VALUES(?,?,?,?,?,?)", (case_id1.get(), victim1.get(),victim2.get(),victim3.get(),age1.get(),address1.get()))
        connection.commit()
        cursor.execute('CREATE TABLE IF NOT EXISTS CASE4(CASENO number PRIMARY KEY,FIRNO number)')
        cursor.execute("INSERT INTO CASE4 VALUES(?,?)", (case_id1.get(), fr1.get()))
        connection.commit()
        connection.close()
        tkinter.messagebox.showinfo('Confirmation', 'created')

    victim = Label(t, text='Name of victim', borderwidth=2, relief="solid")
    od = Label(t, text='OPENING DATE', borderwidth=2, relief="solid")
    address = Label(t, text='ADDRESS', borderwidth=2, relief="solid")
    victim1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                    relief="solid")
    victim2 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                    relief="solid")
    victim3 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                    relief="solid")
    od1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    address1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  relief="solid")
    # =Label(t, text='FIR', borderwidth=2, relief="solid")
    case_id = Label(t, text='CASE ID', borderwidth=2, relief="solid")
    status = Label(t, text='status', borderwidth=2, relief="solid")
    case_id1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                     relief="solid")
    status1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                    relief="solid")
    # =Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    desc = Label(t, text='DESCRIPTION', borderwidth=2, relief="solid")
    desc1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                  relief="solid")
    cd = Label(t, text='CLOSING DATE', borderwidth=2, relief="solid")
    cd1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    fr = Label(t, text='FIR NUMBER', borderwidth=2, relief="solid")
    fr1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    pi = Label(t, text='POLICE ID', borderwidth=2, relief="solid")
    pi1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    pno = Label(t, text='PENAL NUMBER', borderwidth=2, relief="solid")
    pno1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                 relief="solid")
    sn = Label(t, text='SECTION NUMBER', borderwidth=2, relief="solid")
    sn1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                relief="solid")
    # OptionList=[i3[0][1]]
    # v = tk.StringVar(t)
    # v.set('FIR NUMBER ')
    # fir= tk.OptionMenu(t, v, *OptionList)
    # OptionList2=[i1[0][1]]
    # OptionList3=[i[0][1]]
    # v2 = tk.StringVar(t)
    # v2.set('POLICE ID')
    # police_id= tk.OptionMenu(t, v2, *OptionList2)
    # v3 = tk.StringVar(t)
    # v3.set('PENAL NUMBER')
    # penal_no=tk.OptionMenu(t, v3, *OptionList3)
    ps = Label(t, text='POLICE STATION', borderwidth=2, relief="solid")
    ps1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    age = Label(t, text='AGE', borderwidth=2, relief="solid")
    age1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    submit = Button(t, text='submit', command=add5, borderwidth=2, relief="solid")

    victim.place(x=50, y=150, width=150, height=70)
    age.place(x=500, y=50, width=150, height=70)
    address.place(x=850, y=50, width=150, height=70)
    victim1.place(x=250, y=150, width=150, height=70)
    victim2.place(x=450, y=150, width=150, height=70)
    victim3.place(x=650, y=150, width=150, height=70)
    age1.place(x=680, y=50, width=150, height=70)
    address1.place(x=1025, y=50, width=150, height=70)
    case_id.place(x=50, y=50, width=175, height=70)
    fr.place(x=50, y=450, width=150, height=70)
    fr1.place(x=250, y=450, width=150, height=70)
    case_id1.place(x=275, y=50, width=200, height=70)
    pi.place(x=50, y=550, width=100, height=70)
    pi1.place(x=250, y=550, width=100, height=70)
    status.place(x=900, y=250, width=100, height=70)
    status1.place(x=1025, y=250, width=100, height=70)
    pno.place(x=450, y=450, width=100, height=70)
    pno1.place(x=575, y=450, width=100, height=70)
    sn.place(x=400, y=550, width=150, height=70)
    sn1.place(x=600, y=550, width=150, height=70)
    # marks.place(x=50, y=350, width=300, height=70)
    # address.place(x=400, y=350, width=300, height=70)
    # penal_no.place(x=50, y=650, width=200, height=70)
    desc.place(x=550, y=350, width=100, height=70)
    desc1.place(x=675, y=350, width=100, height=70)
    ps.place(x=50, y=350, width=200, height=70)
    ps1.place(x=275, y=350, width=200, height=70)
    od.place(x=50, y=250, width=200, height=70)
    od1.place(x=275, y=250, width=200, height=70)
    cd.place(x=525, y=250, width=200, height=70)
    cd1.place(x=750, y=250, width=100, height=70)
    submit.place(x=1175, y=550, width=100, height=70)