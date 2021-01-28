# Hash Data Structure
class HashDS:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def _get_hash(self, ID):
        return ID % self.size

    def insert(self, ID, address, deadline, city, zipCode, weight):
        key_hash = self._get_hash(ID)
        # status of package whereabouts
        status = "at the hub"
        # truck number assigned to the package
        truck = 'unassigned'
        # Time of Delivery
        ToD = "not yet delivered"
        key_value = [ID, address, deadline, city, zipCode, weight, status, truck, ToD]
        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for items in self.table[key_hash]:
                if items[0] == ID:
                    for i in range(1, len(key_value)):
                        items[i] = key_value[i]
                    return True
            self.table[key_hash].append(key_value)
            return True

    def look_up(self, ID):
        key_hash = self._get_hash(ID)
        if self.table[key_hash] is not None:
            for items in self.table[key_hash]:
                if items[0] == ID:
                    return items
        return None

    # deleting packages is not used in this project
    # def delete(self, ID):
    #     key_hash = self._get_hash(ID)
    #     if self.table[key_hash] is None:
    #         return False
    #     for i in range(0, len(self.table[key_hash])):
    #         if self.table[key_hash][i][0] == ID:
    #             self.table[key_hash].pop(i)
    #             return True

    def load(self, ID, value, truck):
        key_hash = self._get_hash(ID)
        status = "en route"
        key_value = value
        key_value[6] = status
        key_value[7] = truck
        for items in self.table[key_hash]:
            if items[0] == ID:
                for i in range(1, len(key_value)):
                    items[i] = key_value[i]
                return True

    def deliver(self, ID, value, ToD):
        key_hash = self._get_hash(ID)
        status = "Delivered"
        key_value = value
        key_value[6] = status
        key_value[8] = ToD
        for items in self.table[key_hash]:
            if items[0] == ID:
                for i in range(1, len(key_value)):
                    items[i] = key_value[i]
                return True
