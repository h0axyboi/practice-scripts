from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('Basic Adding Application')
root.iconbitmap('icons and images/plus_orange.ico')

def add(a,b):
    sum=float(a)+float(b)
    if int(sum)==sum:
        sum=int(sum)
    e3.delete(0,END)
    e3.insert(0,sum)

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)

frame=LabelFrame(root,text='Addition',padx=5,pady=5)
frame.pack(padx=15,pady=15)

e1=Entry(frame,width=15,borderwidth=3)
e1.grid(row=0,column=0,padx=5,pady=5)

plus=Label(frame,text='+')
plus.grid(row=0,column=1,padx=5,pady=5)

e2=Entry(frame,width=15,borderwidth=3)
e2.grid(row=0,column=2,padx=5,pady=5)

b1=Button(frame,text='Add',padx=5,pady=5,command=lambda: add(e1.get(),e2.get()))
b1.grid(row=1,column=0,padx=5,pady=5,columnspan=3)

e3=Entry(frame,width=15,borderwidth=3)
e3.grid(row=2,column=0,padx=5,pady=5,columnspan=3)

b2=Button(frame,text='Clear everything',padx=5,pady=5,command='clear()')
b2.grid(row=3,column=0,columnspan=3,padx=5,pady=5)

root.mainloop()
