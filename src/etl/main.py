from extract import read_csv

if __name__ == "__main__":
    df = read_csv('data/sample.csv')
    print(df.head())