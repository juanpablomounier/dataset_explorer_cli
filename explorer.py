"""
EXPLORER.PY

Contains the DataExplorer class.

Responsibilities:
- Analyze datasets.
- Detect numeric columns.
- Compute descriptive statistics.
- Calculate correlation matrices.
- Identify strong correlations.
- Filter data subsets.
- Generate derived information used by the visualizer.
"""

import pandas as pd
import numpy as np

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
        treshold, strong_corr = self.get_top_correlations(ds_corr_matrix)
        

        data = {
            "name":self.name,
            "head":self.dataset.head(),
            "number_rows":ds_number_rows,
            "number_columns":ds_number_columns,
            "description":ds_description,
            "columns":ds_columns,
            "data_types":ds_dtypes,
            "nulls":ds_nulls,
            "valid_columns":ds_num_valid_columns,
            "correlation_matrix":ds_corr_matrix,
            "treshold":treshold,
            "strong_corr":strong_corr
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
    

    def get_top_correlations(self, matrix):
        while True:
            try:
                threshold = float(input("Please, enter correlation treshold: \n"))
                break
            except ValueError:
                print("Please enter a valid numbre.")
        
        upper_indices = np.triu_indices_from(matrix, k=1)
        filtered_rows = []
        columns = matrix.columns
        for i, j in zip(*upper_indices):
            var1 = columns[i]
            var2 = columns[j]
            value = matrix.iloc[i, j]
            
            if abs(value) > threshold:
                filtered_rows.append(((var1, var2), value))
        
        if filtered_rows:
            indices = [pair for pair, _ in filtered_rows]
            values = [val for _, val in filtered_rows]
            strong_corr = pd.Series(values, index=pd.MultiIndex.from_tuples(indices))
        else:
            strong_corr = pd.Series(dtype=float)

        return threshold, strong_corr
    
    def filter_data(self, dataset):
        print(f"Available columns are: \n {dataset.columns}\n")
        while True:
            column = input("Chose one column: ")
            try:
                column_dtype = dataset[column].dtype
                break
            except KeyError:
                print("Please, enter a valid column name.")
        
        print(f"Available values are: \n {dataset[column].unique()}\n")
        while True:
            value = input("Chose one value: ")
            try:
                final_value = column_dtype.type(value)
                break
            except ValueError:
                print("Please, enter a valid value.")
        
        filtered_ds = dataset[dataset[column] == final_value]
        if filtered_ds.empty:
            print("Empty dataset.")
            exit()
        head = filtered_ds.head()
        description = filtered_ds.describe()
        average_salary = filtered_ds["salary_usd"].mean()
        average_experience = filtered_ds["years_experience"].mean()

        filtered = {
            "ds":filtered_ds,
            "head":head,
            "description":description,
            "average_salary":average_salary,
            "average_experience":average_experience
        }

        return filtered
