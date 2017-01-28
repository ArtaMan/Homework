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
    text = ''
    if D1 < 0:
        text += 'D = b² - 4ac\n'
        text += 'D = ' + str(D1) + '\n'
        text += 'Дискриминанта меньше нуля\n'
        text += 'У этого уравнения корней нет\n'
    elif D1 == 0:
        text += 'D = b² - 4ac\n'
        text += 'D = ' + str(D1) + '\n'
        text += 'Дискриминанта равна нулю\n'
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
        text += 'Дискриминанта больше нуля\n'
        text += '     -b ± √D\n'
        text += 'x = ---------\n'
        text += '       2a  \n'
        text += 'x1 = ' + str((-b1 + sqrt(D1)) / (2 * a1)) + '\n'
        text += 'x2 = ' + str((-b1 - sqrt(D1)) / (2 * a1)) + '\n'
    solve['text'] = text


root = Tk()
root.title('Reshatel2000')
description = Label(root, text='Решатель2000 решает квадратные уравнения вида ax² + bx + c = 0\n '
                               'Введите ниже коэфиценты a, b и c', width=52, height=2)
a = Text(root, height=1, width=5)
b = Text(root, height=1, width=5)
c = Text(root, height=1, width=5)
a.insert('1.0', '1')
b.insert('1.0', '1')
c.insert('1.0', '1')
# xyz = Label(root, text='ax² + bx + c = 0')
la = Label(root, text='A   = ', width=4, height=1)
lb = Label(root, text='B   = ', width=4, height=1)
lc = Label(root, text='C   = ', width=4, height=1)
press = Button(root, text='Решить', width=10, height=1)
solve = Label(root, text='', width=30, height=10)

description.grid(row=0, column=0)
la.grid(row=2, column=0)
lb.grid(row=3, column=0)
lc.grid(row=4, column=0)
a.place(x=260, y=36)
b.place(x=260, y=58)
c.place(x=260, y=81)
press.grid(row=5, column=0)
solve.grid(row=6, column=0)
press.bind('<Button-1>', _press)
root.mainloop()