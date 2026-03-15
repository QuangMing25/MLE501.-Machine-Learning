import pandas as pd
import sys

# Read the Data Dictionary
file_path = "GiveMeSomeCredit Dataset/Data Dictionary.xls"

try:
    # Try reading the Excel file
    df = pd.read_excel(file_path)

    print("=" * 80)
    print("DATA DICTIONARY - Give Me Some Credit")
    print("=" * 80)
    print()

    # Display the content
    for idx, row in df.iterrows():
        print(f"{idx + 1}. {row.iloc[0]}")
        if len(row) > 1:
            for col_idx in range(1, len(row)):
                if pd.notna(row.iloc[col_idx]):
                    print(f"   {row.iloc[col_idx]}")
        print()

    print("=" * 80)

    # Also show the raw dataframe
    print("\nRaw DataFrame:")
    print(df.to_string())

except Exception as e:
    print(f"Error reading file: {e}")
    print("\nTrying alternative method...")

    # If xlrd is not available, show CSV columns instead
    df_train = pd.read_csv("GiveMeSomeCredit Dataset/cs-training.csv")
    print("\nColumns in training data:")
    print(df_train.columns.tolist())
    print(f"\nShape: {df_train.shape}")
    print("\nFirst few rows:")
    print(df_train.head())
