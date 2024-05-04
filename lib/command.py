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
    except:
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
    except:
        print("!!Failed to Create Data!!")
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
    except:
        print("!!Something Wrong!!")
    
    os.remove(database.database_name)
    os.rename("data_temp.txt", database.database_name)