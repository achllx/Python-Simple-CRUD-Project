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

    data_str = f'{data["id"]},{data["timestamp"],data["name"]},{data["rarity"]},{data["price"]}\n'

    try:
        with open(database.database_name, 'a', encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("!!Failed to Create Data!!")