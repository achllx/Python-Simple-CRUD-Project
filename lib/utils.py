import random
import string
import os

def generate_id(length=6):
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(characters) for _ in range(length))
    return random_id

def clean_console():
     operation_system = os.name

     match operation_system:
            case "posix": os.system("clear") #m macOS
            case "nt": os.system("cls") # windowsmatch operation_system: