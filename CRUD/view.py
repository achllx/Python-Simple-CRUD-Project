from . import action

def read_console():
    data =  action.read()

    index = "No"
    actor_name = "Actor Name"
    actor_gender = "actor_gender"
    movie_title = "Movie Title"
    year_of_release = "Year of Release"

    # table header
    print("\n"+"="*100)
    print(f"{index:4} | {actor_name:30} | {actor_gender:10} | {movie_title: 20} | {year_of_release:15}")
    print("-"*100)

    # Table content
    for index, data in enumerate(data):
        data_break = data.split(",")
        
        actor_name = data_break[2]
        actor_gender = data_break[3]
        movie_title = data_break[4]
        year_of_release = data_break[5][:-1]

        print(f"{index+1:4} | {actor_name:30} | {actor_gender:10} | {movie_title: 20} | {year_of_release:15}", end="")

    print("="*100+"\n")

def create_console():
    print("\n"+"="*100)
    print("Please Add Data\n")
    
    actor_name = input("Actor Name\t:")
    actor_gender = input("Actor Gender\t:")
    movie_title = input("Movie Title\t:")

    while True:
        try:
            year_of_release = input("Year of Release\t:")

            if len(str(year_of_release)) == 4:
                break
            else:
                print("The year only has 4 digits")
        except:
            print("year of release must be a number")
    
    action.create(actor_name, actor_gender, movie_title, year_of_release)

    print("\nSuccess Add New Data")
    read_console()

def delete_console():
    read_console()
    while True:
        print("Please select the data index to delete")

        data_index = int(input("Data Index: "))
        data = action.read(index=data_index)

        if data:
            data_break = data.split(",")
            actor_name = data_break[2]
            actor_gender = data_break[3]
            movie_title = data_break[4]
            year_of_release = data_break[5][:-1]

            # show the data
            print("\n"+"="*100)
            print("The data you want to delete")
            print("\n"+"="*100)

            index = "No"
            actor_name = "Actor Name"
            actor_gender = "actor_gender"
            movie_title = "Movie Title"
            year_of_release = "Year of Release"

            print(f"{index:4} | {actor_name:30} | {actor_gender:10} | {movie_title: 20} | {year_of_release:15}")
            print("-"*100)
            print(f"{data_index:4} | {actor_name:30} | {actor_gender:10} | {movie_title: 20} | {year_of_release:15}", end="")
            print("="*100+"\n")

            is_delete = input("Are you sure want to delete it (y/n)?: ").lower()
            
            if is_delete == "y":
                action.delete(data_index)
                break
        else:
            print("Not a Valid Index, Try Again")

    print("Success Delete Data")

def update_console():
    read_console()
    
    while True:
        print("Please select the data index to update")

        data_index = int(input("Data Index: "))
        data = action.read(index=data_index)

        if data:
            break
        else:
            print("Not a Valid Index, Try Again")
    
    data_break = data.split(",")
    id = data_break[0]
    timestamp = data_break[1]
    actor_name = data_break[2]
    actor_gender = data_break[3]
    movie_title = data_break[4]            
    year_of_release= data_break[5][:-1]

    while True:
        print("\n"+"="*100)
        print("Please select what data you want to change")
        print(f"1. Actor Name\t: {actor_name:.40}")
        print(f"2. Actor Gender\t: {actor_gender:.40}")
        print(f"3. Movie Title\t: {movie_title:.40}")
        print(f"4. Year of Release\t: {year_of_release:4}")

        user_option = input("Select field [1,2,3]: ")
        print("\n"+"="*100)

        match user_option:
            case "1": actor_name = input("New Actor Name\t: ")
            case "2": actor_gender = input("New Actor Gender\t: ")
            case "3": movie_title = input("New Movie Title\t: ")
            case "4": 
                while True:
                    try:
                        year_of_release = input("New Year of Release\t: ")

                        if len(str(year_of_release)) == 4:
                            break
                        else:
                            print("The year only has 4 digits")
                    except:
                        print("year of release must be a number")
            case _: print("!!please select the correct field!!")

        print("-"*100)
        print(f"1. Actor Name\t: {actor_name:.40}")
        print(f"2. Actor Gender\t: {actor_gender:.40}")
        print(f"3. Movie Title\t: {movie_title:.40}")
        print(f"4. Year of Release\t: {year_of_release:4}")

        is_correct = input("Is the data correct (y/n)? ").lower()
        
        if is_correct == "y":
            action.update(
                    data_index, 
                    id, 
                    actor_name, 
                    actor_gender,
                    movie_title,
                    year_of_release)
        
        is_done = input(f"Do you still want to update data on index {data_index} (y/n)?").lower()

        if is_done == "n":
            break