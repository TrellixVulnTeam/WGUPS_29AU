# class TSP

class TSP:
    # When declaring a TSP, a Truck object is taken as a parameter
    def __init__(self, Truck):
        self.current_location = 0
        self.Truck = Truck

    # This method is the algorithm used to delivering all the packages that are loaded on the truck.
    def truckRoute(self, distance_list, package_list, index_column):
        # index_column = 0 to start at hub
        # Test method call # TSP1.truckRoute(allDistances, allPackages, 0)
        return_Hub = 0  # initialize the return column, it is used to return to the hub
        while len(self.Truck.load) > 0:  # loop until all packages are delivered
            min_distance = 14.1  # initialize min-distance
            package_ID = 0  # initialize package ID
            for index_row in range(len(distance_list)):  # iterate through distance table
                for packages in self.Truck.load:  # iterate through truck load
                    if distance_list[index_row][1].__contains__(packages[1]):  # looking for address match
                        if distance_list[index_row][index_column + 2] != '':  # check if table value is not empty
                            current_distance = float(distance_list[index_row][index_column + 2])  # current distance is used to compare to the minimum distance
                            if current_distance < min_distance:
                                min_distance = current_distance # if the current distance is less than the minimum replace the existing minimum value with the current distance
                                package_ID = packages[0]  # This is to keep track of the package ID for delivering the package
                                self.current_location = index_row  # the classes current location is changed to the index row, this is to keep track of the current location outside the method scope.
                        elif float(distance_list[index_column][index_row + 2]) < min_distance:  # if the value in the index row, column is a empty string flip the row, column values
                            min_distance = float(distance_list[index_column][index_row + 2])  # if the value is less than the minimum distance set the new minimum distance as that value
                            package_ID = packages[0]  # keep track of the package ID
                            self.current_location = index_row  # set the class variable current_location to the index_row, the index row is good for keeping track of location in the way a package ID keeps track of a package
            index_column = self.current_location  # set the index_column to the current location so that the algorithm looks at the correct index for the mileage value
            self.Truck.mileage(min_distance)  # This adds the mileage to the Truck object, keeping track of miles traveled
            self.Truck.deliver(package_list, package_ID)  # This delivers the package updating its key values, and removing it from the load.
        self.Truck.mileage(float(distance_list[self.current_location][return_Hub + 2]))  # After all packages have been delivered the mileage for returning to the hub is missing, this line makes sure to keep track of that mileage.
        self.current_location = return_Hub  # set the current_location to 0, which is the index_row for the HUB, keeping track of the location at every step of the algorithm.
