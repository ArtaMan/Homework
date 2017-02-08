from tkinter import *
from math import *
import webbrowser as wb
import sys


def _pressOffline(event):
    try:
        a1 = int(a.get())
    except:
        solve['text'] = 'Введите в строку A только цифры'
        return

    try:
        b1 = int(b.get())
    except:
        solve['text'] = 'Введите в строку B только цифры'
        return

    try:
        c1 = int(c.get())
    except:
        solve['text'] = 'Введите в строку C только цифры'
        return

    if a1 == 0:
        solve['text'] = 'Введите в строку A не ноль'
        return
    text = ''
    v = var.get()
    if v == 0:
        D1 = b1 ** 2 - 4 * a1 * c1
        if D1 < 0:
            text += 'D = b² - 4ac\n'
            text += 'D = ' + str(D1) + '\n'
            text += 'Дискриминант меньше нуля\n'
            text += 'У этого уравнения корней нет\n'
        elif D1 == 0:
            text += 'D = b² - 4ac\n'
            text += 'D = ' + str(D1) + '\n'
            text += 'Дискриминант равен нулю\n'
            text += '     -b\n'
            text += 'x = ----\n'
            text += '     2a  \n'
            if (-b1 + sqrt(D1)) / (2 * a1) == 0:
                text += 'x = 0\n'
            else:
                text += 'x = ' + str((-b1 + sqrt(D1)) / (2 * a1)) + '\n'
        else:
            text += 'D = b² - 4ac\n'
            text += 'D = ' + str(D1) + '\n'
            text += 'Дискриминант больше нуля\n'
            text += '     -b ± √D\n'
            text += 'x = ---------\n'
            text += '       2a  \n'
            text += 'x1 = ' + str((-b1 + sqrt(D1)) / (2 * a1)) + '\n'
            text += 'x2 = ' + str((-b1 - sqrt(D1)) / (2 * a1)) + '\n'
    else:
        D2 = b1 ** 2 - 4 * a1 * c1
        p = c1 / a1
        q = b1 / a1
        text += 'x1 * x2 = c / a = ' + str(p) + '\n'
        text += 'x1 + x2 = -(b / a) = ' + str(-q) + '\n\n'
        if D2 < 0:
            text += 'У этого уравнения нет корней\n'
        elif D2 == 0:
            if (-b1 + sqrt(D2)) / (2 * a1) == 0:
                text += 'x = 0\n'
            else:
                text += 'x = ' + str((-b1 + sqrt(D2)) / (2 * a1)) + '\n'
        else:
            text += 'x1 = ' + str((-b1 + sqrt(D2)) / (2 * a1)) + '\n'
            text += 'x2 = ' + str((-b1 - sqrt(D2)) / (2 * a1)) + '\n'
    solve['text'] = text

def _pressOnline(event):
    try:
        a1 = int(a.get())
    except:
        solve['text'] = 'Введите в строку A только цифры'
        return

    try:
        b1 = int(b.get())
    except:
        solve['text'] = 'Введите в строку B только цифры'
        return

    try:
        c1 = int(c.get())
    except:
        solve['text'] = 'Введите в строку C только цифры'
        return

    if a1 == 0:
        solve['text'] = 'Введите в строку A не ноль'
        return

    url = 'http://www.nigma.ru/?s=' + str(a1) + 'x2'
    if b1 >= 0:
        url += '~%7C-' + str(b1) + 'x'
    else:
        url += str(b1) + 'x'
    if c1 >= 0:
        url += '~%7C-' + str(c1) + '=0'
    else:
        url += str(c1) + '=0'
    wb.open(url)


