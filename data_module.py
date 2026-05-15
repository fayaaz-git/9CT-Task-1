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

correct_order = [
                "> 1 hour",
                "1 - 2 hours",
                "2 - 4 hours",
                "4 - 8 hours",
                "8+ hours (phone) / 8 - 16 hours (book)",
                "16+ hours (book)"
]

def visual_comparison(comparison_df):
    plt.plot(comparison_df["Amount people who spend this amount of time on..."], comparison_df["Their phone (daily)"], label="Daily Phone Usage", marker="o")
    plt.plot(comparison_df["Amount people who spend this amount of time on..."], comparison_df["A book (weekly, in spare time)"], label="Weekly Book Usage", marker="o")