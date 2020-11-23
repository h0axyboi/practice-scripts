from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title('Sabari')
root.iconbitmap('icons and images/frankenstein.ico')

def open_pewds():
    global img
    top=Toplevel()
    top.title('Pewdiepie')
    top.iconbitmap('icons and images/plus_orange.ico')
    img=ImageTk.PhotoImage(Image.open('icons and images/pewdiepie.PNG'))
    Label(top,image=img).pack()
    Button(top,text='Close pewdiepie',command=top.destroy).pack()

Button(root,text='Open pewdiepie',command=open_pewds).pack()

mainloop()
