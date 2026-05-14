import os
import pandas as pd
import matplotlib.pyplot as plt
from data_module import written_comparison, comparison_df


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def interface():
    while True:
        print("(=== Data Viewer Interface ===)\n")

        print("1. View a dataset")
        print("2. Exit the program")
        print("3. Edit specific data [AUTHORISED PERSONEL ONLY!]")
        print("4. Save changes [AUTHORISED PERSONEL ONLY!]")
        print()

        choice = input("Please choose one of the following options (1-4), please.\n")

        if choice == "1":
            cls()
            print("Dataset\n")
            input("Press enter to continue, please.")
            cls()
            interface()
        
        elif choice == "2":
            cls()
            print("Exiting program...")
            break
        elif choice == "3":
            cls()
            print("Edited\n")
            input("Press enter to continue, please.")
            cls()
            interface()
        elif choice == "4":
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