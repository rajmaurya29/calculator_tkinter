from tkinter import *
root =Tk()
root.title("Calculator")

root.geometry('291x380')

root.resizable(0,0)

root.configure(bg='black')

first=second=None

def get_digit(num):
    new=result_label['text']
    new=str(new)+str(num)
    result_label.config(text=new)

def get_clear():
    result_label.config(text='')

def get_opr(operator):
    global first,second
    first=result_label['text']
    result_label.config(text='')
    second=operator

def get_equal():
    third=result_label['text']
    global first,second
    if second=='+':
        new=int(first)+int(third)
        result_label.config(text=str(new))
    elif second=='-':
        new=int(first)-int(third)
        result_label.config(text=str(new))
    elif second=='*':
        new=int(first)*int(third)
        result_label.config(text=str(new))
    elif second=='/':
        if third=='0':
            result_label.config(text="error")
        else:
            new=round(int(first)/int(third),2)
            result_label.config(text=str(new))

result_label=Label(root,text='',bg='black',fg='white',width=12,height=2,anchor='e')
result_label.grid(row=0,column=0,columnspan=5,sticky='e')
result_label.config(font=('verdana',30,'bold'))



bt9=Button(root,text='9',bg='green',fg='white',width=4,height=2,command=lambda:get_digit('9'))
bt9.grid(row=1,column=0)
bt9.config(font=('verdana',14,'bold'))

bt8=Button(root,text='8',bg='green',fg='white',width=4,height=2,command=lambda:get_digit('8'))
bt8.grid(row=1,column=1)
bt8.config(font=('verdana',14,'bold'))

bt7=Button(root,text='7',bg='green',fg='white',width=4,height=2,command=lambda:get_digit('7'))
bt7.grid(row=1,column=2)
bt7.config(font=('verdana',14,'bold'))

bt_add=Button(root,text='+',bg='green',fg='white',width=4,height=2,command=lambda:get_opr('+'))
bt_add.grid(row=1,column=3)
bt_add.config(font=('verdana',14,'bold'))


bt6=Button(root,text='6',bg='green',fg='white',width=4,height=2,command=lambda:get_digit('6'))
bt6.grid(row=2,column=0)
bt6.config(font=('verdana',14,'bold'))

bt5=Button(root,text='5',bg='green',fg='white',width=4,height=2,command=lambda:get_digit('5'))
bt5.grid(row=2,column=1)
bt5.config(font=('verdana',14,'bold'))

bt4=Button(root,text='4',bg='green',fg='white',width=4,height=2,command=lambda:get_digit('4'))
bt4.grid(row=2,column=2)
bt4.config(font=('verdana',14,'bold'))

bt_sub=Button(root,text='-',bg='green',fg='white',width=4,height=2,command=lambda:get_opr('-'))
bt_sub.grid(row=2,column=3)
bt_sub.config(font=('verdana',14,'bold'))

bt3=Button(root,text='3',bg='green',fg='white',width=4,height=2,command=lambda:get_digit('3'))
bt3.grid(row=3,column=0)
bt3.config(font=('verdana',14,'bold'))

bt2=Button(root,text='2',bg='green',fg='white',width=4,height=2,command=lambda:get_digit('2'))
bt2.grid(row=3,column=1)
bt2.config(font=('verdana',14,'bold'))

bt1=Button(root,text='1',bg='green',fg='white',width=4,height=2,command=lambda:get_digit('1'))
bt1.grid(row=3,column=2)
bt1.config(font=('verdana',14,'bold'))

bt_mul=Button(root,text='*',bg='green',fg='white',width=4,height=2,command=lambda:get_opr('*'))
bt_mul.grid(row=3,column=3)
bt_mul.config(font=('verdana',14,'bold'))

bt_clear=Button(root,text='C',bg='green',fg='white',width=4,height=2,command=get_clear)
bt_clear.grid(row=4,column=0)
bt_clear.config(font=('verdana',14,'bold'))

bt0=Button(root,text='0',bg='green',fg='white',width=4,height=2,command=lambda:get_digit('0'))
bt0.grid(row=4,column=1)
bt0.config(font=('verdana',14,'bold'))

bt_equal=Button(root,text='=',bg='green',fg='white',width=4,height=2,command=lambda:get_equal())
bt_equal.grid(row=4,column=2)
bt_equal.config(font=('verdana',14,'bold'))

bt_div=Button(root,text='/',bg='green',fg='white',width=4,height=2,command=lambda:get_opr('/'))
bt_div.grid(row=4,column=3)
bt_div.config(font=('verdana',14,'bold'))

root.mainloop() 