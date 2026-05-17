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
    print(last_book_df)

def reasons():
    print(reasons_df)

def written_comparison():
    print(comparison_df)

def visual_reasons(reasons_df):
    x = reasons_df['Most Common Reasons for Disuse of Books']
    y = reasons_df['People Who Said Yes']
    plt.bar(x, y)
    plt.show()

visual_reasons(reasons_df)