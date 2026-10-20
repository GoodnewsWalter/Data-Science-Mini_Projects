# Mini-Project: Environmental Data Quick-Scan

## Objective
In this project, you will use Pandas to load and perform an initial inspection of a raw environmental dataset right inside your Jupyter Notebook. 
This is always the very first step a data analyst takes when receiving new data.

## Step-by-Step Instructions

### Step 1: Set Up Your Notebook
1. Create a new notebook file named `data_scan.ipynb`.
2. Ensure you have the mock dataset available in your workspace (assume it is named `environmental_data.csv`).

### Step 2: Import Pandas and Load the Data
1. In your first code cell, import the pandas library using its standard alias (`import pandas as pd`).
2. Use the `pd.read_csv()` function to load `environmental_data.csv` and store it in a variable named `df` (short for DataFrame).

### Step 3: Inspect the Data
Write the code to generate the following three essential views of your data. (You can do this in one cell or spread it across multiple cells):
1. **The Head:** Display the first 5 rows of the dataset using the `.head()` method.
2. **The Info:** Print the structural information of the dataset (columns, non-null counts, data types) using the `.info()` method.
3. **The Summary Statistics:** Display the statistical summary (mean, min, max, etc.) of the numeric columns using the `.describe()` method.

*Note: To view your data insights, simply click inside your code cells and press **Shift + Enter** (or click the Play button at the top). 
One of the best parts of using a Jupyter Notebook is that methods like `.head()` and `.describe()` will render as beautiful, easy-to-read tables right below your code!*