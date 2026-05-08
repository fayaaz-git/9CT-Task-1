import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def interface():
    while True:
        print("(=== Data Viewer Interface ===)\n")

        print("1. View written dataset")
        print("2. View visualisation of data")
        print("3. View specific datasets")
        print("4. Exit the program")
        print("5. Edit specific data [AUTHORISED PERSONEL ONLY!]")
        print("6. Save changes [AUTHORISED PERSONEL ONLY!]")
        print()

        choice = input("Please choose one of the following options (1-6), please.\n")

        if choice == "1":
            cls()
            print("Dataset\n")
            input("Press enter to continue, please.")
            cls()
            interface()
        elif choice == "2":
            cls()
            print("Visualisation\n")
            input("Press enter to continue, please.")
            cls()
            interface()
        elif choice == "3":
            cls()
            print("Specific Dataset\n")
            input("Press enter to continue, please.")
            cls()
            interface()
        elif choice == "4":
            cls()
            print("Exiting program...")
            break
        elif choice == "5":
            cls()
            print("Edited\n")
            input("Press enter to continue, please.")
            cls()
            interface()
        elif choice == "6":
            cls()
            print("Saved\n")
            input("Press enter to continue, please.")
            cls()
            interface()
        else:
            cls()
            print("ERROR!\n")
            input("Press enter to continue, please.")
            cls()

interface()