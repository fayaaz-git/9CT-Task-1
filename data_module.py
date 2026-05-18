import pandas as pd
import matplotlib.pyplot as plt
import os
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')  

comparison_df = pd.read_csv(
                            "data/phone_and_book_comparison.csv",
                            header = None)

last_book_df = pd.read_csv(
                        "data/last_book_time.csv",
                        header = None)

reasons_df = pd.read_csv(
                        "data/subject_reasons.csv",
                        header = None)

complete_df = pd.read_csv(
                        "data/phone_and_book.csv",
                        header = None)

complete_df = complete_df.iloc[:,[1,2,3,4]]

def written_complete():
    print(complete_df)

def written_last():
    print(pd.read_csv(
                    "data/last_book_w.csv",
                    header=None))

def reasons():
    print(pd.read_csv(
                    "data/reasons_w.csv",
                    header=None))

def written_comparison():
    print(pd.read_csv(
                    "data/phone_book_w.csv",
                    header=None))

def visual_reasons():
    plt.bar(reasons_df[0], reasons_df[1], width=0.2,)
    plt.show()

def visual_last():
    plt.bar(last_book_df[0], last_book_df[1], width=0.2)
    plt.show()

def visual_comparison():
    plt.plot(comparison_df[0], comparison_df[1])
    plt.plot(comparison_df[0], comparison_df[2])
    plt.show()

def edit_df():
    cls()
    print("What dataset would you like to change?\n")

    print("1. Comparison Between Daily Phone and Weekly Book Usage")
    print("2. Last Time Subjects Read Books")
    print("3. Most Common Reasons for Not Reading Books")
    print("4. The Entire Survey Dataset\n")

    df_choice = input("Please choose one of the following options (1-4).\n")

    if df_choice == "2":
        cls()
        print("What data would you like to change?\n")

        print("1. Change a data value")
        print("2. Add a new row")
        print("3. Add a new column\n")

        change_choice = input("Please choose one of the following options (1-3).\n")

        if change_choice == "1":
            cls()
            print(f"{last_book_df}\n")
            final_choice = input("Choose the row whose dataset value you would like to change\n")
            data_input = input("Write the new value here: ")
            last_book_df.iloc[int(final_choice), 1] = int(data_input)
            cls()
            print(f"{last_book_df}")
            input("Press enter to continue... ")
            cls()