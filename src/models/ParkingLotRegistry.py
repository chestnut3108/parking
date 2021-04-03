from .ParkingLot import ParkingLot


class ParkingLotRegistry:
    parkingLot = None

    def getParkingLot(self, lot_capacity):
        if self.parkingLot is None:
            self.parkingLot = ParkingLot(lot_capacity)
            print("Created parking of {} slots".format(lot_capacity))
            return self.parkingLot
        else:
            return self.parkingLot


