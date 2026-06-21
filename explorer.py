"""
EXPLORER.PY

Analyzes a few elements of the dataframe and save them into returnable variables for showing purposes.
"""

import pandas as pd

class DataExplorer:
    def __init__(self, dataset, ds_name):
        self.dataset = dataset
        self.name = ds_name
        #self.insights
        #self.filtered_data


    def analyze(self):
        ds_number_rows, ds_number_columns = self.dataset.shape
        ds_columns = self.dataset.columns
        ds_dtypes = self.dataset.dtypes
        ds_num_valid_columns = self.filter_valid_columns(self.dataset)
        ds_nulls = self.dataset.isnull().sum()
        ds_description = self.dataset.describe()
        ds_corr_matrix = ds_num_valid_columns.corr()
        

        data = {
            "name":self.name,
            "head":self.dataset.head(),
            "number_rows":ds_number_rows,
            "number_columns":ds_number_columns,
            "columns":ds_columns,
            "data_types":ds_dtypes,
            "nulls":ds_nulls,
            "description":ds_description,
            "valid_columns":ds_num_valid_columns,
            "correlation_matrix":ds_corr_matrix
        }

        return data
    
    def filter_valid_columns(self, dataset):
        ds_num_valid_columns = dataset.select_dtypes(include=["number"])
        invalid_columns = []
        for column in ds_num_valid_columns:
            if "id" in column:
                invalid_columns.append(column)
        ds_num_valid_columns = ds_num_valid_columns.drop(columns=invalid_columns, errors='ignore')
        return ds_num_valid_columns