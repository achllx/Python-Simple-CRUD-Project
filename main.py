import lib
# inisiasi project
if __name__ == "__main__":
    lib.init_database()

    # membuat header sambutan dan opsi
    while True:
        lib.clean_console()

        print("!!CRUD Simple Program!!")
        print("="*23)
        print("what you want to do?\n")
        print(f"1. show data")
        print(f"2. create new data")
        print(f"3. update data")
        print(f"4. delete data")
        print(f"5. exit program\n")

        try:
            user_option = int(input("Masukan nomor opsi yang mau di lakukan(1-5): "))

            match user_option:
                case 1: lib.read_console()
                case 2: lib.create_console()
                case 3: print(f"3. update data")
                case 4: print(f"4. delete data")
                case 5: break
                case _:
                    print("!!Opsi Hanya Angka 1 - 5!!\n")
                    input("Press Enter to Continue")
                    continue
        except:
            print("!!Opsi Harus Berupa Angka!!\n")
            input("Press Enter to Continue")
            continue

print("\nProgram Ended.")