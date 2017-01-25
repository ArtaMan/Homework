from tkinter import *
from math import *


def _press(event):
    try:
        a1 = int(a.get('1.0', END))
    except:
        print('Введите в строку A только цифры')
        return

    try:
        b1 = int(b.get('1.0', END))
    except:
        print('Введите в строку B только цифры')
        return

    try:
        c1 = int(c.get('1.0', END))
    except:
        print('Введите в строку C только цифры')
        return

    D1 = b1 ** 2 - 4 * a1 * c1
    if D1 < 0:
        x1['text'] = 'Корней нет'
        x2['text'] = 'Корней нет'
        D['text'] = D1
    elif D1 == 0:
        x1['text'] = -b1 / (2 * a1)
        x2['text'] = -b1 / (2 * a1)
        D['text'] = D1
    else:
        x1['text'] = (-b1 + sqrt(D1)) / (2 * a1)
        x2['text'] = (-b1 - sqrt(D1)) / (2 * a1)
        D['text'] = D1


root = Tk()
a = Text(root, height=1, width=5)
b = Text(root, height=1, width=5)
c = Text(root, height=1, width=5)
a.insert('1.0', '1')
b.insert('1.0', '1')
c.insert('1.0', '1')
xyz = Label(root, text='ax2 + bx + c = 0')
la = Label(root, text='A        = ', width=10, height=1)
lb = Label(root, text='B        = ', width=10, height=1)
lc = Label(root, text='C        = ', width=10, height=1)
press = Button(root, text='Решить', width=10, height=1)
lx1 = Label(root, text='x1       = ', width=10, height=1)
lx2 = Label(root, text='x1       = ', width=10, height=1)
lD = Label(root, text='x1        = ', width=10, height=1)
x1 = Label(root, height=1, width=10)
x2 = Label(root, height=1, width=10)
D = Label(root, height=1, width=5)

xyz.grid(row=0, column=0)
la.grid(row=1, column=0)
lb.grid(row=2, column=0)
lc.grid(row=3, column=0)
a.grid(row=1, column=1)
b.grid(row=2, column=1)
c.grid(row=3, column=1)
press.grid(row=4, column=0)
lx1.grid(row=5, column=0)
x1.grid(row=5, column=1)
lx2.grid(row=6, column=0)
x2.grid(row=6, column=1)
lD.grid(row=7, column=0)
D.grid(row=7, column=1)
press.bind('<Button-1>', _press)
root.mainloop()