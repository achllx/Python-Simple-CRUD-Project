from . import command
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
    while True:
        utils.clean_console()

        data = command.read()

        index = "No"
        name = "Weapon Name"
        rarity = "Rarity"
        price = "Price"

        # creating Table header view
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
            input("Press Enter to Back")
            break
  
        print("="*66)
        
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

def update_console():
    while True:
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
            input("Press Enter to Back")
            break
  
        print("="*66)
        
        print("Select The Data Index to Update")

        try:
            index = int(input("Data Index: "))
            data = command.read(index=index)

            if data:
                data_break = data.split(",")
                id = data_break[0]
                name = data_break[2]
                rarity = data_break[3]
                price = data_break[4][:-1]

                # show data
                while True:
                    print("="*66)
                    print("Which one you want to update?")
                    print(f"1. Name\t\t: {name}")
                    print(f"2. Rarity\t: {rarity}")
                    print(f"3. Price\t: {price}")

                    try:
                        user_option = int(input("Enter the Option number:"))
                        
                        match user_option:
                            case 1: name = input("New Weapon Name: ")
                            case 2: rarity = input("New Weapon Rarity: ")
                            case 3: price = input("New Weapon Price: ")
                            case _:
                                print("!!Option is only between number 1 and 3!!\n")
                                input("Press Enter to Continue")
                                continue
                    except:
                        print("!!Option must a number!!\n")
                        input("Press Enter to Continue")
                        continue

                    user_option = input("Another else (y/n)? ")

                    if user_option == 'y':
                        continue
                    else:
                        break

                print("="*66)
                print(f"1. Name\t\t: {name}")
                print(f"2. Rarity\t: {rarity}")
                print(f"3. Price\t: {price}")

                is_correct = input("Check if This data update is what you want (y/n)? ").lower()

                if is_correct == "y":
                    command.update(index, id, name, rarity, price)
                else:
                    break
            else:
                print("Index Is Empty")
                input("Press Enter to Continue")
                continue
        except:
            print("!!Not a Valid Index, Try Again!!")
            input("Press Enter to Continue")

        break