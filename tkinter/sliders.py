from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title('Sabari Krishna M')
root.iconbitmap('icons and images/frankenstein.ico')
root.geometry("125x160")

def slide(x):
    root.geometry(str(hori.get())+'x'+str(vert.get()))

vert=Scale(root,from_=160,to=500,command=slide)
vert.grid(sticky=W)

hori=Scale(root,from_=125,to=500,orient=HORIZONTAL,command=slide)
hori.grid(sticky=W)

root.mainloop()
