# Time Class

class WGUTime:
    def __init__(self, hours, minutes):
        while hours > 24 or hours < 0:
            self.hours = input("Hours are in military time from 0 - 24, please enter valid hour value")
        self.hours = hours
        while minutes > 59 or minutes < 0:
            self.minutes = input("Minute values ranger from 0 - 59, please enter a valid minute value")
        self.minutes = minutes

    def addMinutes(self, minute):
        hour = int(minute / 60)
        minute = int(minute % 60)
        self.minutes += minute
        self.hours += hour
        if self.minutes >= 60:
            self.minutes = int(self.minutes % 60)
            self.hours += 1
        if self.hours >= 24:
            self.hours = int(self.hours % 24)

    def getTimeStamp(self):
        if self.hours < 10 and self.minutes < 10:
            time_string = f'0{self.hours}:0{self.minutes}'
        elif self.hours < 10:
            time_string = f'0{self.hours}:{self.minutes}'
        elif self.minutes < 10:
            time_string = f'{self.hours}:0{self.minutes}'
        else:
            time_string = f'{self.hours}:{self.minutes}'
        return time_string
