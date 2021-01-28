from HashDS import HashDS
from Truck import Truck
from TSP import TSP

import csv

allPackages = HashDS(40)
allDistances = []
with open('WGUPSPackageFile.csv') as packageFile:
    packages = csv.reader(packageFile, delimiter=",")
    for row in packages:
        allPackages.insert(int(row[0]), row[1], row[5], row[2], int(row[4]), row[6])

with open('WGUPSDistanceTable.csv') as distanceFile:
    distance = csv.reader(distanceFile, delimiter=",")
    for row in distance:
        allDistances.append(row)

# creating truck 1, and truck 2 objects to load packages
truck_1 = Truck('Truck 1', 9, 5)
TSP_1 = TSP(truck_1)
truck_1.load_truck(allPackages, 6)
truck_1.load_truck(allPackages, 12)
truck_1.load_truck(allPackages, 13)
truck_1.load_truck(allPackages, 22)
truck_1.load_truck(allPackages, 23)
truck_1.load_truck(allPackages, 24)
truck_1.load_truck(allPackages, 25)
truck_1.load_truck(allPackages, 26)
truck_1.load_truck(allPackages, 28)
truck_1.load_truck(allPackages, 27)
truck_1.load_truck(allPackages, 31)
truck_1.load_truck(allPackages, 32)
truck_1.load_truck(allPackages, 40)
truck_1.load_truck(allPackages, 34)
TSP_1.truckRoute(allDistances, allPackages, 0)

# Manually loading packages onto Truck object
truck_2 = Truck('Truck 2', 8, 0)
TSP_2 = TSP(truck_2)
truck_2.load_truck(allPackages, 1)
truck_2.load_truck(allPackages, 3)
truck_2.load_truck(allPackages, 14)
truck_2.load_truck(allPackages, 15)
truck_2.load_truck(allPackages, 16)
truck_2.load_truck(allPackages, 18)
truck_2.load_truck(allPackages, 19)
truck_2.load_truck(allPackages, 20)
truck_2.load_truck(allPackages, 21)
truck_2.load_truck(allPackages, 29)
truck_2.load_truck(allPackages, 30)
truck_2.load_truck(allPackages, 37)
truck_2.load_truck(allPackages, 38)
truck_2.load_truck(allPackages, 36)
TSP_2.truckRoute(allDistances, allPackages, 0)

# declare after truck 2 has returned so the time is set dynamically
truck_3 = Truck('Truck 3', truck_2.time.hours, truck_2.time.minutes)
truck_3.load_truck(allPackages, 2)
truck_3.load_truck(allPackages, 4)
truck_3.load_truck(allPackages, 5)
truck_3.load_truck(allPackages, 7)
truck_3.load_truck(allPackages, 8)
truck_3.load_truck(allPackages, 9)
truck_3.load_truck(allPackages, 10)
truck_3.load_truck(allPackages, 11)
truck_3.load_truck(allPackages, 17)
truck_3.load_truck(allPackages, 33)
truck_3.load_truck(allPackages, 35)
truck_3.load_truck(allPackages, 39)
TSP_3 = TSP(truck_3)
TSP_3.truckRoute(allDistances, allPackages, 0)

print(truck_2.info(), truck_1.info(), truck_3.info())
print(truck_2.miles+truck_1.miles+truck_3.miles)
