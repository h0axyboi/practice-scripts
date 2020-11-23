from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()
root.geometry('500x200')
root.title('Sabari')
root.iconbitmap('icons and images/frankenstein.ico')

def popup():
    #showinfo,showwarning,showerror,askquestion,askokcancel,askyesno
    inp=messagebox.askyesno('This is a message box','Hello World!')
    if inp==1:
        Label(root,text='You clicked yes!').pack()
    else:
        Label(root,text='You clicked no!').pack()

Button(root,text='Click',command=popup).pack()

mainloop()
