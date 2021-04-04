import argparse
from os import path
from models.ParkingLotRegistry import ParkingLotRegistry
from models.ParkingLotRegistry import ParkingLot

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--filepath", required=True, help="filepath")
cli_args = vars(ap.parse_args())

parkingLot: ParkingLot = None


def createParkingLot(lot_capacity: int):
    global parkingLot
    parking_lot_registry = ParkingLotRegistry()
    if lot_capacity > 0:
        parkingLot = parking_lot_registry.getParkingLot(lot_capacity)
    else:
        print("Invalid capacity :(")


def execute_command(command: str, parkingLot: ParkingLot):
    command = command.strip("\n")
    command = command.split(' ')

    if command[0] == 'Create_parking_lot':
        createParkingLot(int(command[1]))

    else:
        if parkingLot is None:
            print("Create a parking lot ;)")

        elif command[0] == 'Leave':
            parkingLot.leave(command[1])

        elif command[0] == 'Park':
            parkingLot.park(command[1], command[3])

        elif command[0] == 'Slot_number_for_car_with_number':
            print(parkingLot.get_slot_number_by_registration_number(command[1]))

        elif command[0] == 'Slot_numbers_for_driver_of_age':
            result = parkingLot.get_vehicle_registration_numbers_by_driver_age(command[1])
            if len(result) > 0:
                print(', '.join(map(str, result)))
            else:
                print("No slot is booked by any user with age {}".format(command[1]))

        elif command[0] == 'Vehicle_registration_number_for_driver_of_age':
            result = parkingLot.get_vehicle_registration_numbers_by_driver_age(command[1])
            if len(result) > 0:
                print(', '.join(map(str, result)))
            else:
                print("No slot is booked by any user with age {}".format(command[1]))

        else:
            print("Please enter a valid command")


if __name__ == '__main__':

    if path.isfile(cli_args['filepath']):
        file = open(cli_args['filepath'], "r")
        lines = file.readlines()
        for command in lines:
            execute_command(command, parkingLot)
    else:
        print("please enter valid path")
