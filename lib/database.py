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