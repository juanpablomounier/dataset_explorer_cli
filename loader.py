"""
LOADER.PY

Contains the dataset loading functionality.

Responsibilities:
- Read CSV files.
- Return the dataframe and dataset name.
"""

import pandas as pd
import os

def load(file):
    try:
        ds = pd.read_csv(file)
        ds_name = os.path.splitext(os.path.basename(file))[0]
        print(f"CSV {ds_name} successfully loaded.\n\n")
    except FileNotFoundError:
        print("File couldn't be loaded. Please verify file's name and path.\n")
    
    return ds, ds_name