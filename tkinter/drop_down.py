from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title('Sabari Krishna M')
root.iconbitmap('icons and images/frankenstein.ico')
root.geometry('400x400')

def display():
    l=Label(root,text=x.get()).pack()

weekdays=['Mon','Tue','Wed','Thu','Fri']

x=StringVar()
x.set(weekdays[0])

drop=OptionMenu(root,x,*weekdays)
drop.pack()

b=Button(root,text='Show day of the week',command=display).pack()

root.mainloop()
