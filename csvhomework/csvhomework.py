import csv

with open('parkings.csv', 'r', encoding='cp1251') as file:
    fields = ["ID", "ParkingName", "global_id", "ParkingZoneNumber", "AdmArea", "District", "Address", "WorkingHours",
              "Price", "CarCapacity", "Longitude_WGS84", "Latitude_WGS84", "Coordinates", "geoData"]
    reader = csv.DictReader(file, fields, delimiter=';')
    sum1mashine = 0
    sumfull = 0
    i = 0
    for row in reader:
        if i == 0:
            i += 1
            continue
        sum1mashine += float(row.get('Price')) * float(row.get('CarCapacity'))
        sumfull += float(row.get('Price')) * float(row.get('CarCapacity'))
print(sum1mashine, sumfull)