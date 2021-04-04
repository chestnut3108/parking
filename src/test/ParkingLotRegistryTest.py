import unittest
from src.lib.models.ParkingLotRegistry import ParkingLotRegistry
from src.lib.models.Vehicle import Vehicle


class ParkingLotRegistryTest(unittest.TestCase):
    capacity = 4

    def testGetParkingLot(self):
        registry = ParkingLotRegistry()
        self.assertIsNone(registry.parkingLot)
        parkinglot1 = registry.getParkingLot(4)
        self.assertEqual(4, parkinglot1.capacity)

        # Checking singleton behaviour
        parkinglot2 = registry.getParkingLot(6)
        self.assertEqual(4, parkinglot2.capacity)

if __name__ == '__main__':
    unittest.main()