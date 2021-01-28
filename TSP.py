# TSP attempt algorithm
class TSP:
    def __init__(self, Truck):
        self.current_location = 0
        self.Truck = Truck

    def truckRoute(self, distance_list, package_list, index_column):
        # index_column = 0 to start at hub
        # Test Function # truckRoute(truck_2, allDistances, allPackages, 0)
        return_Hub = 0  # initialize the return column, it is used to return to the hub
        while len(self.Truck.load) > 0:  # loop until all packages are delivered
            min_distance = 14.1  # initialize min-distance
            package_ID = 0  # initialize package ID
            for index_row in range(len(distance_list)):  # iterate through distance table
                for packages in self.Truck.load:  # iterate through truck load
                    if distance_list[index_row][1].__contains__(packages[1]):  # looking for address match
                        if distance_list[index_row][index_column + 2] != '':  # check if table value is not empty
                            current_distance = float(distance_list[index_row][index_column + 2])
                            if current_distance < min_distance:
                                min_distance = current_distance
                                package_ID = packages[0]
                                self.current_location = index_row
                        elif float(distance_list[index_column][index_row + 2]) < min_distance:
                            min_distance = float(distance_list[index_column][index_row + 2])
                            package_ID = packages[0]
                            self.current_location = index_row
            index_column = self.current_location
            self.Truck.mileage(min_distance)
            self.Truck.deliver(package_list, package_ID)
        self.Truck.mileage(float(distance_list[self.current_location][return_Hub + 2]))
        self.current_location = return_Hub
