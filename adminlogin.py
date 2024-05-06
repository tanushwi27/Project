from tkinter import *
from tkinter import messagebox
import sqlite3
import os

root=Tk()
root.geometry("700x600")
root.title("Admin Login Screen")

txtaname=StringVar()
txtuname=StringVar()
txtpass=StringVar()

def login_clicked():
    con=sqlite3.connect("mydatabase.sqlite")
    c=con.cursor()
    u=txtuname.get()
    p=txtpass.get()
    c.execute("select * from adminlogin where username=? and password=?",(u,p))
    datalist=c.fetchall()
    if len(datalist)==0:
        messagebox.showinfo("Alert","Username does not exit..Register first")
        clear_clicked()
        t1.focus()
    else:
        messagebox.showinfo("Congrats","Login successful..")
    con.close()

def create_clicked():
    root.destroy()
    os.system("newadminlogin.py")

def exit_clicked():
    root.destroy()

def clear_clicked():
    txtaname.set("")
    txtuname.set("")
    txtpass.set("")


l0=Label(root,text="Login Screen")
l1=Label(root,text="Enter Username")
l2=Label(root,text="Enter Password")
t1=Entry(root,textvariable=txtuname)
t2=Entry(root,textvariable=txtpass,show="*")
l0.place(x=250,y=50)
l1.place(x=150,y=150)
l2.place(x=150,y=250)
t1.place(x=350,y=150)
t2.place(x=350,y=250)

b0=Button(root,text="Login",command=login_clicked)
b1=Button(root,text="New Admin Login",command=create_clicked)
b2=Button(root,text="Clear",command=clear_clicked)
b3=Button(root,text="Exit",command=exit_clicked)
b0.place(x=150,y=450)
b1.place(x=200,y=450)
b2.place(x=330,y=450)
b3.place(x=380,y=450)
t1.focus()
root.mainloop()

