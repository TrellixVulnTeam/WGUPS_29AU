# Jose Alvarez Pulido
# Student ID: 001206503
from HashDS import HashDS
from Truck import Truck
from TSP import TSP
from TimeStamp import *

import csv
# declaration of the User defined data structure, 40 is the size of the package list.
allPackages = HashDS(40)
# declaration of the distance 2D table
allDistances = []
with open('WGUPSPackageFile.csv') as packageFile:
    packages = csv.reader(packageFile, delimiter=",")
    # using the python csv reader
    for row in packages:
        # inserting the packages into the allPackages hash table
        allPackages.insert(int(row[0]), row[1], row[5], row[2], int(row[4]), row[6])

with open('WGUPSDistanceTable.csv') as distanceFile:
    distance = csv.reader(distanceFile, delimiter=",")
    # using the python csv reader
    for row in distance:
        # adding the distance table per row to the allDistances Table
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

# Command Line interface
# printing the truck info at the start of command line interface
# truck.info is a method of the Truck object, which displays the time of departure from Hub as well as the mileage traveled per truck and the time the truck returns to the Hub
print(truck_2.info(), truck_1.info(), truck_3.info())
# printing a screenshot of all the packages at the time 9:00 AM G1 requirement
all_packages_status(allPackages, "09:00")
# printing a screenshot of all the packages at the time of 10:30 AM G2 requirement
all_packages_status(allPackages, "10:30")
# printing a screenshot of all the packages at the time of 12:03 PM G3 requirement
all_packages_status(allPackages, "12:03")
# print a screenshot of the total mileage traveled by all trucks for the day, contains time check making sure all packages where delivered before the deadline
total_mileage(truck_1, truck_2, truck_3, allPackages)
# prints the start of the User interface
print("=========================================================================================================")
print("Hello welcome to command line interface for the WGUPS package manager")
print("=========================================================================================================")
# User interface loop
loop = True
while loop:
    # gets user input Y to continue N to exit the app
    x = input("would you like to continue the app 'Y' to continue/'N' to end\n")
    # ends the loop and thus ending the program
    if x.lower() == "n":
        print("GoodBye!")
        loop = False
    # continues the loop, and asks for user to enter a valid time in HH:MM military time
    elif x.lower() == "y":
        # while loop for exception handling
        while 1:
            # a try/except block for catching invalid inputs
            try:
                # input the user for a valid time
                input_time = input("Enter a time in format HH:MM\n")
                # create a list of items slit by a colon ":"
                # defines the hour by the first item in the list
                # defines the minute by the second item in the list
                time_del = input_time.split(":")
                # makes sure the hour and minute are integers, else exception valueError is triggered
                hour = int(time_del[0])
                minute = int(time_del[1])
                # another while loop for exception handling, makes sure a valid time is entered and it limits the time to hours and minutes
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
        # Another exception handling loop
        while 1:
            # try/except block used to make sure valid user inputs
            try:
                # makes sure the input is an integer
                package_ID = int(input("please enter package ID:\n"))
                # makes sure the package ID is valid
                while package_ID <= 0 or package_ID > allPackages.size:
                    print("package ID's range from 1-40\n")
                    # if the ID is valid it is stored
                    package_ID = int(input("please enter a package ID:\n"))
                break
            except ValueError:
                print("invalid entry")
        # The function package_status() is used to retrieve the status of the package and print out the values
        # The function is found in the file TimeStamp.py
        package_status(allPackages, input_time, package_ID)
    # handles user typos and restarts the loop
    else:
        print("invalid entry\n")
