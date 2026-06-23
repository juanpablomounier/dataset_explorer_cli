"""
MAIN.PY

Entry point of the application.

Coordinates the complete workflow:

1. Load dataset.
2. Create DataExplorer object.
3. Analyze the dataset.
4. Display the full report.
5. Optionally filter the data.
6. Display filtered results.
"""

from loader import load
from explorer import DataExplorer
from visualizer import visualize_full_report, visualize_filtered_report

print("\n\n")
print("="*28)
print("WELCOME TO DATA EXPLORER CLI")
print("="*28)
print("\n")

while True:
    file = input("Please, enter the CSV file's path: \n") #"datasets/diverse_employee_dataset.csv"
    try:
        ds, ds_name = load(file)
        data_explorer = DataExplorer(ds, ds_name)
        data = data_explorer.analyze()
        visualize_full_report(data)
        want_filter = input("Do you want to filter the data? (y/n): ")
        if want_filter == "y" or want_filter == "yes":
            filtered_ds = data_explorer.filter_data(ds)
            visualize_filtered_report(filtered_ds)
        break
    except FileNotFoundError:
        print("Enver a valid path.")

