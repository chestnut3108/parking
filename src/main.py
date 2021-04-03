import sys
import argparse
from os import path
from models.ParkingLotRegistry import ParkingLotRegistry


ap = argparse.ArgumentParser()

ap.add_argument("-f", "--filepath", required=True, help="filepath")

cli_args = vars(ap.parse_args())

parkingLot = None

def createParkingLot(lot_capacity):
    global parkingLot
    parkingLotRegistry =  ParkingLotRegistry()
    parkingLot = parkingLotRegistry.getParkingLot(int(lot_capacity))



def execute_command(command):
    global parkingLot
    command = command.strip("\n")
    command = command.split(' ')
    print("command Started", command)
    if command[0] == 'Create_parking_lot':
        createParkingLot(command[1])

    elif command[0] == 'Leave' and parkingLot is not None:

        parkingLot.leave(command[1])

    elif command[0] == 'Park'and parkingLot is not None:

        parkingLot.park(command[1], command[3])
    elif command[0] == 'Slot_number_for_car_with_number'and parkingLot is not None:
        
        print(parkingLot.slotNumberByRegistrationNumber(command[1]))
    elif command[0] == 'Slot_numbers_for_driver_of_age'and parkingLot is not None:

        print(parkingLot.getSlotNumbersForDriverOfAge(command[1]))

    elif command[0] == 'Vehicle_registration_number_for_driver_of_age' and parkingLot is not None:

        result = parkingLot.getVehicleRegistrationNumbersByDriverAge(command[1])
        if len(result)>0:
            print(', '.join(map(str, result)))
        else:
            print("No slot is booked by any user with age {}".format( command[1]))

    print("-----------------------------------------------------------")



if __name__ == '__main__':

    if path.isfile(cli_args['filepath']):
        file = open(cli_args['filepath'], "r")
        lines = file.readlines()
        for command in lines:
            execute_command(command)
    else:
        print("please enter valid path")
