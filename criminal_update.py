from tkinter import *
import tkinter as tk
import os
root = tk.Tk()
root.geometry('400x400')
root.title("UPDATE")
def next():
    if v.get()=='CRIMINAL ID' and e1.get()=='786':
        os.system('python open_criminal.py')
    elif v.get()=='FIR NUMBER' and e1.get()=='343':
        os.system('python open_crime.py')
    elif v.get()=='CASE ID' and e1.get()=='A123':
        os.system('python open_criminal.py')
    return

def back():
    root.destroy()
    os.system('python acp_home.py')
    return

OptionList=['CRIMINAL ID','CASE ID','FIR NUMBER','CRIMINAL NAME']
v = tk.StringVar(root)
v.set('UPDATE BY')
opt = tk.OptionMenu(root, v, *OptionList)
opt.place(x=100,y=100,width=200,height=70)

e1=Entry(root, borderwidth=2, relief="solid")
e1.place(x=100,y=180,width=200,height=70)

submit=Button(root, text='Submit', command=next ,borderwidth=2, relief="solid")
submit.place(x = 100, y =260, width=200, height=50)

back=Button(root, text = '<--', command=back,borderwidth=2, relief="solid")
back.place(x=20,y=20,width=50,height=30)
root.mainloop()