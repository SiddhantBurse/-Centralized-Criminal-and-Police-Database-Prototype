import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter as tk
t=tk.Tk()
t.title('Employee Details Entry Form')
t.geometry('300x200')
connection=sqlite3.connect('lab8.db')
cursor=connection.cursor()
def reset():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    v2.set('Select Designation')
    return
def create():
    cursor.execute('CREATE TABLE IF NOT EXISTS emp(name TEXT, id NUMBER PRIMARY KEY, org TEXT, desig TEXT, salary REAL)')
    print('Table Creation : Successful')
def entries():
    cursor.execute('INSERT INTO emp VALUES(?,?,?,?,?)',(e2.get(),int(e1.get()), e3.get(), v2.get(), float(e4.get())))
    connection.commit()
    reset()
    print('Data Entry : Successful')
def show():
    t.destroy()
    cursor.execute("SELECT * FROM emp WHERE desig='Analyst'")
    for row in cursor.fetchall():
        print(row)
create()
Label(t, text='ID : ').grid(row=2, column=0)
Label(t, text='Name : ').grid(row=3, column=0)
Label(t, text='Organization : ').grid(row=4, column=0)
OptionList = ['Tester','Programmer','Analyst']
v2 = tk.StringVar(t)
v2.set('Select Designation')
Label(t, text='Designation : ').grid(row=5, column=0)
opt = tk.OptionMenu(t, v2, *OptionList).grid(sticky='w', row=5, column = 1)
Label(t, text='Salary : ').grid(row=6, column=0)
e1=Entry(t)
e1.grid(row=2,column=1)
e2=Entry(t)
e2.grid(row=3,column=1)
e3=Entry(t)
e3.grid(row=4,column=1)
e4=Entry(t)
e4.grid(row=6,column=1)
Button(t,text='Submit Details', command=entries).grid(row=7, column=1)
Button(t,text='Show Analysts', command=show).grid(row=8, column=1)
mainloop()
