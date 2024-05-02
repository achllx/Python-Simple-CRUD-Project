import random
import string

def id_generator(length:int) -> str:
    result = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result