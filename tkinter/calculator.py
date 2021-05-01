from tkinter import *
import math


root=Tk()
root.title('Simple Calculator')
sum=0
math=''
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,current+str(number))

def button_clear():
    e.delete(0,END)

def button_equal():
    global sum
    if math=='addition':
        sum=f_num+float(e.get())
    elif math=='subtraction':
        sum=f_num-float(e.get())
    elif math=='multiplication':
        sum=f_num*float(e.get())
    else:
        sum=f_num/float(e.get())
    if sum==int(sum):
        sum=int(sum)
    e.delete(0,END)
    e.insert(0,sum)

def button_add():
    global sum
    global math
    math='addition'
    global f_num
    f_num=float(e.get())
    e.delete(0,END)

def button_subtract():
    global sum
    global math
    math='subtraction'
    global f_num
    f_num=float(e.get())
    e.delete(0,END)

def button_multiply():
    global sum
    global math
    math='multiplication'
    global f_num
    f_num=float(e.get())
    e.delete(0,END)

def button_divide():
    global sum
    global math
    math='division'
    global f_num
    f_num=float(e.get())
    e.delete(0,END)

e=Entry(root,width=45,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

b_1=Button(root,text='1',padx=40,pady=20,command=lambda: button_click(1))
b_2=Button(root,text='2',padx=40,pady=20,command=lambda: button_click(2))
b_3=Button(root,text='3',padx=40,pady=20,command=lambda: button_click(3))
b_4=Button(root,text='4',padx=40,pady=20,command=lambda: button_click(4))
b_5=Button(root,text='5',padx=40,pady=20,command=lambda: button_click(5))
b_6=Button(root,text='6',padx=40,pady=20,command=lambda: button_click(6))
b_7=Button(root,text='7',padx=40,pady=20,command=lambda: button_click(7))
b_8=Button(root,text='8',padx=40,pady=20,command=lambda: button_click(8))
b_9=Button(root,text='9',padx=40,pady=20,command=lambda: button_click(9))
b_0=Button(root,text='0',padx=40,pady=20,command=lambda: button_click(0))
b_add=Button(root,text='+',padx=39,pady=20,command=button_add)
b_equal=Button(root,text='=',padx=90,pady=20,command=button_equal)
b_clear=Button(root,text='Clear',padx=80,pady=20,command=button_clear)

b_subtract=Button(root,text='-',padx=41,pady=20,command=button_subtract)
b_multiply=Button(root,text='x',padx=40,pady=20,command=button_multiply)
b_divide=Button(root,text='/',padx=42,pady=20,command=button_divide)

b_1.grid(row=3,column=0)
b_2.grid(row=3,column=1)
b_3.grid(row=3,column=2)

b_4.grid(row=2,column=0)
b_5.grid(row=2,column=1)
b_6.grid(row=2,column=2)

b_7.grid(row=1,column=0)
b_8.grid(row=1,column=1)
b_9.grid(row=1,column=2)

b_0.grid(row=4,column=0)
b_add.grid(row=5,column=0)
b_equal.grid(row=5,column=1,columnspan=2)
b_clear.grid(row=4,column=1,columnspan=2)

b_subtract.grid(row=6,column=0)
b_multiply.grid(row=6,column=1)
b_divide.grid(row=6,column=2)

root.mainloop()
