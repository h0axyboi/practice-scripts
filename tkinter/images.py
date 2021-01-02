from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('Learn to code at codemy')
root.iconbitmap('icons and images/frankenstein.ico')

img1=ImageTk.PhotoImage(Image.open('icons and images/pewdiepie.PNG'))
img2=ImageTk.PhotoImage(Image.open('icons and images/sonic.PNG'))
img3=ImageTk.PhotoImage(Image.open('icons and images/sugoi.PNG'))
img4=ImageTk.PhotoImage(Image.open('icons and images/kars.PNG'))

img_list=[img1, img2, img3, img4]

status=Label(root,text='Image 1 of '+str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)

my_label=Label(image=img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(img_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label=Label(image=img_list[img_number-1])
    button_forward=Button(root,text='>>',command=lambda: forward(img_number+1))
    button_back=Button(root,text='<<',command=lambda: back(img_number-1))
    status=Label(root,text='Image '+str(img_number)+' of '+str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)

    if(img_number==4):
        button_forward=Button(root,text='>>',state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)


def back(img_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label=Label(image=img_list[img_number-1])
    button_forward=Button(root,text='>>',command=lambda: forward(img_number+1))
    button_back=Button(root,text='<<',command=lambda: back(img_number-1))
    status=Label(root,text='Image '+str(img_number)+' of '+str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)


    if(img_number==1):
        button_back=Button(root,text='<<',state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)


button_back=Button(root,text='<<',state=DISABLED)
button_exit=Button(root,text='Exit program',command=root.quit)
button_forward=Button(root,text='>>',command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

root.mainloop()
