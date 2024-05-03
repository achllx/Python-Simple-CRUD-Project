from . import command
from . import database
from . import utils

def read_console():
    utils.clean_console()

    data = command.read()

    index = "No"
    name = "Weapon Name"
    rarity = "Rarity"
    price = "Price"

    # creating Table heade view
    print("\n"+"="*66)
    print(f"{index:4} | {name:30} | {rarity:10} | {price:13}")
    print("="*66)
    
    if data:
       for index, data in enumerate(data):
            data_break = data.split(",")
            name = data_break[2]
            rarity = data_break[3]
            price = data_break[4]
            
            print(f"{index+1:<4} | {name:30} | {rarity:10} | {price:>13}")
    else:
         print(" "*28+"Empty Table")
    
    print("="*66)
    input("\nPress Enter to Continue")

def create_console():
    utils.clean_console()
