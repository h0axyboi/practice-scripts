from tkinter import *

def my_click():
    hello='Hello '+e.get()
    label1=Label(root,text=hello)
    label1.pack()

root=Tk()
e=Entry(root,width=70)
e.pack()
e.insert(0,'Enter your name:')
my_button=Button(root,text='Enter your name',command=my_click,padx=50,pady=10,fg='white',bg='grey')
my_button.pack()
root.mainloop()
