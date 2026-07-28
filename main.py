#!/bin/python3

#Imports
import subprocess
import sys
from src.file_search import File, Directory

#Welcome message and warning.
print("================================================================================================")
print("Hi! Welcome to the Data Exporter made by Calvin Johns!\nAny reprouctions of this program will be taken down imediatly by Tony Stark himself!\nAnd the developer will be killed by Tony Starks killer drones!!!\nThank you!\nAt any point in the program you can enter 0 to close it.")
print("================================================================================================")
while 1:
    export_file = File()
    export_file.the_type(input("Would you like to spesify a file type? Yes, No:\n"))
    export_file.command()
    export_location = Directory()
    export_location.command()
    command = ["sudo", "cp", f"{export_file.object_path}", f"{export_location.object_path}"]
    subprocess.run(command)
    print("Your file has been exported successfully.")
    while 1:
        loop: str = input("Do you wish to export another file? Type Yes to continue or No to exit.\n")
        if loop.lower() == "no":
            sys.exit()
        elif loop.lower() == "yes":
            break
        else:
            print("Input unrecognized. Please try again.")
            continue
    continue
