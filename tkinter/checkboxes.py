from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title('Sabari Krishna M')
root.iconbitmap('icons and images/frankenstein.ico')
root.geometry('400x400')

def display():
    l=Label(root,text=x.get()).pack()

x=StringVar()
c=Checkbutton(root,text='Check me',variable=x,onvalue='On',offvalue='Off')
c.deselect()
c.pack()

b=Button(root,text='Click me',command=display).pack()

root.mainloop()
