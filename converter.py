import urllib.request
from xml.dom import minidom
from tkinter import *


def send1(i):
    # print(i)
    text = 'За ' + str(valuty[i][3]) + ' рублей ' + str(valuty[i][2]) + ' ' + str(valuty[i][1])
    ans['text'] = text


def _send1(i):
    def send1_(event):
        send1(i)
    return send1_


# Ежедневные курсы валют ЦБ РФ
url = "http://www.cbr.ru/scripts/XML_daily.asp"

# Чтение URL
webFile = urllib.request.urlopen(url)
data = webFile.read()

# Имя файла
UrlSplit = url.split("/")[-1]
ExtSplit = UrlSplit.split(".")[1]
FileName = UrlSplit.replace(ExtSplit, "xml")

with open(FileName, "wb") as localFile:
    localFile.write(data)

webFile.close()

# Парсинг xml и запись данных в файл
doc = minidom.parse(FileName)

# Извлечение данных по валютам
currency = doc.getElementsByTagName("Valute")

valuty = []
for rate in currency:
    sid = rate.getAttribute("ID")
    charcode = rate.getElementsByTagName("CharCode")[0]
    name = rate.getElementsByTagName("Name")[0]
    value = rate.getElementsByTagName("Value")[0]
    nominal = rate.getElementsByTagName("Nominal")[0]
    valuty.append((charcode.firstChild.data, name.firstChild.data, value.firstChild.data, nominal.firstChild.data))

# valuty = [(0, 'lol', 12, 23), (0, 'juj', 45, 34)]

root = Tk()
rbuttons1 = []
i = 0
ans = Label(root, text='press button', width=50, height=1)
ans.grid(row=0, column=2)
for i in range(len(valuty)):
    lol = Button(root, text=valuty[i][1], height=1, width=50)
    lol.bind("<Button-1>", _send1(i))
    lol.grid(row=i, column=0)
    rbuttons1.append(lol)
root.mainloop()