from tkinter import *
import tkinter as tk

import tkinter.messagebox
import tkinter.font as tkFont
import os
import sqlite3
from open_criminalacpsearch import test
from open_crimeacpsearch import best
from opern_caseacpsearch import fest
from open_criminaledit import*
connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()

root = tk.Tk()
root.geometry('400x400')
root.title("SEARCH")
cursor.execute('CREATE TABLE IF NOT EXISTS CIVILIAN1 (USERID text PRIMARY KEY, PASSWORD text NOT NULL, FNAME text, MNAME text, LNAME text, DOB date, GENDER text, MARITALSTATUS text, EMAILID text NOT NULL, OCCUPATION text, ADDRESS text, LASTLOGIN text, PHOTO blob)')
cursor.execute('CREATE TABLE IF NOT EXISTS CIVILIAN2 (USERID text PRIMARY KEY, CONTACT number)')

cursor.execute('CREATE TABLE IF NOT EXISTS COMPLAINT (COMPLAINT_NO text PRIMARY KEY, PLACEOFCRIME text, TIMEOFCRIME date, CRIMEDESCRIPTION text, CITY text, POLICESTATION text, STATUS text, VFNAME text, VMNAME text, VLNAME text, AFNAME text, AMNAME text, ALNAME text)')

cursor.execute("CREATE TABLE IF NOT EXISTS POLICE1 (POLICEID text PRIMARY KEY, PASSWORD text, FNAME text, MNAME text, LNAME text, DOB date, MARITALSTATUS text, EMAILID text, JURISDICTION TEXT, GENDER TEXT, BATCH TEXT, RANK TEXT,LASTLOGIN TEXT,PHOTO BLOB)")
cursor.execute("CREATE TABLE IF NOT EXISTS POLICE2 (POLICEID text, CONTACT number)")

cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL(CRIMINALID number PRIMARY KEY,FNAME text,MNAME text,LNAME text,DOB text,BLOODGROUP text,STATUS number,PRIORITY number,GENDER text,PHOTO BLOB)')
cursor.execute('CREATE TABLE IF NOT EXISTS CASE1(CASENO number PRIMARY KEY,PENALCODETYPE text,SECTIONNUMBER number,POLICESTATION text,DESCRIPTION text,STATUS number,OPENDATE text,CLOSEDATE text)')
cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL3(CRIMINALID number PRIMARY KEY,CONTACT text)')
cursor.execute('CREATE TABLE IF NOT EXISTS CASE2(CASENO number PRIMARY KEY,POLICEID)')
cursor.execute('CREATE TABLE IF NOT EXISTS CASE3(CASENO number PRIMARY KEY,VFNAME text,VMNAME text,VLNAME text,VAGE number,VADDRESS text)')
cursor.execute('CREATE TABLE IF NOT EXISTS CASE4(CASENO number PRIMARY KEY,FIRNO number)')
cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL2(CRIMINALID number PRIMARY KEY,ADDRESS text)')
cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL1(CRIMINALID number PRIMARY KEY,IDENTIFICATIONMARKS text)')
cursor.execute('CREATE TABLE IF NOT EXISTS CRIME2(FIRNO number PRIMARY KEY,CRIMINALID number)')
cursor.execute('CREATE TABLE IF NOT EXISTS CRIME3(FIRNO number PRIMARY KEY,PENALCODETYPE text,SECTIONNUMBER number)')
cursor.execute( 'CREATE TABLE IF NOT EXISTS CRIME(FIRNO number PRIMARY KEY,DAMAGEAMOUNT number,INJURED number,DEATHS number,DATEOFCRIME text,PLACEOFCRIME text)')
connection.commit()
OptionList = ['CRIMINAL ID', 'CASE ID', 'FIR NUMBER']
v = tk.StringVar(root)
v.set('SEARCH BY')
opt = tk.OptionMenu(root, v, *OptionList)
opt.place(x=100, y=100, width=200, height=70)

e1 = Entry(root, borderwidth=2, relief="solid")
e1.place(x=100, y=180, width=200, height=70)
x = e1.get()


def next():
    if v.get() == 'CRIMINAL ID':
        x = e1.get()
        u = cursor.execute('SELECT * FROM CRIMINAL where CRIMINALID=(?)', (x,))
        j = u.fetchall()
        r = cursor.execute('SELECT * FROM CRIMINAL1 where CRIMINALID=(?)', (x,))
        j1 = r.fetchall()

        q = cursor.execute('SELECT * FROM CRIMINAL2 where CRIMINALID=(?)', (x,))
        j2 = q.fetchall()
        p = cursor.execute('SELECT * FROM CRIMINAL3 where CRIMINALID=(?)', (x,))
        j3 = p.fetchall()

        photo = j[0][9]

        photoPath = "E:\z" + str(20180829_004758) + ".jpg"
        with open(photoPath, 'wb') as file:
            file.write(photo)
        print("Stored blob data into: ", photoPath, "\n")

        if len(j1) == 1:
            root.destroy()
            test(j,j1,j2,j3,photoPath)


        else:
            tkinter.messagebox.showinfo('Title', 'DOES NOT EXIST')
    elif v.get() == 'FIR NUMBER':
        x = e1.get()
        z = cursor.execute('SELECT * FROM CRIME where FIRNO=(?)', (x,))
        k = z.fetchall()
        z1=cursor.execute('SELECT * FROM CRIME2 where FIRNO=(?)', (x,))
        k1=z1.fetchall()
        z2=cursor.execute('SELECT * FROM CRIME3 where FIRNO=(?)', (x,))
        k2=z2.fetchall()
        if len(k) == 1:
            root.destroy()
            best(k,k1,k2)
        else:
            tkinter.messagebox.showinfo('Title', 'DOES NOT EXIST')


    elif v.get() == 'CASE ID':
        x = e1.get()
        w = cursor.execute('SELECT * FROM CASE1 where CASENO=(?)', (x,))
        i = w.fetchall()
        w1 = cursor.execute('SELECT * FROM CASE2 where CASENO=(?)', (x,))
        i1 = w1.fetchall()
        w2 = cursor.execute('SELECT * FROM CASE3 where CASENO=(?)', (x,))
        i2 = w2.fetchall()
        w3 = cursor.execute('SELECT * FROM CASE4 where CASENO=(?)', (x,))
        i3 = w3.fetchall()
        if len(i) == 1:
            root.destroy()
            fest(i,i1,i2,i3)
        else:
            tkinter.messagebox.showinfo('Title', 'DOES NOT EXIST')


    return


submit = Button(root, text='Submit', command=next, borderwidth=2, relief="solid")
submit.place(x=100, y=260, width=200, height=50)


def back():
    root.destroy()
    os.system('python acp_home.py')
    return


back = Button(root, text='<--', command=back, borderwidth=2, relief="solid")
back.place(x=20, y=20, width=50, height=30)
root.mainloop()