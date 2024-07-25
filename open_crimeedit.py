from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import os
import sqlite3

def best1(k,k1,k2,):
    connection = sqlite3.connect('NCD.db')
    cursor = connection.cursor()
    t=tk.Tk()
    t.title('CRIME')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))

    def update_crime():
        cursor.execute("Update CRIME set FIRNO=? where FIRNO=?", (fir_no1.get(), k[0][0],))
        cursor.execute("Update CRIME set DAMAGEAMOUNT=? where FIRNO=?", (da1.get(), k[0][0],))
        cursor.execute("UPDATE CRIME set INJURED=?  where FIRNO=?", (noi1.get(), k[0][0],))
        cursor.execute("UPDATE CRIME set DEATHS=?  where FIRNO=?", (nod1.get(), k[0][0],))
        # cursor.execute("UPDATE CRIMINAL set Datee=?  where CRIMINALID=?", (dob1.get(), j,))
        # cursor.execute("UPDATE CRIMINAL set Monthh=?  where CRIMINALID=?", (dob1.get(), j,))
        # cursor.execute("UPDATE CRIMINAL set Year=?  where CRIMINALID=?", (dob1.get(), j,))
        cursor.execute("UPDATE CRIME set DATEOFCRIME=?  where FIRNO=?", (doc1.get(), k[0][0],))
        cursor.execute("UPDATE CRIME2 set CRIMINALID=? where FIRNO=?", (ci1.get(), k1[0][0],))
        cursor.execute("UPDATE CRIME3 set SECTIONNUMBER=? where FIRNO=?", (sn1.get(), k2[0][0],))
        cursor.execute("UPDATE CRIME3 set PENALCODETYPE =? where FIRNO=?", (pc1.get(), k2[0][0],))
        #cursor.execute("UPDATE CRIME set IDENTIFICATIONMARKS=? where CRIMINALID=?", (v.get(), j1[0][0],))
        #cursor.execute("UPDATE CRIMINAL2 set ADDRESS=? where CRIMINALID=?", (v2.get(), j2[0][0],))
        #cursor.execute("UPDATE CRIMINAL3 set CONTACT=? where CRIMINALID=?", (v3.get(), j3[0][0],))
        connection.commit()
    def delete():
        cursor.execute('DELETE from CRIME where FIRNO=?', (k[0][0],))
        connection.commit()
        cursor.execute('DELETE from CRIME2 where FIRNO=?', (k1[0][0],))
        connection.commit()
        cursor.execute('DELETE from CRIME3 where FIRNO=?', (k2[0][0],))
        connection.commit()



    fir = StringVar(t)
    daa = StringVar(t)
    ing = StringVar(t)
    de = StringVar(t)
    dc = StringVar(t)
    pcr = StringVar(t)
    cii = StringVar(t)
    snn = StringVar(t)
    pcc = StringVar(t)



    #name=Label(t, text='Victim name', borderwidth=2, relief="solid")
    noi=Label(t, text='NUMBER OF INJURIES',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    nod=Label(t, text='NUMBER OF DEATHS',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    #name1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    noi1=Entry(t,font=tkFont.Font(family="Times New Roman", size=16), textvariable=ing, borderwidth=2, relief="solid")
    nod1=Entry(t,font=tkFont.Font(family="Times New Roman", size=16),  textvariable=de, borderwidth=2, relief="solid")

    fir_no=Label(t, text='FIR',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    poc=Label(t, text='PLACE OF CRIME',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    fir_no1=Entry(t,font=tkFont.Font(family="Times New Roman", size=16),  textvariable=fir, borderwidth=2, relief="solid")
    poc1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30),textvariable=pcr, borderwidth=2, relief="solid")
    ci = Label(t, text='CRIMINAL ID',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    ci1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=16), textvariable=cii, borderwidth=2,
                 relief="solid")
    # OptionList=[k1[0][1]]
    #v = tk.StringVar(t)
    #v.set('CRIMINAL')
    #c_id= tk.OptionMenu(t, v, *OptionList)
    doc=Label(t, text='DATE OF CRIME',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    doc1=Entry(t,font=tkFont.Font(family="Times New Roman", size=16), textvariable=dc, borderwidth=2, relief="solid")
    sn = Label(t, text='SECTION NO',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    sn1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=16), textvariable=snn, borderwidth=2, relief="solid")
    pc = Label(t, text='PENAL CODE',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    pc1 = Entry(t, font=tkFont.Font(family="PENAL CODE", size=16), textvariable=pcc, borderwidth=2, relief="solid")
    #OptionList2=[k2[0][1]]
    #OptionList3=[k2[0][2]]
    #v2 = tk.StringVar(t)
    #v2.set('SECTION NO')
    #sn= tk.OptionMenu(t, v2, *OptionList2)
    #v3 = tk.StringVar(t)
    #v3.set('PENAL CODE')
    #pc=tk.OptionMenu(t, v3, *OptionList3)

    da=Label(t, text='DAMAGE AMOUNT',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    da1=Entry(t,font=tkFont.Font(family="Times New Roman", size=16), textvariable=daa,  borderwidth=2, relief="solid")
    delete=Button(t, text='delete',command=delete,font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    submit=Button(t,text='submit',command=update_crime,font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")

    fir.set(k[0][0])
    daa.set(k[0][1])
    ing.set(k[0][2])
    de.set(k[0][3])
    dc.set(k[0][4])
    # v.set(k1[0][1])
    #v2.set(k2[0][1])
    #v3.set(k2[0][1])
    pcr.set(k[0][5])
    cii.set(k1[0][1])
    pcc.set(k2[0][1])
    snn.set(k2[0][2])


    #name.place(x=50, y=150, width=150, height=70)
    noi.place(x=750, y=450, width=150, height=70)
    nod.place(x=750, y=350, width=150, height=70)
    #name1.place(x=225, y=150, width=150, height=70)
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
    ci.place(x=50,y=150,width=300,height=70)
    ci1.place(x=400, y=150, width=300, height=70)


    da.place(x=50, y=250, width=200, height=70)
    da1.place(x=275, y=250, width=200, height=70)
    doc.place(x=525,y=250,width=200,height=70)
    doc1.place(x=750,y=250,width=100,height=70)
    delete.place(x=1025, y=550, width=100, height=70)
    submit.place(x=1175, y=550, width=100, height=70)
    mainloop()