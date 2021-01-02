from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title('Sabari')
root.iconbitmap('icons and images/frankenstein.ico')
frame=LabelFrame(root,padx=15,pady=15)
frame.pack(padx=30,pady=30)

b1=Button(frame,text='Click here')
b2=Button(frame,text='Second button')
b1.grid(row=0,column=0)
b2.grid(row=1,column=1)

root.mainloop()