root = Tk()
if sys.platform == 'win32':
    root.title('Reshatel2000')
    root['bg'] = 'white'
    root.geometry('400x400+0+0')
    description = Label(root, bg='white', text='Решатель2000 решает квадратные уравнения вида ax² + bx + c = 0\n '
                                               'Введите ниже коэфиценты a, b и c', width=52, height=2)
    a = Entry(root, width=20, bg='white')
    b = Entry(root, width=20, bg='white')
    c = Entry(root, width=20, bg='white')
    # xyz = Label(root, text='ax² + bx + c = 0')
    la = Label(root, bg='white', text='A   = ', width=4, height=1)
    lb = Label(root, bg='white', text='B   = ', width=4, height=1)
    lc = Label(root, bg='white', text='C   = ', width=4, height=1)
    var = IntVar()
    DorV = Label(root, bg='white', text='Как решить уравнение?')
    Disk = Radiobutton(root, bg='white', text='Через дискриминант', variable=var, value=0)
    Viet = Radiobutton(root, bg='white', text='Через теорему Виета', variable=var, value=1)
    pressOffline = Button(root, bg='white', text='Решить локально', width=15, height=1, bd=1)
    pressOnline = Button(root, bg='white', text='Решить онлайн', width=15, height=1, bd=1)
    solve = Label(root, bg='white', text='', width=50, height=10)
    kostil = Label(root, bg='white', text='', width=0, height=0)
    kostil2 = Label(root, bg='white', text='', width=0, height=0)
    kostil3 = Label(root, bg='white', text='', width=0, height=0)
    kostil4 = Label(root, text='', width=0, height=0)

    description.grid(row=0, column=0)
    la.grid(row=2, column=0)
    lb.grid(row=3, column=0)
    lc.grid(row=4, column=0)
    a.place(x=205, y=36)
    b.place(x=205, y=58)
    c.place(x=205, y=81)
    kostil4.grid(row=5, column=0)
    DorV.grid(row=6, column=0)
    Disk.place(x=20, y=145)
    Viet.place(x=235, y=145)
    kostil.grid(row=8, column=0)
    kostil2.grid(row=9, column=0)
    kostil3.grid(row=10, column=0)
    pressOffline.place(x=15, y=165)
    pressOnline.place(x=265, y=165)
    solve.grid(row=11, column=0)
else:
    root.title('Reshatel2000')
    description = Label(root, text='Решатель2000 решает квадратные уравнения вида ax² + bx + c = 0\n '
                                   'Введите ниже коэфиценты a, b и c', width=52, height=2)
    a = Entry(root, width=20, text='1')
    b = Entry(root, width=20)
    c = Entry(root, width=20)
    # xyz = Label(root, text='ax² + bx + c = 0')
    la = Label(root, text='A   = ', width=4, height=1)
    lb = Label(root, text='B   = ', width=4, height=1)
    lc = Label(root, text='C   = ', width=4, height=1)
    var = IntVar()
    DorV = Label(root, text='Как решить уравнение?')
    Disk = Radiobutton(root, text='Через дискриминант', variable=var, value=0)
    Viet = Radiobutton(root, text='Через теорему Виета', variable=var, value=1)
    pressOffline = Button(root, text='Решить локально', width=15, height=1)
    pressOnline = Button(root, text='Решить онлайн', width=15, height=1)
    solve = Label(root, text='', width=50, height=10)
    kostil = Label(root, text='', width=0, height=0)
    kostil2 = Label(root, text='', width=0, height=0)
    kostil3 = Label(root, text='', width=0, height=0)

    description.grid(row=0, column=0)
    la.grid(row=2, column=0)
    lb.grid(row=3, column=0)
    lc.grid(row=4, column=0)
    a.place(x=260, y=36)
    b.place(x=260, y=58)
    c.place(x=260, y=81)
    kostil3.grid(row=5, column=0)
    DorV.grid(row=6, column=0)
    Disk.place(x=45, y=145)
    Viet.place(x=260, y=145)
    kostil.grid(row=7, column=0)
    kostil2.grid(row=8, column=0)
    pressOffline.place(x=30, y=165)
    pressOnline.place(x=280, y=165)
    solve.grid(row=9, column=0)
pressOffline.bind('<Button-1>', _pressOffline)
pressOnline.bind('<Button-1>', _pressOnline)
root.mainloop()