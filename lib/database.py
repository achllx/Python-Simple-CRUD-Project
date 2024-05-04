import os
database_name = "weapon.txt"

template = {
    "id":"",
    "timestamp":"",
    "name":"",
    "rarity":"",
    "price":"",
}

def init_database():
    try:
        with open(database_name, 'r') as file:
            pass
    except:
        with open(database_name, 'w') as file:
            pass

def init_temp():
    if os.path.exists("data_temp.txt"):
        # empty the file if already exist
        with open("data_temp.txt", 'w', encoding="utf-8") as temp_file:
            temp_file.truncate(0) 
    else:
        # if not exist create new one
        with open("data_temp.txt", 'w', encoding="utf-8") as temp_file:
            pass  