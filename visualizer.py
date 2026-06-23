"""
VISUALIZER.PY

Contains presentation utilities.

Responsibilities:
- Display the full report.
- Display filtered reports.
- Generate histogram images.
- Generate correlation matrix images.
- Provide loading animations.

No analysis or business logic should be implemented here.
"""
import matplotlib.pyplot as plt
import time
import itertools

def visualize_full_report(data):
    print(f"The {data["name"]} dataset's head is: \n {data["head"]}")
    print("\n")
    print("-"*25)
    print("\n")
    print(f"The dataframe's shape is: \n Rows: {data["number_rows"]}\n Columns: {data["number_columns"]}\n\n")
    print("\n")
    print("-"*25)
    print("\n")
    print(f"Dataset description: \n {data["description"]}")
    print("\n")
    print("-"*25)
    print("\n")
    print(f"Columns are: \n")
    for column in list(data["columns"]):
        print(column)
    print("\n")
    print("-"*25)
    print("\n")
    print(f"Data types are: \n")
    print(data["data_types"])
    print("\n")
    print("-"*25)
    print("\n")
    print(f"Numeric columns are: \n")
    for valid_column in list(data["valid_columns"]):
        print(valid_column)
    print("\n")    
    print("-"*25)
    print("\n")
    print(f"Missing values are: \n")
    print(data["nulls"])
    print("\n")
    print("-"*25)
    print("\n")
    print(f"Correlation matrix is: \n")
    print(f"{data["correlation_matrix"]}")
    print("\n")
    print("-"*25)
    print("\n")
    print(f"Correlations above {data["treshold"]} are:\n")
    for (var1, var2), valor in data["strong_corr"].items():
        print(f"Variables: {var1} <-> {var2} | Correlation: {valor:.4f}")
    print("\n")
    print("-"*25)
    print("\n")
    loading("Analyzing and creating figures...")
    print("\n")
    print("-"*25)
    print("\n")

    for column in data["valid_columns"].columns:
        plt.hist(data["valid_columns"][column], bins=10)
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.title(f"{column} distribution")
        figname = str(data["name"] + "__" + column + ".jpg")
        plt.savefig("outputs/histograms/"+figname, dpi=300, bbox_inches='tight')
        plt.close()


    plt.figure(figsize=(10, 8))
    plt.imshow(data["correlation_matrix"], cmap='coolwarm', vmin=-1, vmax=1)
    plt.colorbar()
    columns = data["correlation_matrix"].columns
    plt.xticks(range(len(columns)), columns, rotation=45, ha='right')
    plt.yticks(range(len(columns)), columns)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    figname = str(data["name"] + "__Correlation Matrix.jpg")
    plt.savefig("outputs/correlations/"+figname, dpi=300, bbox_inches='tight')
    plt.close()


def visualize_filtered_report(data):
    print(f"The sub-dataset's head is: \n{data["head"]}\n")
    print(f"Description: \n {data["description"]} \n")
    print(f"The average USD salary is: {data["average_salary"]:,.2f} \n")
    print(f"The average years experience is: {data["average_experience"]:.1f} \n")



def loading(message):
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    end_time = time.time() + 2  # 2 segundos

    while time.time() < end_time:
        print(f"\r{message} {next(spinner)}", end="", flush=True)
        time.sleep(0.1)

    print(f"\r{message} ✓")