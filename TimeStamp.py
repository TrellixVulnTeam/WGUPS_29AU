# This function is used to convert a time string in military time in the format of HH:MM to a time value that can be used to compare times.
def get_time_value(time_string):
    times = time_string.split(':')
    hours = int(times[0])
    minutes = int(times[1])
    time_value = (hours * 60) + minutes
    return time_value


# This function is used to determine the package status of an individual package.
# it takes in the HashDS, the user selected time for the status, and the package ID
# package[6] is load time, package[8] is delivery time, selected time is user selected time
def package_status(HashDS, selected_time, package_ID):
    # the contents of the package are retrieved and stored to list variable using the HashDS look_up method
    package = HashDS.look_up(package_ID)
    # The function then compares the time values of the selected time, load time, and delivery time.
    # if the load time value is greater than the selected time value then the packages are still at the hub
    if get_time_value(package[6]) > get_time_value(selected_time):
        print(
            f'ID:{package[0]}, Address: {package[1]}, Deadline:{package[2]}, City:{package[3]}, ZipCode:{package[4]}, weight:{package[5]}, Truck:unassigned, Status:At Hub, Delivered:TBD')
    # if the selected time value is in between the load time and delivery time then the package is at the truck
    elif get_time_value(package[8]) > get_time_value(selected_time) >= get_time_value(package[6]):
        print(
            f'ID:{package[0]}, Address: {package[1]}, Deadline:{package[2]}, City:{package[3]}, ZipCode:{package[4]}, weight:{package[5]}, Truck:{package[7]}, Status:En Route, Delivered:TBD')
    # if the selected time value is greater or equal the delivery time value, then the package has been delivered.
    elif get_time_value(selected_time) >= get_time_value(package[8]):
        print(
            f'ID:{package[0]}, Address: {package[1]}, Deadline:{package[2]}, City:{package[3]}, ZipCode:{package[4]}, weight:{package[5]}, Truck:{package[7]}, Status:Delivered, Delivered:{package[8]}')


# This function is used to determine the package status of all the packages at a given time.
# it takes in the HashDS, the user selected time for the statuses
# package[6] is load time, package[8] is delivery time, selected time is user selected time
def all_packages_status(HashDS, selected_time):
    print(
        "################################################################################################################################################")
    print(f'Current Time of Screenshot - {selected_time}')
    # this function iterates through all the IDs in the HashDS printing the status for each package at a given time
    for i in range(1, len(HashDS.table) + 1):
        package = HashDS.look_up(i)
        # The function then compares the time values of the selected time, load time, and delivery time.
        # if the load time value is greater than the selected time value then the packages are still at the hub
        if get_time_value(package[6]) > get_time_value(selected_time):
            print(
                f'ID:{package[0]}, Address: {package[1]}, Deadline:{package[2]}, City:{package[3]}, ZipCode:{package[4]}, weight:{package[5]}, Truck:unassigned, Status:At Hub, Delivered:TBD')
        # if the selected time value is in between the load time and delivery time then the packages are still at the truck
        elif get_time_value(package[8]) > get_time_value(selected_time) >= get_time_value(package[6]):
            print(
                f'ID:{package[0]}, Address: {package[1]}, Deadline:{package[2]}, City:{package[3]}, ZipCode:{package[4]}, weight:{package[5]}, Truck:{package[7]}, Status:En Route, Delivered:TBD')
        # if the selected time value is greater or equal the delivery time value, then the packages have been delivered.
        elif get_time_value(selected_time) >= get_time_value(package[8]):
            print(
                f'ID:{package[0]}, Address: {package[1]}, Deadline:{package[2]}, City:{package[3]}, ZipCode:{package[4]}, weight:{package[5]}, Truck:{package[7]}, Status:Delivered, Delivered:{package[8]}')


# This function is used to determine the total mileage traveled across all trucks
# This function makes sure all packages are delivered before the deadline
def total_mileage(Truck1, Truck2, Truck3, HashDS):
    total_miles = Truck1.miles + Truck2.miles + Truck3.miles
    # These variables are used for handling the packages that were delivered after the deadline
    error = False
    error_list = []
    # The function iterates through all the packages in the hash table
    for packages in HashDS.table:
        # if the index where the deadline is stored EOD the calculation can be skipped
        if packages[0][2] != "EOD":
            # for this project the hash table has no collisions, comparing time values for the index where the deadline is stored
            # and the time value for where the index that stores the delivery time
            deadline = get_time_value(packages[0][2].split(' ')[0])
            delivery = get_time_value(packages[0][8])
            if deadline < delivery:
                error = True
                error_list.append(packages[0])
    # If any logical errors arise they are printed
    if error:
        for errors in error_list:
            print(f'Package ID:{errors} was not delivered in time')
    # if no errors are found the function prints out the total mileage for all trucks
    else:
        print(
            "=========================================================================================================")
        print(
            f'All packages were delivered on time. The combined mileage of all trucks is {round(total_miles, 2)} miles')
