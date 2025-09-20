import pandas as pd
from sqlalchemy import create_engine

def load_to_sql(df: pd.DataFrame, db_path: str, table_name: str):
    engine = create_engine(f'sqlite:///{db_path}')
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f'Data loaded into table "{table_name}" (SQLite DB: {db_path})')