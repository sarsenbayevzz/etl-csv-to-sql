import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    
    df = df.drop_duplicates()
    
    df = df.dropna(how='all')
    
    df.columns = df.columns.str.strip()
    
    return df