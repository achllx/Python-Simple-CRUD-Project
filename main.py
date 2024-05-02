import os

if __name__ == "__main__":

    operating_system = os.name
    

    while True:

        # clear terminal for both windows and mac os
        match operating_system:

            case "posix": os.system('clear')
            case "nt": os.system('cls')

        print("DATABASE")
        print("="*20+"\n")
        print(f"Option:")
        print(f"1. Add data")
        print(f"2. Update data")
        print(f"3. Delete data\n")

        user_option = input("What you want to do?: ")

        match user_option:
            case "1": print("add")
            case "2": print("update")
            case "3": print("delete")

        # stop the program
        is_done = input("Are you Done? (y/n): ").lower()
        if is_done == 'y':
            break

print("Program Ended.")