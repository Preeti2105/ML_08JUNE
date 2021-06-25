import tkinter as t

expr = ""

app = t.Tk()
app.title('Python Calculator')
app.geometry('350x350')

result = t.Variable(app)
t.Entry(app, textvariable=result, width=15).place(x=20,y=40)

def total():
    global expr
    result.set(eval(expr))
    expr=" "

def clearScreen():
    global expr
    expr=" "
    result.set(expr)

def values(num):
    global expr
    expr = expr+num
    result.set(expr)
    
t.Button(app, text='Clear', width = 10, height=1, command=lambda: clearScreen(),bg='red').place(x=30,y=5)

t.Button(app, text='1', width = 6, height=4, command=lambda: values('1')).place(x=30,y=70)
t.Button(app, text='2', width = 6, height=4, command=lambda: values('2')).place(x=80,y=70)
t.Button(app, text='3', width = 6, height=4, command=lambda: values('3')).place(x=130,y=70)
t.Button(app, text='+', width = 6, height=4, command=lambda: values('+')).place(x=180,y=70)

t.Button(app, text='4', width = 6, height=4, command=lambda: values('4')).place(x=30,y=140)
t.Button(app, text='5', width = 6, height=4, command=lambda: values('5')).place(x=80,y=140)
t.Button(app, text='6', width = 6, height=4, command=lambda: values('6')).place(x=130,y=140)
t.Button(app, text='-', width = 6, height=4, command=lambda: values('-')).place(x=180,y=140)

t.Button(app, text='7', width = 6, height=4, command=lambda: values('7')).place(x=30,y=210)
t.Button(app, text='8', width = 6, height=4, command=lambda: values('8')).place(x=80,y=210)
t.Button(app, text='9', width = 6, height=4, command=lambda: values('9')).place(x=130,y=210)
t.Button(app, text='*', width = 6, height=4, command=lambda: values('*')).place(x=180,y=210)

t.Button(app, text='.', width = 6, height=4, command=lambda: values('.')).place(x=30,y=280)
t.Button(app, text='0', width = 6, height=4, command=lambda: values('0')).place(x=80,y=280)
t.Button(app, text='=', width = 6, height=4, command=lambda: total()).place(x=130,y=280)
t.Button(app, text='/', width = 6, height=4, command=lambda: values('/')).place(x=180,y=280)

app.mainloop()
