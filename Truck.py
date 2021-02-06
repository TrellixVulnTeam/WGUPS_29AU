# Truck Object
from WGUTime import WGUTime


class Truck:
    # Truck objects are declared with a truck number, the hour and minute as integers for the delivery start time
    # The truck object also stores values for the current time, start time, a list of the load, the mileage traveled, the maximum size of the load, and the speed of the truck
    def __init__(self, truckNumber, hour, minute):
        self.truckNumber = truckNumber
        self.start_time = WGUTime(hour, minute)
        self.time = WGUTime(hour, minute)
        self.load = []
        self.miles = 0
        self.size = 16
        self.speed = 18

    # This method is used for loading packages into the truck, appending the package to the load list, as well as interfacing with
    # the HashDS for updating the values of the package being loaded.
    def load_truck(self, HashDS, ID):
        package = HashDS.look_up(ID)
        if len(self.load) < self.size:
            HashDS.load(ID, package, self.truckNumber, self.time.getTimeStamp())
            package = HashDS.look_up(ID)
            self.load.append(package)
        else:
            print(f'{self.truckNumber} is at capacity, package ID {str(package[0])} Was not loaded')

    # This method is used for delivering packages into the truck, removing the package from the load list, as well as interfacing with
    # the HashDS for updating the values of the package being delivered.
    def deliver(self, HashDS, ID):
        package = HashDS.look_up(ID)
        HashDS.deliver(ID, package, self.time.getTimeStamp())
        package = HashDS.look_up(ID)
        self.load.remove(package)

    # This method is used to keep track of the mileage as well as the time, using the trucks internal variables time, miles, and speed.
    def mileage(self, miles):
        # result of miles/speed is in hours to get minutes must multiply minutes by 60
        minutes = round((miles / self.speed) * 60, 2)
        self.time.addMinutes(minutes)
        self.miles += miles
        self.miles = round(self.miles, 2)

    # This method is used to display the info of the truck route
    # The info for the truck route includes the truck number, the start time, the mileage traveled, and the time the truck returns to the hub
    def info(self):
        return f"{self.truckNumber} left the Hub at {self.start_time.getTimeStamp()} and has traveled {self.miles} miles " \
               f"on its route.\n {self.truckNumber} completed its route and returned to Hub at {self.time.getTimeStamp()}\n"
