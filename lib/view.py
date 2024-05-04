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
    print("="*66)
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

    print("="*66)

    name = input("Weapon Name\t: ")
    rarity = input("Weapon Rarity\t: ")
    price = input("Weapon Price\t: ")

    command.create(name, rarity, price)
    print("="*66)
    input("\nPress Enter to Continue")

def delete_console():
    utils.clean_console()

    data = command.read()

    index = "No"
    name = "Weapon Name"
    rarity = "Rarity"
    price = "Price"

    # creating Table heade view
    print("="*66)
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

    while True:
        print("Select The Data Index to Delete")
        try:
            index = int(input("Data Index: "))
            data = command.read(index=index)

            if data:
                data_break = data.split(",")
                name = data_break[2]
                rarity = data_break[3]
                price = data_break[4][:-1]

                # show data
                print("="*66)
                print("The data you want to delete")
                print(f"1. Name\t\t: {name}")
                print(f"2. Rarity\t: {rarity}")
                print(f"3. Price\t: {price}")

                is_delete = input("Are you sure want to delete it (y/n)?: ").lower()

                if is_delete == "y":
                    command.delete(index)
                    print("Success Deleting Data")
                    input("Press Enter to Continue")
                    break
                else:
                    break
            else:
                print("Index Is Empty")
                input("Press Enter to Continue")
                continue
        except:
            print("!!Not a Valid Index, Try Again!!")
            input("Press Enter to Continue")
