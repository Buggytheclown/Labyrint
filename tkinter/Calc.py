from tkinter.messagebox import showinfo, showerror
from tkinter import *
from tkinter.colorchooser import *

root = Tk()
root.title('TiCalc')
displaed = StringVar()
displaed.set('0')
history = StringVar()
history.set('')
stuck0 = ''
stuck1 = ''
flag = 0
opperation = ''

but_height = IntVar()
but_width = IntVar()

config = {'height': 2, 'width': 4, 'bg': 'grey'}
config_num = {'height': 2, 'width': 4}
config_C = {'height': 2, 'width': 4, 'bg': 'red'}
config_res = {'height': 2, 'width': 4, 'bg': 'green'}
'''
lab_history = Frame()
lab2 = Text(lab_history, height=3)
lab2.pack(side=TOP, fill=X, expand=1)
lab_history.pack(side=TOP, fill=X)

separotor = Frame(height=20, bg="grey")
separotor.pack(side=TOP, fill=X)
'''
lab_display = Frame()
lab1 = Label(lab_display, textvariable=displaed, justify=LEFT, font=("Helvetica", 16))
lab1.pack(side=TOP, fill=X, expand=1)
lab_display.pack(side=TOP)

OtherFr = Frame()
OtherFr.pack(side=TOP)


def num_add(num):
    if not flag:
        global stuck0
        stuck0 += num
        displaed.set(stuck0)
    else:
        global stuck1
        stuck1 += num
        displaed.set(stuck1)


class mybut(Button):
    def __init__(self, num, master=OtherFr, **kargs):
        Button.__init__(self, master, **kargs)
        self.config(text=num, command=lambda: num_add(num))
        self.config(**config_num)


# 0123456789.
b1 = mybut('1')
b1.grid(row=2, column=0)
b2 = mybut('2')
b2.grid(row=2, column=1)
b3 = mybut('3')
b3.grid(row=2, column=2)
b4 = mybut('4')
b4.grid(row=3, column=0)
b5 = mybut('5')
b5.grid(row=3, column=1)
b6 = mybut('6')
b6.grid(row=3, column=2)
b7 = mybut('7')
b7.grid(row=4, column=0)
b8 = mybut('8')
b8.grid(row=4, column=1)
b9 = mybut('9')
b9.grid(row=4, column=2)
b0 = mybut('0')
b0.grid(row=5, column=0)


def add_dot():
    if not flag:
        global stuck0
        if '.' not in stuck0:
            stuck0 += '.'
            displaed.set(stuck0)
        else:
            showerror('warning', 'decimal my contain only 1 dot')
    else:
        global stuck1
        if '.' not in stuck0:
            stuck1 += '.'
            displaed.set(stuck1)
        else:
            showerror('warning', 'decimal my contain only 1 dot')


dot_but = Button(OtherFr, text='.', command=add_dot, **config_num)
dot_but.grid(row=5, column=1)


def clear():
    if not flag:
        global stuck0
        stuck0 = ''
        displaed.set('0')
    else:
        global stuck1
        stuck1 = ''
        displaed.set('0')


Cbut = Button(OtherFr, text='C', command=clear, **config_C)
Cbut.grid(row=1, column=1)


def clearall():
    global stuck0
    global stuck1
    global opperation
    global flag
    flag = 0
    opperation = ''
    stuck0 = ''
    stuck1 = ''
    displaed.set('0')


CEbut = Button(OtherFr, text='CE', command=clearall, **config_C)
CEbut.grid(row=1, column=2)


def back():
    if not flag:
        global stuck0
        stuck0 = stuck0[:-1]
        displaed.set(stuck0)
    else:
        global stuck1
        stuck1 = stuck1[:-1]
        displaed.set(stuck1)


Back_but = Button(OtherFr, text='<-', command=back, **config)
Back_but.grid(row=1, column=0)


def summ():
    if stuck0:
        global opperation
        opperation = '+'
        global flag
        flag = 1
    else:
        showerror('Warning', 'Input some args first')


Sum_but = Button(OtherFr, text='+', command=summ, **config)
Sum_but.grid(row=5, column=3)


def minus():
    if stuck0:
        global opperation
        opperation = '-'
        global flag
        flag = 1
    else:
        showerror('Warning', 'Input some args first')


Min_but = Button(OtherFr, text='-', command=minus, **config)
Min_but.grid(row=4, column=3)


def mult():
    if stuck0:
        global opperation
        opperation = '*'
        global flag
        flag = 1
    else:
        showerror('Warning', 'Input some args first')


