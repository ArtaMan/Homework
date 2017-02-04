import csv

with open('dolzhniki.csv', 'r', encoding='cp1251') as file:
    fields = ["ID", "Name", "INN", "global_id", "KPP", "OGRN", "Sum", "ExtraInfo"]
    reader = csv.DictReader(file, fields, delimiter=';')
    sum = 0
    i = 0
    j = 1
    lst = []
    for row in reader:
        if i == 0:
            i += 1
            continue
        lst.append((row.get('Name'), float(row.get('Sum'))))
        sum += float(row.get('Sum'))
        j += 1
    sred = sum / j
    print('1) Средняя задолжность - %s'%sred)
    lst.sort(key=lambda x: x[1])
    for i in range(len(lst)):
        if lst[i][1] < sred:
            if lst[i][1] - sred < sred - lst[i - 1][1]:
                sr = lst[i][0]
                sr1 = lst[i][1]
            else:
                sr = lst[i - 1][0]
                sr1 = lst[i - 1][1]

with open('parkings.csv', 'r', encoding='cp1251') as file:
    fields = ["ID", "ParkingName", "global_id", "ParkingZoneNumber", "AdmArea", "District", "Address", "WorkingHours",
              "Price", "CarCapacity", "Longitude_WGS84", "Latitude_WGS84", "Coordinates", "geoData"]
    reader = csv.DictReader(file, fields, delimiter=';')
    sumfull = 0
    i = 0
    for row in reader:
        if i == 0:
            i += 1
            continue
        sumfull += float(row.get('Price')) * int(row.get('CarCapacity'))
    print('2) Если все парковки заполненены, то Москва получает %s рублей в час'%int(sumfull))

print('3) Должник с средней задолжностью: %s, %s рублей'%(sr, sr1))