from . import database
from .utils import generate_id
import time
import os

def read(**kwargs):
    try:
        with open(database.database_name, 'r') as file:
            data = file.readlines()
            total = len(data)

            if "index" in kwargs:
                data_index = kwargs["index"]-1

                if data_index < 0 or data_index > total:
                    return False
                else:
                    return data[data_index]
            else:
                return data
    except FileNotFoundError:
        print(f"File '{database.database_name}' not found.")
        return False
    except PermissionError:
        print(f"No permission to read '{database.database_name}'.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def create(name, rarity, price):
    data = database.template.copy()

    data["id"] = generate_id()
    data["timestamp"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["name"] = name
    data["rarity"] = rarity
    data["price"] = price

    data_str = f'{data["id"]},{data["timestamp"]},{data["name"]},{data["rarity"]},{data["price"]}'

    try:
        with open(database.database_name, 'a', encoding="utf-8") as file:
            file.write(data_str)
            file.write('\n')
    except PermissionError:
        print(f"No permission to write to '{database.database_name}'.")
    except FileNotFoundError:
        print(f"File '{database.database_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    input("Press Enter To Continue")
    
def delete(index):
    database.init_temp()

    try:
        with open(database.database_name, 'r') as file:
            counter = 0
            while True:
                data = file.readline()
                if len(data) == 0:
                    break
                elif counter != index-1:
                    with open("data_temp.txt", 'a', encoding="utf-8") as temp_file:
                        temp_file.write(data)

                counter += 1
    except FileNotFoundError:
        print(f"File '{database.database_name}' not found.")
        input("Press Enter To Continue")
    except PermissionError:
        print(f"No permission to access '{database.database_name}'.")
        input("Press Enter To Continue")
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter To Continue")
    
    os.remove(database.database_name)
    os.rename("data_temp.txt", database.database_name)

def update(index, id, name, rarity, price):
    data = database.template.copy()

    data["id"] = id
    data["timestamp"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["name"] = name
    data["rarity"] = rarity
    data["price"] = price

    data_str = f'{data["id"]},{data["timestamp"]},{data["name"]},{data["rarity"]},{data["price"]}\n'

    data_length = len(data_str)

    try:
        with open(database.database_name, 'r+', encoding="utf-8") as file:
            lines = file.readlines()
            if index <= len(lines):
                lines[index - 1] = data_str.ljust(data_length)  # Overwrites rows with new data
                file.seek(0)  # Move the file pointer to the beginning
                file.writelines(lines)  # Rewrite all lines
                file.truncate()  # Trim remaining content (if any)
                print("Data updated successfully!")
            else:
                print("Index out of range!")
    except OSError as e:
        print("Failed to Update Data:", e)
    except Exception as e:
        print("An error occurred:", e)