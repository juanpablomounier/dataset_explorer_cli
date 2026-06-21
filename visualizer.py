"""
VISUALIZER.PY

Shows the analysis in the terminal.
"""
import matplotlib.pyplot as plt

def visualize(data):
    print(f"The dataset's head is: \n {data["head"]}")
    print(f"The dataframe's shape is: \n Rows: {data["number_rows"]}\n Columns: {data["number_columns"]}\n")
    print("-"*25)
    print("\n")
    print(f"Numeric columns are: \n")
    for column in list(data["valid_columns"]):
        print(column)
    print("\n")
    print("-"*25)
    print("\n")
    print("Analyzing and creating figures...")
    print("\n")
    print("-"*25)

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
    plt.show()
    plt.close()


