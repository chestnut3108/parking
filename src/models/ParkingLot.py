from .Vehicle import Vehicle


class ParkingLot:
    def __init__(self, lot_capacity):
        self.capacity = lot_capacity
        self.unused_slots = [x for x in range(1, lot_capacity + 1)]
        self.used_slot_count = 0
        self.slot_vehicle_dict = {}         # {slot: vehicle} dictionary

    def __getEmptySlot(self):
        if self.used_slot_count == self.capacity:
            return -1
        else:
            nearest_unused_slot = self.unused_slots[0]
            self.unused_slots = self.unused_slots[1:]
            self.used_slot_count += 1
            return nearest_unused_slot

    def park(self, registration_number: str, driver_age: str) -> int:
        slot = self.__getEmptySlot()
        if slot == -1:
            print("No empty slot please wait")
        else:
            self.slot_vehicle_dict[str(slot)] = Vehicle(registration_number, driver_age)
            print(
                "Car with vehicle registration number {} has been parked at slot number {}".format(registration_number,
                                                                                                   slot))
        return int(slot)

    def leave(self, slot_number):
        vehicle_left = self.slot_vehicle_dict.pop(slot_number, -1)
        if vehicle_left == -1:
            print("Slot already empty")
        else:
            self.unused_slots.append(int(slot_number))
            self.unused_slots.sort()
            self.used_slot_count -= 1
            print(
                "Slot number {} vacated, the car with vehicle registration number {} left the space, the driver of the car was of age {}"
                .format(slot_number, vehicle_left.registration_number, vehicle_left.driver_age))

    def get_slot_number_by_registration_number(self, registration_number):
        '''
            Parameter :int registration_number \n
            Returns slot: str else -1 if slot not found
        '''
        for slot, vehicle in self.slot_vehicle_dict.items():
            if vehicle.registration_number == registration_number:
                return slot
        return -1

    def get_vehicle_registration_numbers_by_driver_age(self, driver_age):
        '''
            Parameter :int -> driver_age  \n
            Returns :str[] -> list of slots
        '''
        result = []
        for slot in self.slot_vehicle_dict:
            vehicle = self.slot_vehicle_dict.get(slot)
            if vehicle.driver_age == driver_age:
                result.append(vehicle.registration_number)
        return result

    def get_slot_numbers_for_driver_of_age(self, driver_age):
        '''
            Parameter :int -> driver_age   \n
            Returns :str[] -> list of slots
        '''
        result = []
        for slot in self.slot_vehicle_dict:
            vehicle = self.slot_vehicle_dict.get(slot)
            if vehicle.driver_age == driver_age:
                result.append(slot)
        return result