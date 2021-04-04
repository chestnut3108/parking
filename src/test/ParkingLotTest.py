import unittest
from src.lib.models.ParkingLot import ParkingLot
from src.lib.models.Vehicle import Vehicle
class ParkingLotTest(unittest.TestCase):
    capacity = 4
    VEHICLE_REGISTRATION_NUMBER_1 = 'XX-1234-0001'
    VEHICLE_REGISTRATION_NUMBER_2 = 'XX-1234-0002'
    VEHICLE_REGISTRATION_NUMBER_3 = 'XX-1234-0003'
    VEHICLE_REGISTRATION_NUMBER_4 = 'XX-1234-0004'
    VEHICLE_REGISTRATION_NUMBER_5 = 'XX-1234-0005'

    def setUp(self):
        self.parking_lot = ParkingLot(self.capacity)

    def fullParkingSetUp(self, parking_lot):
        vehicle1 = Vehicle(self.VEHICLE_REGISTRATION_NUMBER_1, 18)
        vehicle2 = Vehicle(self.VEHICLE_REGISTRATION_NUMBER_2, 20)
        vehicle3 = Vehicle(self.VEHICLE_REGISTRATION_NUMBER_3, 18)
        vehicle4 = Vehicle(self.VEHICLE_REGISTRATION_NUMBER_4, 21)
        parking_lot.park(vehicle1.registration_number, vehicle1.driver_age)
        parking_lot.park(vehicle2.registration_number, vehicle2.driver_age)
        parking_lot.park(vehicle3.registration_number, vehicle3.driver_age)
        parking_lot.park(vehicle4.registration_number, vehicle4.driver_age)
        return parking_lot

    def testFullParkOverFlow(self):
        parking_lot = self.fullParkingSetUp(self.parking_lot)
        self.assertEqual(self.capacity, parking_lot.used_slot_count)
        vehicle5 = Vehicle(self.VEHICLE_REGISTRATION_NUMBER_5, 21)
        newVehicleSlot = parking_lot.park(vehicle5.registration_number, vehicle5.driver_age)
        self.assertEqual(-1, newVehicleSlot )
        self.assertEqual(self.capacity, parking_lot.used_slot_count)

    def testParking(self):
        vehicle1 = Vehicle(self.VEHICLE_REGISTRATION_NUMBER_1, 18)
        vehicle2 = Vehicle(self.VEHICLE_REGISTRATION_NUMBER_2, 20)
        vehicle3 = Vehicle(self.VEHICLE_REGISTRATION_NUMBER_3, 18)
        self.parking_lot.park(vehicle1.registration_number, vehicle1.driver_age)
        self.parking_lot.park(vehicle2.registration_number, vehicle2.driver_age)
        self.parking_lot.park(vehicle3.registration_number, vehicle3.driver_age)

        self.assertEqual(self.parking_lot.used_slot_count, 3)
        self.assertEqual(len(self.parking_lot.unused_slots), 1)

        vehicle4 = Vehicle(self.VEHICLE_REGISTRATION_NUMBER_4, 21)
        self.parking_lot.park(vehicle4.registration_number, vehicle4.driver_age)

        self.assertEqual(self.parking_lot.used_slot_count, 4)
        self.assertEqual(len(self.parking_lot.unused_slots), 0)

    def testLeaveParkingLot(self):
        vehicle1 = Vehicle(self.VEHICLE_REGISTRATION_NUMBER_1, 18)
        vehicle2 = Vehicle(self.VEHICLE_REGISTRATION_NUMBER_2, 20)
        self.parking_lot.park(vehicle1.registration_number, vehicle1.driver_age)
        self.parking_lot.park(vehicle2.registration_number, vehicle2.driver_age)

        self.assertEqual(self.parking_lot.used_slot_count, 2)
        self.assertEqual(len(self.parking_lot.unused_slots), 2)
        self.assertTrue('1' in self.parking_lot.slot_vehicle_dict)
        self.assertTrue('2' in self.parking_lot.slot_vehicle_dict)
        self.assertFalse('3' in self.parking_lot.slot_vehicle_dict)

        self.parking_lot.leave('2')
        self.assertFalse('2' in self.parking_lot.slot_vehicle_dict)
        self.assertEqual(self.parking_lot.used_slot_count, 1)
        self.assertEqual(len(self.parking_lot.unused_slots), 3)

        # Leave wrong slot
        self.parking_lot.leave('10')
        self.assertEqual(self.parking_lot.used_slot_count, 1)
        self.assertEqual(len(self.parking_lot.unused_slots), 3)

        # Leave already empty slot
        self.parking_lot.leave('3')
        self.assertEqual(self.parking_lot.used_slot_count, 1)
        self.assertEqual(len(self.parking_lot.unused_slots), 3)

    def testGetVehicleRegistrationNumbersByDriverAge(self):
        parking_lot = self.fullParkingSetUp(self.parking_lot)
        vehicle_r_nos = parking_lot.get_vehicle_registration_numbers_by_driver_age(18)
        self.assertTrue(self.VEHICLE_REGISTRATION_NUMBER_1 in vehicle_r_nos)
        self.assertTrue(self.VEHICLE_REGISTRATION_NUMBER_3 in vehicle_r_nos)
        self.assertEqual(2, len(vehicle_r_nos))

        #Testing wrong age
        vehicle_r_nos = parking_lot.get_vehicle_registration_numbers_by_driver_age(1000)
        self.assertEqual(0, len(vehicle_r_nos))

    def testGetSlotNumbersForDriverOfAge(self):
        parking_lot = self.fullParkingSetUp(self.parking_lot)
        slots = parking_lot.get_slot_numbers_for_driver_of_age(18)
        self.assertEqual(2, len(slots))

        #Testing wrong age
        slots = parking_lot.get_slot_numbers_for_driver_of_age(1000)
        self.assertEqual(0, len(slots))

    def testSlotNumberByRegistrationNumber(self):
        parking_lot = self.fullParkingSetUp(self.parking_lot)
        slot1 = parking_lot.get_slot_number_by_registration_number(self.VEHICLE_REGISTRATION_NUMBER_1)
        slot2 = parking_lot.get_slot_number_by_registration_number(self.VEHICLE_REGISTRATION_NUMBER_2)
        slot3 = parking_lot.get_slot_number_by_registration_number(self.VEHICLE_REGISTRATION_NUMBER_3)
        slot4 = parking_lot.get_slot_number_by_registration_number(self.VEHICLE_REGISTRATION_NUMBER_4)

        self.assertEqual(slot1, '1')
        self.assertEqual(slot2, '2')
        self.assertEqual(slot3, '3')
        self.assertEqual(slot4, '4')

        # Test invalid Registration number vehicle
        slot5 = parking_lot.get_slot_number_by_registration_number(self.VEHICLE_REGISTRATION_NUMBER_5)
        self.assertEqual(slot5, -1)



if __name__ == '__main__':
    unittest.main()