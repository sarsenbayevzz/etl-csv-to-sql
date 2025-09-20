import pandas as pd
from pathlib import Path

def read_csv(file_path: str) -> pd.DataFrame:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f'File {file_path} not found.')
    return pd.read_csv(path)

def read_excel(file_path: str, sheet_name=0) -> pd.DataFrame:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f'File {file_path} not found.')
    return pd.read_excel(path, sheet_name=sheet_name)