Mult_but = Button(OtherFr, text='*', command=mult, **config)
Mult_but.grid(row=3, column=3)


def div():
    if stuck0:
        global opperation
        opperation = '/'
        global flag
        flag = 1
    else:
        showerror('Warning', 'Input some args first')


Div_but = Button(OtherFr, text='/', command=div, **config)
Div_but.grid(row=2, column=3)


def res():
    try:
        global stuck0
        global stuck1
        if stuck0 and stuck1 and opperation:
            locres = eval(stuck0 + opperation + stuck1)
            displaed.set(locres)
            stuck0 = ''
            stuck1 = ''
            global flag
            flag = 0
    except:
        showerror('Warning', 'missing argument')
        clearall()


Res_but = Button(OtherFr, text='=', command=res, **config_res)
Res_but.grid(row=5, column=2)


# bind method
def upres(event):
    k = event.char

    if k.isdigit():
        num_add(k)

    elif k == '+':
        summ()

    elif k == '-':
        minus()

    elif k == '*':
        mult()

    elif k == '/':
        div()

    elif k == '.' or k == ',':
        add_dot()


def resUP(event):
    res()


def clearallUP(event):
    clearall()


OtherFr.bind('<Key>', upres)
OtherFr.bind("<Escape>", clearallUP)
OtherFr.bind("<Return>", resUP)
#backspace didnt realise
OtherFr.focus_set()

# func from Menu
menubar = Menu(root)


def accept_func():
    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b0, dot_but,
               Cbut, CEbut, Back_but, Sum_but, Min_but, Mult_but, Div_but, Res_but]
    for i in buttons:
        i.config(height=but_height.get(), width=but_width.get())



def do_config():
    # resolutions - scHW
    TLconf = Toplevel()
    TLconf.title('configure')
    scHW = Frame(TLconf)
    scHW.grid(row=0, column=0)
    Label(scHW, text='Button resolutions').pack(side=TOP)

    global but_height
    scHeight = Scale(scHW, variable=but_height, label='But_Height', from_=1, to=20, orient=VERTICAL)
    scHeight.pack(side=LEFT)

    scWidth = Scale(scHW, variable=but_width, label='But_Width', from_=1, to=50, orient=HORIZONTAL)
    scWidth.pack(side=BOTTOM)
    scWidth.set(4)
    # choose color - colorschem
    colorschem = Frame(TLconf)
    colorschem.grid(row=0, column=1)
    Label(colorschem, text='Button Color').grid(row=0, column=0)
    # conf Color
    Label(colorschem, text='Number Color').grid(row=1, column=0)
    Button(colorschem, text='FG Color').grid(row=1, column=1)
    Button(colorschem, text='BG Color').grid(row=1, column=2)
    Label(colorschem, text='Res_But Color').grid(row=2, column=0)
    Button(colorschem, text='FG Color').grid(row=2, column=1)
    Button(colorschem, text='BG Color').grid(row=2, column=2)
    Label(colorschem, text='C and CE_But Color').grid(row=3, column=0)
    Button(colorschem, text='FG Color').grid(row=3, column=1)
    Button(colorschem, text='BG Color').grid(row=3, column=2)
    Label(colorschem, text='The other_But Color').grid(row=4, column=0)
    Button(colorschem, text='FG Color').grid(row=4, column=1)
    Button(colorschem, text='BG Color').grid(row=4, column=2)
    # accept, cancel - okcan
    okcan = Frame(TLconf)
    okcan.grid(row=1, column=1)
    Button(okcan, text='Accept', command=accept_func).pack(side=LEFT)
    Button(okcan, text='Cancel', command=TLconf.destroy).pack(side=LEFT)


'''
config = {'height': 2, 'width': 4, 'bg': 'grey'}
config_num = {'height': 2, 'width': 4}
config_C = {'height': 2, 'width': 4, 'bg': 'red'}
config_res = {'height': 2, 'width': 4, 'bg': 'green'}
'''


def hello():
    showinfo(title='Info', message='In progress')


def about():
    showinfo(title='About', message='Pycalc was created by Tidjei. Enjoy it!')


# File Menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="-Open-", command=hello)
filemenu.add_command(label="-Save-", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Edit Menu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="-Cut-", command=hello)
editmenu.add_command(label="-Copy-", command=hello)
editmenu.add_command(label="-Paste-", command=hello)
editmenu.add_separator()
editmenu.add_command(label="Config", command=do_config)
menubar.add_cascade(label="Edit", menu=editmenu)

# Help Menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)
mainloop()
