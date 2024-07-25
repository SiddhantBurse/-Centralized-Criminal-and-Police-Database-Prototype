from tkinter import*
import os
t=Tk()
t.title("UPDATE")
t.geometry("450x250")

def crime():
    os.system('python acp_updates_crime.py')
def criminal():
    os.system('python acp_updates_criminal.py')
def case():
    os.system('python acp_updates_case.py')

text1=Label(t, text="PLEASE SELECT THE FIELD TO UPDATE?")
text1.place(x=100,y=50,width=250,height=50)

criminal=Button(t,text="CRIMINAL", command = criminal, borderwidth=2,relief="solid")
criminal.place(x=10,y=90,width=120,height=50)


civilian=Button(t,text="CRIME", command=crime, borderwidth=2,relief="solid")
civilian.place(x=160,y=90,width=120,height=50)

case=Button(t,text="CASE",command = case, borderwidth=2,relief="solid")
case.place(x=320,y=90,width=120,height=50)

mainloop()
