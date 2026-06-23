# DATA EXPLORER CLI

A command-line application for quickly exploring CSV datasets using Python and Pandas.

## Features

* Load any CSV dataset interactively.
* Display dataset dimensions.
* Show columns and data types.
* Detect missing values.
* Generate descriptive statistics.
* Automatically detect valid numeric columns.
* Ignore ID columns for analysis.
* Create histograms for numeric variables.
* Generate a correlation matrix image.
* Display correlations above a user-defined threshold.
* Filter the dataset interactively.
* Generate statistics for filtered subsets.
* Basic error handling for invalid inputs.

## Project Structure

```
DATA_EXPLORER_CLI/

datasets/

outputs/
├── histograms/
└── correlations/

main.py
loader.py
explorer.py
visualizer.py
```

## Requirements

* Python 3.13
* pandas
* numpy
* matplotlib

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Then enter the path to a CSV file when prompted.

Example:

```text
datasets/diverse_employee_dataset.csv
```

## Output

The application provides:

* Dataset overview
* Missing values report
* Descriptive statistics
* Correlation analysis
* Histograms
* Correlation matrix image
* Interactive filtering
* Statistics for filtered data

## Author

Juan Pablo Mounier


Github: https://github.com/juanpablomounier