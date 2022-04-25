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
c.execute( '''CREATE TABLE product(
    pid INT PRIMARY KEY,
    pname TEXT,
    brand TEXT,
    price INT NOT NULL);
    ''')

c.execute("INSERT INTO product( pid, pname, brand, price)\
        VALUES (1,'dress','zara', 3000)");

c.execute("INSERT INTO product( pid, pname, brand, price)\
        VALUES (2,'shirt','zara', 2000)");

c.execute("INSERT INTO product( pid, pname, brand, price)\
        VALUES (3,'hoodie','H & M', 2999)");
"""

def backpg():
    root.destroy()
    import page1
def nextpg():
    root.destroy()
    import page3

def save():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    record_id = delete_box.get()
    c.execute("""
    UPDATE product SET
    pid= :pid,
    pname= :pname,
    brand= :brand,
    price= :price

    WHERE oid = :oid""",

    {
    "pid":pid_e.get(),
    "pname":pname_e.get(),
    "brand": brand_e.get(),
    "price": price_e.get(),

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
    check=c.execute('SELECT * FROM product').fetchall()
    flag=0
    if delete_box.get()== "":
        messagebox.showinfo("","PLEASE ENTER AN ID")  
    else:
        for i in check:
            if str(i[0])== record_id:
                global editor
                editor= ThemedTk(theme='radiance')
                editor.title('Update Window')
                editor.geometry('450x400')

                c.execute("SELECT * FROM product WHERE oid = " + record_id);
                records=c.fetchall()

                #global variables
                global pid_e
                global pname_e
                global brand_e
                global price_e

                #text boxes
                pid_e = Entry(editor, width=30)
                pid_e.grid(row=0, column=1, padx=20)

                pname_e = Entry(editor, width=30)
                pname_e.grid(row=1, column=1)

                brand_e = Entry(editor, width=30)
                brand_e.grid(row=2, column=1)

                price_e = Entry(editor, width=30)
                price_e.grid(row=3, column=1)


                #Text Labels
                pid_label = ttk.Label(editor, text="Product ID")
                pid_label.grid(row=0, column=0)

                pname_label = ttk.Label(editor, text="Product Name")
                pname_label.grid(row=1, column=0)

                brand_label = ttk.Label(editor, text="Brand Name")
                brand_label.grid(row=2, column=0)

                price_label = ttk.Label(editor, text="Price")
                price_label.grid(row=3, column=0)


                for each in records:
                    pid_e.insert(0,each[0])
                    pname_e.insert(0,each[1])
                    brand_e.insert(0,each[2])
                    price_e.insert(0,each[3])

                #save button
                save_btn = ttk.Button(editor, text="Save Record", command=save)
                save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
       # messagebox.showinfo("","INVALID, ID DOESN'T EXIST")
    conn.commit()
    conn.close()

def delete():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    if delete_box.get()== "":
        messagebox.showinfo("","PLEASE ENTER AN ID")
    else:
        check=c.execute("SELECT * FROM product").fetchall()
        for each in check:
            if str(each[0])== delete_box.get():
                c.execute("DELETE from product WHERE oid = " +delete_box.get())
                break
        #messagebox.showinfo("","INVALID, ID DOESN'T EXIST")
    conn.commit()
    conn.close()
    delete_box.delete(0,END)

def select_id():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    global delete_box
    delete_box= Entry(root,width=30)
    delete_box.grid(row=9,column=1)
    delete_box_label= ttk.Label(root,text="Select ID")
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
    c.execute("INSERT INTO product VALUES(:pid, :pname, :brand, :price)",
			{
                                'pid': pid.get(),
				'pname': pname.get(),
				'brand': brand.get(),
				'price': price.get()
			})
    
    conn.commit()
    conn.close()
    
    pid.delete(0,END)
    pname.delete(0,END)
    brand.delete(0,END)
    price.delete(0,END)


#query function(show records)
def query():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    
    c.execute('SELECT * FROM product')#oid is the primary key assigned by
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
pid = Entry(root, width=30)
pid.grid(row=0, column=1, padx=20)

pname = Entry(root, width=30)
pname.grid(row=1, column=1)

brand = Entry(root, width=30)
brand.grid(row=2, column=1)

price = Entry(root, width=30)
price.grid(row=3, column=1)


#Text Labels
pid_label = ttk.Label(root, text="Product ID")
pid_label.grid(row=0, column=0, pady=2,padx=2)

pname_label = ttk.Label(root, text="Product Name")
pname_label.grid(row=1, column=0,padx=2)

brand_label = ttk.Label(root, text="Brand Name")
brand_label.grid(row=2, column=0,pady=2,padx=2)

price_label = ttk.Label(root, text="Price")
price_label.grid(row=3, column=0,padx=2)

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

