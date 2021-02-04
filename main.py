from HashDS import HashDS
from Truck import Truck
from TSP import TSP
from TimeStamp import *
from WGUTime import WGUTime

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

# creating a Truck 1 instance as well as a TSP 1 instance and adding packages to Truck 1 manually
truck_1 = Truck('Truck 1', 9, 5)
TSP_1 = TSP(truck_1)
truck_1.load_truck(allPackages, 1)
truck_1.load_truck(allPackages, 6)
truck_1.load_truck(allPackages, 12)
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
truck_1.load_truck(allPackages, 4)
truck_1.load_truck(allPackages, 17)
TSP_1.truckRoute(allDistances, allPackages, 0)

# creating a Truck 2 instance as well as a TSP 2 instance and adding packages to Truck 2 manually
truck_2 = Truck('Truck 2', 8, 0)
TSP_2 = TSP(truck_2)
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
truck_2.load_truck(allPackages, 11)
truck_2.load_truck(allPackages, 13)
TSP_2.truckRoute(allDistances, allPackages, 0)

# declare after truck 2 has returned so the time is set dynamically,
# creating a Truck 3 instance as well as a TSP 3 instance and adding packages to Truck 3 manually
truck_3 = Truck('Truck 3', truck_2.time.hours, truck_2.time.minutes)
truck_3.load_truck(allPackages, 2)
truck_3.load_truck(allPackages, 5)
truck_3.load_truck(allPackages, 7)
truck_3.load_truck(allPackages, 8)
truck_3.load_truck(allPackages, 9)
truck_3.load_truck(allPackages, 10)
truck_3.load_truck(allPackages, 33)
truck_3.load_truck(allPackages, 35)
truck_3.load_truck(allPackages, 39)
TSP_3 = TSP(truck_3)
TSP_3.truckRoute(allDistances, allPackages, 0)



print(truck_2.info(), truck_1.info(), truck_3.info())
total_miles = truck_2.miles + truck_1.miles + truck_3.miles
print(f'The combined mileage of all trucks sums up to {round(total_miles,2)}')
all_packages_status(allPackages, "09:00")
all_packages_status(allPackages, "10:30")
all_packages_status(allPackages, "12:03")
print("==========================================================================")
print("Hello welcome to command line interface for the WGUPS package manager")
print("==========================================================================")
loop = True
while loop:
    x = input("would you like to continue the app 'Y' to continue/'N' to end\n")
    if x.lower() == "n":
        print("GoodBye!")
        loop = False
    elif x.lower() == "y":
        while 1:
            try:
                input_time = input("Enter a time in format HH:MM\n")
                time_del = input_time.split(":")
                hour = int(time_del[0])
                minute = int(time_del[1])
                while len(time_del) > 2 or hour >= 24 or hour < 0 or minute >= 60 or minute < 0:
                    print("Hours are in military time from 0 - 23, please enter valid hour value")
                    print("Minute values range from 0 - 59, please enter a valid minute value")
                    input_time = input("Enter a time in format HH:MM\n")
                    time_del = input_time.split(":")
                    hour = int(time_del[0])
                    minute = int(time_del[1])
                break
            except ValueError:
                print("invalid entry")
            except IndexError:
                print("invalid entry")
        while 1:
            try:
                package_ID = int(input("please enter package ID:\n"))
                while package_ID <= 0 or package_ID > allPackages.size:
                    print("package ID's range from 1-40\n")
                    package_ID = int(input("please enter a package ID:\n"))
                break
            except ValueError:
                print("invalid entry")
        package_status(allPackages, input_time, package_ID)
    else:
        print("invalid entry\n")
