from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
import os
import sqlite3
from add_crime import*
from add_criminal import*
from add_case import*



root = tk.Tk()
root.geometry('400x400')
root.title("ADD")
OptionList = ['CRIMINAL', 'CASE', 'FIR']
v = tk.StringVar(root)
v.set('ADD BY')
opt = tk.OptionMenu(root, v, *OptionList)
opt.place(x=100, y=100, width=200, height=70)

def nex():
    if v.get()=='FIR':
        add1()
    elif v.get()=='CRIMINAL':
        add2()
    elif v.get() == 'CASE':
        add4()
    else:
        tkinter.messagebox.showinfo('Title', 'DOES NOT EXIST')
submit = Button(root, text='Submit', command=nex, borderwidth=2, relief="solid")
submit.place(x=100, y=260, width=200, height=50)
mainloop()

