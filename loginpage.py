import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk

root=ThemedTk(theme='radiance')
root.title("Login")
root.geometry("370x200")

def login():
    username=entry1.get()
    password=entry2.get()

    if(username=="samriddhi" and password=="admin"):
        messagebox.showinfo("","Login Success")
        root.destroy()
        import page1
    elif(username=="" and password==""):
        messagebox.showinfo("","Blank Not Allowed")
        
    else:
        messagebox.showinfo("","Incorrect Username or Password")

global entry1
global entry2


ttk.Label(root,text="Username").place(x=70,y=20)
ttk.Label(root,text="Password").place(x=70,y=70)

entry1=Entry(root)
entry1.place(x=140,y=20)

entry2=Entry(root,show="*")
entry2.place(x=140,y=70)

ttk.Button(root,text="Login", command=login).place(x=135,y=120)
root.mainloop()
