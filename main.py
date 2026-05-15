import os                                                                                                   # Imports OS
import pandas as pd                                                                                         # Imports Pandas (should be in data module but just in case)
import matplotlib.pyplot as plt                                                                             # Imports Matplotlib (should be in data module but just in case)
from data_module import *      # Imports everything from data module


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')                                                        # Makes a function to clear everything in terminal if triggered

def dataset():                                                                                              # Function that allows specific datasets to be displayed in certain ways if triggered
    print("DATASET VIEWER\n")

    print("1. Show the dataset")
    print("2. Show a visual representation of the data\n")

    rep_choice = input("Please choose one of the following options (1-2).\n")

    if rep_choice == "1":
        cls()
        print("DATASET VIEWER\n")

        print("Choose your dataset:")
        print("1. Comparison Between Daily Phone and Weekly Book Usage")
        print("2. Last Time Subjects Read Books")
        print("3. Most Common Reasons for Not Reading Books")
        print("4. The Entire Survey Dataset\n")

        data_choice = input("Please choose one of the following options (1-4).\n")

        if data_choice == "1":
            cls()
            written_comparison()
            input("Press enter to continue...")
        
        elif data_choice == "2":
            cls()
            written_last()
            input("Press enter to continue")

        elif data_choice == "3":
            cls()
            reasons()
            input("Press enter to continue...")
        
        elif data_choice == "4":
            cls()
            written_complete()
            input("Press enter to continue")
        
        else:
            cls()
            print("ERROR!\n")
            input("Press enter to continue...")
    
    elif rep_choice == "2":
        cls()
        print("DATASET VIEWER\n")

        print("Choose your visual:")
        print("1. Comparison Between Daily Phone and Weekly Book Usage")
        print("2. Last Time Subjects Read Books")
        print("3. Most Common Reasons for Not Reading Books\n")

        data_choice = input("Please choose one of the following options (1-4).\n")

        if data_choice == "1":
            cls()
            visual_comparison()
            input("Press enter to continue...")

def interface():
    while True:
        print("(=== Data Viewer Interface ===)\n")

        print("1. View a dataset")
        print("2. Exit the program")
        print("3. Edit specific data [AUTHORISED PERSONEL ONLY!]")
        print("4. Save changes [AUTHORISED PERSONEL ONLY!]\n")

        choice = input("Please choose one of the following options (1-4).\n")

        if choice == "1":
            cls()
            dataset()
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

cls()
interface()