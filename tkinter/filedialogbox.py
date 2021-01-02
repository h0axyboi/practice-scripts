from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root=Tk()
root.title('Sabari')
root.iconbitmap('icons and images/frankenstein.ico')

def choose_file():
    root.filename=filedialog.askopenfilename(initialdir='c:',title='Select an image',filetypes=(('png files','*.png'),('all files','*.*')))
    Label(root,text='Chosen file: '+root.filename).pack(padx=5,pady=5)

def open_image():
    global img
    img=ImageTk.PhotoImage(Image.open(root.filename))
    top=Toplevel()
    Label(top,image=img).pack()
    Button(top,text='Close image',command=top.destroy).pack(padx=5,pady=5)

Button(root,text='Choose an image',command=choose_file).pack(padx=5,pady=5)
Button(root,text='Open the image',command=open_image).pack(padx=5,pady=5)

mainloop()
