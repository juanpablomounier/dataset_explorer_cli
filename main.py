"""
MAIN.PY

Orchestrates the pipeline. It call all the methods in order to load, analyze and show data.
"""

from loader import load
from explorer import DataExplorer
from visualizer import visualize

print("="*28)
print("WELCOME TO DATA EXPLORER CLI")
print("="*28)
print("\n")


file = input("Por favor, ingrese la ruta del archivo CSV que quiere analizar: ") #"datasets/diverse_employee_dataset.csv"
ds, ds_name = load(file)

data_explorer = DataExplorer(ds, ds_name)
data = data_explorer.analyze()
visualize(data)

#shape, numeric_columns, corr_matrix = analyze(df)"
#visualize(df, df_name, shape, numeric_columns, corr_matrix)
