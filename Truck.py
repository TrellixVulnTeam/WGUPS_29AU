# Truck Object
from WGUTime import WGUTime


class Truck:
    def __init__(self, truckNumber, hour, minute):
        self.truckNumber = truckNumber
        self.start_time = WGUTime(hour, minute)
        self.time = WGUTime(hour, minute)
        self.load = []
        self.miles = 0
        self.size = 16
        self.speed = 18

    def load_truck(self, HashDS, ID):
        package = HashDS.look_up(ID)
        if len(self.load) < self.size:
            HashDS.load(ID, package, self.truckNumber, self.time.getTimeStamp())
            package = HashDS.look_up(ID)
            self.load.append(package)
        else:
            print(f'{self.truckNumber} is at capacity, package ID {str(package[0])} Was not loaded')

    def deliver(self, HashDS, ID):
        package = HashDS.look_up(ID)
        HashDS.deliver(ID, package, self.time.getTimeStamp())
        package = HashDS.look_up(ID)
        self.load.remove(package)

    def mileage(self, miles):
        # result of miles/speed is in hours to get minutes must multiply minutes by 60
        minutes = round((miles / self.speed) * 60, 2)
        self.time.addMinutes(minutes)
        self.miles += miles
        self.miles = round(self.miles, 2)

    def info(self):
        return f"{self.truckNumber} left the Hub at {self.start_time.getTimeStamp()} and has traveled {self.miles} miles " \
               f"on its route.\n {self.truckNumber} completed its route and returned to Hub at {self.time.getTimeStamp()}\n"
