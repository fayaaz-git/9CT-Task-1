import pandas as pd
import matplotlib.pyplot as plt


comparison_df = pd.read_csv(
                            "data/phone_and_book_comparison.csv",
                            header = None)

complete_df = pd.read_csv(
                        "data/phone_and_book.csv",
                        header = None)

complete_df = complete_df.iloc[:,[1,2,3,4]]

def written_complete():
    print(complete_df)

def written_comparison():
    print(comparison_df)

written_complete()