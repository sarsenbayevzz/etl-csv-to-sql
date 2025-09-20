from extract import read_csv
from transform import clean_data

if __name__ == "__main__":
    df = read_csv('data/sample.csv')
    print("Original data:")
    print(df.head())
    
    df_clean = clean_data(df)
    print("\nCleaned data:")
    print(df_clean.head())