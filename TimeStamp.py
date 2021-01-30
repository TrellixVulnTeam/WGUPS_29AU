def get_time_value(time_string):
    times = time_string.split(':')
    hours = int(times[0])
    minutes = int(times[1])
    time_value = (hours * 60) + minutes
    return time_value


# package[6] is load time, package[8] is delivery time, selected time is user selected time
def package_status(HashDS, selected_time, package_ID):
    package = HashDS.look_up(package_ID)
    if get_time_value(package[6]) > get_time_value(selected_time):
        print(f'ID:{package[0]}, Truck:unassigned, Status:At Hub, Delivered:TBD')
    elif get_time_value(package[8]) > get_time_value(selected_time) >= get_time_value(package[6]):
        print(f'ID:{package[0]}, Truck:{package[7]}, Status:En Route, Delivered:TBD')
    elif get_time_value(selected_time) >= get_time_value(package[8]):
        print(f'ID:{package[0]}, Truck:{package[7]}, Status:Delivered, Delivered:{package[8]}')


# package[6] is load time, package[8] is delivery time, selected time is user selected time
def all_packages_status(HashDS, selected_time):
    print("##########################################################")
    print(f'Current Time of Screenshot - {selected_time}')
    for i in range(1, len(HashDS.table) + 1):
        package = HashDS.look_up(i)
        if get_time_value(package[6]) > get_time_value(selected_time):
            print(f'ID:{package[0]}, Truck:unassigned, Status:At Hub, Delivered:TBD, Deadline:{package[2]}')
        elif get_time_value(package[8]) > get_time_value(selected_time) >= get_time_value(package[6]):
            print(f'ID:{package[0]}, Truck:{package[7]}, Status:En Route, Delivered:TBD, Deadline:{package[2]}')
        elif get_time_value(selected_time) >= get_time_value(package[8]):
            print(f'ID:{package[0]}, Truck:{package[7]}, Status:Delivered, Delivered:{package[8]}, Deadline:{package[2]} ')
