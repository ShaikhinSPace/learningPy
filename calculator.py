from tkinter import *
win = Tk()
win.title('Calculator')
win.geometry('515x400')
win.resizable(0,0)

def btn_clicl(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# function to clear input field
def btnclear():
    global expression
    expression = ""
    input_text.set("")
    
def equalbtn():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression= ""
    
expression =""
input_text = StringVar()

# input field frame

input_frame = Frame(win, width=312,height=50)
input_frame.pack(side=TOP)

input_field =Entry(input_frame, font=('arial',18,'bold'),width=45,justify=RIGHT,textvariable=input_text)
input_field.grid(row=0,column=0)

# increase the height of input field
input_field.pack(ipady=10)


# button frame

btns_frame =Frame(win,width=310,height=270)
btns_frame.pack()

# first row
clear = Button(btns_frame,text='C',width=38,height=3,command=lambda: btnclear()).grid(row=0,column=0,columnspan=3,padx=1,pady=1)
divide = Button(btns_frame, text='/',width=10,height=3,).grid(row=0,column=3,padx=1,pady=1)

#second row
seven = Button(btns_frame, text='7',width=10,height=3,command=lambda: btn_clicl(7)).grid(row=1,column=0,padx=1,pady=1)
eight = Button(btns_frame, text='8',width=10,height=3,command=lambda: btn_clicl(8)).grid(row=1,column=1,padx=1,pady=1)
nine = Button(btns_frame, text='9',width=10,height=3,command=lambda: btn_clicl(9)).grid(row=1,column=2,padx=1,pady=1)
multiply = Button(btns_frame, text='*',width=10,height=3,command=lambda: btn_clicl('*')).grid(row=1,column=3,padx=1,pady=1)


#third row
four = Button(btns_frame, text='4',width=10,height=3,command=lambda: btn_clicl(4)).grid(row=2,column=0,padx=1,pady=1)
five = Button(btns_frame, text='5',width=10,height=3,command=lambda: btn_clicl(5)).grid(row=2,column=1,padx=1,pady=1)
six = Button(btns_frame, text='6',width=10,height=3,command=lambda: btn_clicl(6)).grid(row=2,column=2,padx=1,pady=1)
subtract = Button(btns_frame, text='-',width=10,height=3,command=lambda: btn_clicl('-')).grid(row=2,column=3,padx=1,pady=1)


#fourth row
one = Button(btns_frame, text='1',width=10,height=3,command=lambda: btn_clicl(1)).grid(row=3,column=0,padx=1,pady=1)
two = Button(btns_frame, text='2',width=10,height=3,command=lambda: btn_clicl(2)).grid(row=3,column=1,padx=1,pady=1)
three = Button(btns_frame, text='3',width=10,height=3,command=lambda: btn_clicl(3)).grid(row=3,column=2,padx=1,pady=1)
add = Button(btns_frame, text='+',width=10,height=3,command=lambda: btn_clicl('+')).grid(row=3,column=3,padx=1,pady=1)


#fifth row
zero = Button(btns_frame, text='0',width=24,height=3,command=lambda: btn_clicl(0)).grid(row=4,column=0,columnspan=2 ,padx=1,pady=1)
dec = Button(btns_frame, text='.',width=10,height=3,command=lambda: btn_clicl('.')).grid(row=4,column=2,padx=1,pady=1)
equal = Button(btns_frame, text='=',width=10,height=3,command=lambda: equalbtn()).grid(row=4,column=3,padx=1,pady=1)

win.mainloop()