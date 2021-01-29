def get_time_value(time_string):
    times = time_string.split(':')
    hours = int(times[0])
    minutes = int(times[1])
    time_value = (hours * 60) + minutes
    return time_value


# package[6] is load time, package[8] is delivery time, selected time is user selected time
def time_comparison(all_packages, selected_time):
    for package in all_packages:
        if get_time_value(package[6]) > get_time_value(selected_time):
            print(f'ID:{package[0]}, Truck:{package[7]}, Status: At Hub, Time of Delivery: TBD')
