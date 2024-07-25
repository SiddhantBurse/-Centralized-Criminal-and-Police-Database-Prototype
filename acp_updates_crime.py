from tkinter import*
t=Tk()
t.title("civilian id entry")

t.geometry("500x250")

cid=Label(t, text="CRIME ID",borderwidth=2,relief="solid")
cid.place(x=100,y=100,width=150,height=70)
e1=Entry(t)
e1.place(x=270,y=100,width=150,height=70)



sub=Button(t, text="SUBMIT",borderwidth=2,relief="solid")
sub.place(x=200,y=190,width=130,height=50)
mainloop()