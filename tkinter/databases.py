from tkinter import *
from PIL import Image,ImageTk
import sqlite3

root=Tk()
root.title('Sabari Krishna M')
root.iconbitmap('icons and images/frankenstein.ico')
root.geometry('400x400')

conn=sqlite3.connect('address_book.db')
c=conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS addresses(
first_name text,
last_name text,
address text,
city text,
state text,
zipcode integer
)
""")

def submit():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()

    c.execute('INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)',
                {
                    'f_name':f_name.get(),
                    'l_name':l_name.get(),
                    'address':address.get(),
                    'city':city.get(),
                    'state':state.get(),
                    'zipcode':zipcode.get()
                }
            )

    conn.commit()
    conn.close()

    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

def query():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()

    c.execute('SELECT *,oid FROM addresses')
    records=c.fetchall()
    print_record=''
    for record in records:
        print_record+=str(record)+'\n'
    query_label=Label(root ,text=print_record)
    query_label.grid(row=9,column=0,columnspan=2)

    conn.commit()
    conn.close()

def clear():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    c.execute('DELETE FROM addresses')
    conn.commit()
    conn.close()

#Creating text boxes
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)
address=Entry(root,width=30)
address.grid(row=2,column=1,padx=20)
city=Entry(root,width=30)
city.grid(row=3,column=1,padx=20)
state=Entry(root,width=30)
state.grid(row=4,column=1,padx=20)
zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20)

#Create text box labels
f_name_label=Label(root,text='First Name')
f_name_label.grid(row=0,column=0)
l_name_label=Label(root,text='Last Name')
l_name_label.grid(row=1,column=0)
address_label=Label(root,text='Address')
address_label.grid(row=2,column=0)
city_label=Label(root,text='City')
city_label.grid(row=3,column=0)
state_label=Label(root,text='State')
state_label.grid(row=4,column=0)
zipcode_label=Label(root,text='Zipcode')
zipcode_label.grid(row=5,column=0)

#Create Submit button
submit_btn=Button(root,text='Add entry to the database', command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=100)

#Create query button
query_btn=Button(root,text='Show records',command=query)
query_btn.grid(row=7,column=0,columnspan=2,padx=10,ipadx=137)

#Clear databse
clear_btn=Button(root,text='Clear database',command=clear)
clear_btn.grid(row=8,column=0,columnspan=2)

root.mainloop()
