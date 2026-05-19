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

    if df_choice == "1":
        cls()
        comparison_w_df = pd.read_csv(
             "data/phone_book_w.csv",
             header=0)
        print(f"{comparison_df}\n")
        column_choice = int(input("Choose the column whose dataset value you would like to change (1-2)? "))
        final_choice = int(input("Choose the row whose dataset value you would like to change (0-5)\n"))
        data_input = int(input("Write the new value here: "))
        comparison_df.iloc[final_choice, column_choice] = data_input
        comparison_w_df.iloc[final_choice, column_choice] = data_input
        cls()
        print(f"{comparison_df}")
        save_choice = input("Do you want to save (yes/no)?\n")
        if save_choice.lower() == "yes":
            comparison_df.to_csv("data/phone_and_book_comparison.csv", index=False, header=False)
            comparison_w_df.to_csv("data/phone_book_w.csv", index=False, header=True)
            input("Saved. Press enter to continue...")
        elif save_choice.lower() == "no":
            input("Press enter to continue...")
        cls()

    elif df_choice == "2":
        cls()
        last_w_df = pd.read_csv(
             "data/last_book_w.csv",
             header=0)
        print(f"{last_book_df}\n")
        final_choice = int(input("Choose the row whose dataset value you would like to change (0-4)\n"))
        data_input = input("Write the new value here: ")
        last_book_df.iloc[final_choice, 1] = data_input
        last_w_df.iloc[final_choice, 1] = data_input
        cls()
        print(f"{last_book_df}")
        save_choice = input("Do you want to save (yes/no)?\n")

        if save_choice.lower() == "yes":
            last_book_df.to_csv("data/last_book_time.csv", index=False, header=False)
            last_w_df.to_csv("data/last_book_w.csv", index=False, header=True)
            input("Saved. Press enter to continue...")
        elif save_choice.lower() == "no":
            input("Press enter to continue...")
        cls()
    
    elif df_choice == "3":
        cls()
        reasons_w_df = pd.read_csv(
             "data/reasons_w.csv",
             header=0)
        cls()
        print(f"{reasons_df}\n")
        final_choice = int(input("Choose the row whose dataset value you would like to change (0-7)\n"))
        data_input = input("Write the new value here: ")
        reasons_df.iloc[final_choice, 1] = data_input
        reasons_w_df.iloc[final_choice, 1] = data_input
        cls()
        print(f"{reasons_df}")
        save_choice = input("Do you want to save (yes/no)?\n")

        if save_choice.lower() == "yes":
            reasons_df.to_csv("data/subject_reasons.csv", index=False, header=False)
            reasons_w_df.to_csv("data/reasons_w.csv", index=False, header=True)
            input("Saved. Press enter to continue...")
        elif save_choice.lower() == "no":
            input("Press enter to continue...")
        cls()

    elif df_choice == "4":
        cls()
        print(f"{complete_df}\n")
        column_choice = int(input(f"Choose the column whose dataset value you would like to change (0 - 4)? "))
        final_choice = int(input(f"Choose the row whose dataset value you would like to change (0 - {len(complete_df) - 1})\n"))
        data_input = input("Write the new value here: ")
        complete_df.iloc[final_choice, column_choice] = data_input
        cls()
        print(f"{complete_df}")
        save_choice = input("Do you want to save (yes/no)?\n")
        if save_choice.lower() == "yes":
            complete_df.to_csv("data/phone_and_book.csv", index=False, header=True)
            input("Saved. Press enter to continue...")
        elif save_choice.lower() == "no":
            input("Press enter to continue...")
        cls()
        