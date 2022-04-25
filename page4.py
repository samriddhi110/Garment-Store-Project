import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk

root= ThemedTk(theme='radiance')
root.title('dbms project')
root.geometry('430x500')
conn=sqlite3.connect('project_dbms.db')
c= conn.cursor()
"""
c.execute('''CREATE TABLE purchase(
		purchase_id integer PRIMARY KEY NOT NULL,
		customer_id integer NOT NULL,
		pid integer,
		quantity integer,
		amount integer,
		CONSTRAINT fkcid FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
		CONSTRAINT fkpid FOREIGN KEY(pid) REFERENCES product(pid)
		)''')

"""

def backpg():
    root.destroy()
    import page3

def nextpg():
    root.destroy()
    import loginpage

def save():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    record_id = delete_box.get()
    c.execute('''
    UPDATE purchase SET
    customer_id= :cid,
    purchase_id= :purchase,
    pid= :pid,
    quantity= :quantity,
    amount= :amount

    WHERE oid = :oid''',

    {
    "cid":cid_e.get(),
    "purchase":purchase_e.get(),
    "pid": pid_e.get(),
    "quantity": quantity_e.get(),
    "amount":amount_e.get(),

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
    check=c.execute('SELECT * FROM purchase').fetchall()

    if delete_box.get()== "":
        messagebox.showinfo("","PLEASE ENTER AN ID")
    elif delete_box.get() != "":
        for each in check:
            if str(each[0])== record_id:
                global editor
                editor= ThemedTk(theme='radiance')
                editor.title('Update Window')
                editor.geometry('450x400')
                   
                    
                c.execute("SELECT * FROM purchase WHERE oid = " + record_id)
                records=c.fetchall()

                 #global variables
                global purchase_e
                global cid_e
                global pid_e
                global quantity_e
                global amount_e

                #text boxes
                purchase_e = Entry(editor, width=30)
                purchase_e.grid(row=0, column=1)
                
                cid_e = Entry(editor, width=30)
                cid_e.grid(row=1, column=1, padx=20)

                pid_e = Entry(editor, width=30)
                pid_e.grid(row=2, column=1)

                quantity_e = Entry(editor, width=30)
                quantity_e.grid(row=3, column=1)

                amount_e = Entry(editor, width=30)
                amount_e.grid(row=4, column=1)


                #Text Labels
                purchase_label = ttk.Label(editor, text="Purchase ID")
                purchase_label.grid(row=0, column=0)
                
                cid_label = ttk.Label(editor, text="Customer ID")
                cid_label.grid(row=1, column=0)

                pid_label = ttk.Label(editor, text="Product ID")
                pid_label.grid(row=2, column=0)

                quantity_label = ttk.Label(editor, text="Quantity")
                quantity_label.grid(row=3, column=0)

                amount_label = ttk.Label(editor, text="Total Amount")
                amount_label.grid(row=4, column=0)

                for each in records:
                    purchase_e.insert(0,each[0])
                    cid_e.insert(0,each[1])
                    pid_e.insert(0,each[2])
                    quantity_e.insert(0,each[3])
                    amount_e.insert(0,each[4])

                    #save button
                save_btn = ttk.Button(editor, text="Save Record", command=save)
                save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
    else:
        messagebox.showinfo("","INVALID, ID DOESN'T EXIST")
    
    conn.commit()
    conn.close()

def delete():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    if delete_box.get()== "":
        messagebox.showinfo("","PLEASE ENTER AN ID")
    else:
        check=c.execute("SELECT * FROM purchase").fetchall()
        for each in check:
            if str(each[0])== delete_box.get():
                c.execute("DELETE from purchase WHERE oid = " +delete_box.get())
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
    c.execute("INSERT INTO purchase VALUES(:purchase,:cid,:pid, :quantity, :amount)",
			{
                                'purchase': purchase.get(),
                                'cid': cid.get(),
				'pid': pid.get(),
				'quantity': quantity.get(),
				'amount': amount.get()
			})
    
    conn.commit()
    conn.close()
    
    purchase.delete(0,END)
    cid.delete(0,END)
    pid.delete(0,END)
    quantity.delete(0,END)
    amount.delete(0,END)


#query function(show records)
def query():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    
    c.execute('SELECT * FROM purchase')#oid is the primary key assigned by
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
purchase = Entry(root, width=30)
purchase.grid(row=0, column=1)

cid = Entry(root, width=30)
cid.grid(row=1, column=1, padx=20)

pid = Entry(root, width=30)
pid.grid(row=2, column=1)

quantity = Entry(root, width=30)
quantity.grid(row=3, column=1)

amount = Entry(root, width=30)
amount.grid(row=4, column=1)



#Text Labels
purchase_label = ttk.Label(root, text="Purchase ID")
purchase_label.grid(row=0, column=0)
                
cid_label = ttk.Label(root, text="Customer ID")
cid_label.grid(row=1, column=0)

pid_label = ttk.Label(root, text="Product ID")
pid_label.grid(row=2, column=0)

quantity_label = ttk.Label(root, text="Quantity")
quantity_label.grid(row=3, column=0)

amount_label = ttk.Label(root, text="Total Amount")
amount_label.grid(row=4, column=0)

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

