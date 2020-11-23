from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title('Use of radio buttons')
root.iconbitmap('icons and images/frankenstein.ico')

pizza=StringVar()
pizza.set('Pepperoni')

toppings=[
'Pepperoni',
'Mushroom',
'Chicken',
'Cheese'
]

for topping in toppings:
    Radiobutton(root,text=topping,variable=pizza,value=topping).pack(anchor=W)

def clicked(value):
    my_label=Label(root,text=pizza.get())
    my_label.pack()

b1=Button(root,text='Update',command=lambda: clicked(pizza.get()))
b1.pack()

root.mainloop()
