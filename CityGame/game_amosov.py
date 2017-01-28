from random import *


def game(city):
    if city == -1:
        return choice(a)
    city = city.lower()
    # if lastcity != -1:
    #     lastcity = lastcity.lower()
    if city not in a:
        print('There`s no city named', city, 'or I don`t have it in my cities...')
        return -1
    if city not in used[ord(city[0].lower()) - 1072]:
        used[ord(city[0].lower()) - 1072].append(city)
    else:
        print('This city already was')
        return -1
    # if lastcity != -1:
    #     if lastcity[-1].lower() != city[0].lower():
    #         print('Choice city that starts on letter "', lastcity[-1], '"', sep='')
    #         return lastcity
    last = city[-1].lower()
    if last in ['ь', 'ъ', 'ы']:
        print('Theres no city on the last letter')
        return -1
    temp = ord(last) - 1072
    if len(used[ord(city[-1].lower()) - 1072]) == len(words[ord(city[-1].lower()) - 1072]):
        print('sdayus')
        exit()
    lol = choice(words[temp])
    while lol in used:
        lol = choice(words[temp])
    used[ord(lol[0].lower()) - 1072].append(lol)
    lol = lol[0].upper() + lol[1:len(lol) - 1]
    for i in range(len(lol)):
        if lol[i] == '-' or lol[i] == ' ':
            lol = lol[0:i + 1] + lol[i + 1].upper() + lol[i + 2:]
    return lol

fin = open('citiesAmosov.txt', 'r', encoding='utf-8')
a = fin.readlines()
for i in range(len(a)):
    a[i] = a[i][:len(a[i]) - 1]
    a[i] = a[i].lower()
words = [[] for i in range(32)]
for i in range(len(a)):
    temp = ord(a[i][0])
    temp1 = temp - 1072
    words[temp1].append(a[i])
used = [[] for i in range(32)]
