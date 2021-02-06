# Hash Data Structure

class HashDS:
    # at declaration the size of the HashDS is required
    def __init__(self, size):
        # The size is stored for hashing
        self.size = size
        # An internal list is created with the length of the size inputted, all values are set to None as default
        self.table = [None] * self.size

    # This method returns the hash value of the ID used as parameter
    def _get_hash(self, ID):
        return ID % self.size

    # The insert method takes in values to be inserted as parameters, uses its key hash to insert the items in the table
    def insert(self, ID, address, deadline, city, zipCode, weight):
        # the key hash uses the ID entered as well as the classes _get_hash() method.
        key_hash = self._get_hash(ID)
        # the time package is loaded on truck
        load_time = ""
        # Time of Delivery
        time_of_delivery = ""
        # truck number assigned to the package
        truck = 'unassigned'
        # The key value is the list that will be inserted in table, it is kept as a list to encapsulate the data.
        key_value = [ID, address, deadline, city, zipCode, weight, load_time, truck, time_of_delivery]
        # if the location at index key_hash is None the a list with the first value of key_value is added
        # it is a list of list, this is in case of a hash value collision known as chaining
        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        # In the event that a value is already present
        else:
            for items in self.table[key_hash]:
                # If the ID's match the new key_values will replace the existing values
                if items[0] == ID:
                    for i in range(1, len(key_value)):
                        items[i] = key_value[i]
                    return True
            # If the ID's do not match the new key values will be chained at that location
            self.table[key_hash].append(key_value)
            return True

    # This function looks up an item in the table using the ID
    def look_up(self, ID):
        # a key hash is used to locate item in O(1) time.
        key_hash = self._get_hash(ID)
        # if a value exists in that location use the for loop to cycle through chained key values
        if self.table[key_hash] is not None:
            for items in self.table[key_hash]:
                # if the ID of a chained key value matches return all the key values
                if items[0] == ID:
                    return items
        return None

    # This method is used for loading packages into the truck. The parameters are the ID of the package, the contents of the key value,
    # the truck number string, and the load time of the package.
    def load(self, ID, value, truck, load_time):
        key_hash = self._get_hash(ID)
        # using the contents of the existing key value, change the key values of the list at index 6,7
        # The key values of the list at index 6 corresponds to the time the package was loaded on the truck
        # The key values of the list at index 7 corresponds to the truck number the package was loaded on
        key_value = value
        key_value[6] = load_time
        key_value[7] = truck
        for items in self.table[key_hash]:
            # if a value exists in that location use the for loop to cycle through chained key values
            if items[0] == ID:
                # replace the existing values with the updated key values
                # since the package is loaded the values need to be updated
                for i in range(1, len(key_value)):
                    items[i] = key_value[i]
                return True

    # This method is used for delivering packages to the address. The parameters are the ID of the package, the contents of the key value,
    # The time of delivery
    def deliver(self, ID, value, time_of_delivery):
        key_hash = self._get_hash(ID)
        # using the contents of the existing key value, change the key values of the list at index 8
        # The key values of the list at index 8 corresponds to the time the package was delivered
        key_value = value
        # if a value exists in that location use the for loop to cycle through chained key values
        key_value[8] = time_of_delivery
        for items in self.table[key_hash]:
            # replace the existing values with the updated key values
            # since the package is delivered the values need to be updated
            if items[0] == ID:
                for i in range(1, len(key_value)):
                    items[i] = key_value[i]
                return True

