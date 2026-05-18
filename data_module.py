import pandas as pd
import matplotlib.pyplot as plt


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
    print(reasons_df)

def written_comparison():
    print(comparison_df)

def visual_reasons():
    plt.bar(reasons_df[0], reasons_df[1], width=0.3,)
    plt.show()

def visual_last():
    plt.bar(last_book_df[0], last_book_df[1], width=0.3)
    plt.show()

def visual_comparison():
    plt.plot(comparison_df[0], comparison_df[1])
    plt.plot(comparison_df[0], comparison_df[2])
    plt.show()