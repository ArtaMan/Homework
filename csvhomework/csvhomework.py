import csv

with open('parkings.csv', 'r', encoding='cp1251') as file:
    fields = ["ID", "ParkingName", "global_id", "ParkingZoneNumber", "AdmArea", "District", "Address", "WorkingHours",
              "Price", "CarCapacity", "Longitude_WGS84", "Latitude_WGS84", "Coordinates", "geoData"]
    reader = csv.DictReader(file, fields, delimiter=';')
    for row in reader:
        print(row)