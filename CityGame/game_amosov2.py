# -*- coding: utf-8 -*-
import sys
from random import *
inpu = open('citiesAmosov.txt', 'r', encoding='utf8')

a = inpu.readlines()
for i in range(len(a)):
    cur = ''
    for j in a[i]:
        if j.isalpha():
            cur += j
    cur = cur.lower()
    a[i] = cur


def game(iniortown):
    


    # iniortown.split()
    if iniortown == -1:
        return choice(a)
    town = ''
    for i in iniortown:
        i = str(i)
        if i.isalpha():
            town += i


    town = town.lower()
    #town += ' '
    # town += '\n'

    if town not in a:
        # print('Я такого города не знаю, либо он уже был')
        return -1

    lastb = False
    x = 1
    town2 = []
    for i in range(len(town) - 1):
        town2.append(town[i])

    while lastb == False:
        if town2[len(town2) - x] == 'ъ' or town2[len(town2) - x] == 'ь' or town2[len(town2) - x] == 'ы':
            town2[len(town2) - x] = ' '
        else:
            lastb = True
        x += 1
    town = ''

    for i in town2:
        i = str(i)
        if i.isalpha():
            town += i

    '''    iniortown = input()
        iniortown.split()
        town = ''
        for i in iniortown:
            i = str(i)
            if i.isalpha():
                town += i
        for i in a:
            i = str(i)
            cor = i.lower()
            if cor == town:
                ok = True
    '''



    for i in range(len(a)):

        a[i] = str(a[i])

        cor = a[i].lower()

        if cor[0] == town[len(town)-1]:
            myTown = a[i]
            a.remove(a[i])
            ret = ''
            for j in range(len(myTown)-1):
                ret += myTown[j] 

            return (ret)
    print('Я сдаюсь')
    sys.exit()  

if __name__ == '__main__':
    while True:
        print(city(input()))
