from . import database
from .utils import id_generator
import time
import os

def read(**kwargs):
    try:
        with open(database.database_name, 'r') as file:
            content = file.readlines()
            total_name = len(content)

            if "index" in kwargs:
                index_name = kwargs["index"]-1

                if index_name < 0 or index_name > total_name:
                    return False
                else:
                    return content[index_name]
            else:
                return content
    except:
        print("Error Reading Database")
        return False
    
def create(actor_name, actor_gender, movie_title, year_of_release):
    data = database.TEMPLATE.copy()

    data["id"] = id_generator(6)
    data["timestamp"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["actor_name"] = actor_name + database.TEMPLATE["actor_name"][len(actor_name):]
    data["actor_gender"] = actor_gender + database.TEMPLATE["judul"][len(actor_gender):]
    data["movie_title"] = movie_title + database.TEMPLATE["judul"][len(movie_title):]
    data["year_of_release"] = str(year_of_release)

    data_str = f'{data["id"]},{data["timestamp"]},{data["actor_name"]},{data["actor_gender"]},{data["movie_title"]},{data["year_of_release"]}\n'

    try:
        with open(database.database_name, 'a', encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("!!Failed to Add Data to database!!")

def update(no_data, id, actor_name, actor_gender, movie_title, year_of_release):
    data = database.TEMPLATE.copy()

    data["id"] = id
    data["timestamp"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["actor_name"] = actor_name + database.TEMPLATE["actor_name"][len(actor_name):]
    data["actor_gender"] = actor_gender + database.TEMPLATE["judul"][len(actor_gender):]
    data["movie_title"] = movie_title + database.TEMPLATE["judul"][len(movie_title):]
    data["year_of_release"] = str(year_of_release)

    data_str = f'{data["id"]},{data["timestamp"]},{data["actor_name"]},{data["actor_gender"]},{data["movie_title"]},{data["year_of_release"]}\n'

    data_length = len(data_str)

    try:
        with open(database.database_name, 'r+', encoding="utf-8") as file:
            file.seek(data_length*(no_data - 1))
            file.write(data_str)
    except:
        print("!!Failed to Update Data!!")

def delete(no_data):
    try:
        with open(database.database_name, 'r') as file:
            counter = 0

            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_data - 1:
                    pass
                else:
                    with open("data_temp.txt", 'a', encoding="utf-8") as temp_file:
                        temp_file.writable(content)

                counter += 1
    except:
        print("!!Error Something Wrong!!")
    
    os.rename("data_temp.text", database.database_name)