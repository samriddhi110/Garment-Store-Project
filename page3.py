import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk

root= ThemedTk(theme='radiance')
root.title('dbms project')
root.geometry('430x500')
conn=sqlite3.connect('project_dbms.db')
c= conn.cursor()
"""
c.execute( '''CREATE TABLE stock(
    sid INT PRIMARY KEY,
    pid INT,
    pname TEXT,
    instock INT,
    CONSTRAINT fkpid FOREIGN KEY(pid) REFERENCES product(pid)
    );
    ''')
"""
def backpg():
    root.destroy()
    import page2

def nextpg():
    root.destroy()
    import page4

def save():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    record_id = delete_box.get()
    c.execute('''
    UPDATE stock SET
    sid= :sid,
    pid= :pid,
    pname= :pname,
    instock= :instock

    WHERE oid = :oid''',

    {
    "sid": sid_e.get(),
    "pid":pid_e.get(),
    "pname":pname_e.get(),
    "instock": instock_e.get(),

    "oid":record_id
    }
    )

    conn.commit()
    conn.close()
    editor.destroy()
    
def update():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    record_id = delete_box.get()
    check=c.execute('SELECT * FROM stock').fetchall()

    if delete_box.get()== "":
        messagebox.showinfo("","PLEASE ENTER AN ID")  
    else:
        for each in check:
            if str(each[0])== record_id:   
                global editor
                editor= ThemedTk(theme='radiance')
                editor.title('Update Window')
                editor.geometry('450x400')
                c.execute("SELECT * FROM stock WHERE oid = " + record_id)
                records=c.fetchall()

                #global variables
                global sid_e
                global pid_e
                global pname_e
                global instock_e

                #text boxes
                sid_e = Entry(editor, width=30)
                sid_e.grid(row=0, column=1)
                
                pid_e = Entry(editor, width=30)
                pid_e.grid(row=1, column=1, padx=20)

                pname_e = Entry(editor, width=30)
                pname_e.grid(row=2, column=1)

                instock_e = Entry(editor, width=30)
                instock_e.grid(row=3, column=1)


                #Text Labels
                sid_label = ttk.Label(editor, text="Supplier ID")
                sid_label.grid(row=0, column=0)

                pid_label = ttk.Label(editor, text="Product ID")
                pid_label.grid(row=1, column=0)

                pname_label = ttk.Label(editor, text="Stock Name")
                pname_label.grid(row=2, column=0)

                instock_label = ttk.Label(editor, text="Instock")
                instock_label.grid(row=3, column=0)


                for each in records:
                    sid_e.insert(0,each[0])
                    pid_e.insert(0,each[1])
                    pname_e.insert(0,each[2])
                    instock_e.insert(0,each[3])

                #save button
                save_btn = ttk.Button(editor, text="Save Record", command=save)
                save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
           # if str(each[0])!= record_id:
             #   messagebox.showinfo("","INVALID, ID DOESN'T EXIST")
        
    conn.commit()
    conn.close()

def delete():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    if delete_box.get()== "":
        messagebox.showinfo("","PLEASE ENTER AN ID")
    else:
        check=c.execute("SELECT * FROM stock").fetchall()
        for each in check:
            if str(each[0])== delete_box.get():
                c.execute("DELETE from stock WHERE oid = " +delete_box.get())
           # if str(each[0])!= delete_box.get():
             #   messagebox.showinfo("","INVALID, ID DOESN'T EXIST")        
    conn.commit()
    conn.close()
    delete_box.delete(0,END)

def select_id():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    global delete_box
    delete_box= Entry(root,width=30)
    delete_box.grid(row=9,column=1)
    delete_box_label= Label(root,text="Select ID")
    delete_box_label.grid(row=9,column=0)
    #Delete Button
    delete_btn = ttk.Button(root, text="Delete Record", command=delete)
    delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

    #Update Button
    update_btn = ttk.Button(root, text="Update Record", command=update)
    update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

    conn.commit()
    conn.close()

#submit function
def submit():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    c.execute("INSERT INTO stock VALUES(:sid, :pid, :pname, :instock)",
			{
                                'sid': sid.get(),
                                'pid': pid.get(),
				'pname': pname.get(),
				'instock': instock.get()
			})
    
    conn.commit()
    conn.close()
    
    sid.delete(0,END)
    pid.delete(0,END)
    pname.delete(0,END)
    instock.delete(0,END)


#query function(show records)
def query():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    
    c.execute('SELECT * FROM stock')#oid is the primary key assigned by
    #sqlite3(auto increment)
    records=c.fetchall()
    print(records)
    print_records=" "
    for each in records:
        print_records += str(each)+ "\n"
    query_label=Label(root,text=print_records)
    query_label.grid(row=16,column=0,columnspan=2)
    conn.commit()
    conn.close()

#text boxes
sid = Entry(root, width=30)
sid.grid(row=0, column=1)

pid = Entry(root, width=30)
pid.grid(row=1, column=1, padx=20)

pname = Entry(root, width=30)
pname.grid(row=2, column=1)

instock = Entry(root, width=30)
instock.grid(row=3, column=1)


#Text Labels
sid_label = ttk.Label(root, text="Supplier ID")
sid_label.grid(row=0, column=0,pady=2,padx=2)

pid_label = ttk.Label(root, text="Product ID")
pid_label.grid(row=1, column=0, pady=2,padx=2)

pname_label = ttk.Label(root, text="Product Name")
pname_label.grid(row=2, column=0,padx=2)

instock_label = ttk.Label(root, text="Instock")
instock_label.grid(row=3, column=0,padx=2)

submit_btn=ttk.Button(root, text="Add Record To Database",command= submit) 
submit_btn.grid(row=6,column=0,columnspan=2,pady=10, padx=10,ipadx=101)

#Show records Button
query_btn = ttk.Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#select_id button
select_btn = ttk.Button(root, text="Update Record", command=select_id)
select_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

next_btn = ttk.Button(root, text="Next", command=nextpg)
next_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=141)

back_btn = ttk.Button(root, text="Back", command=backpg)
back_btn.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=141)

conn.commit()
conn.close()
