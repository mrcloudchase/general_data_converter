import pandas as pd
import json

def read_json(input_file: str) -> pd.DataFrame:
    with open(input_file, 'r') as f:
        data = pd.read_json(f)
    return data

def write_json(data: pd.DataFrame, output_file: str):
    with open(output_file, 'w') as f:
        f.write(data.to_json(orient='records', lines=True))
