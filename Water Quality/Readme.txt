# Mini-Project: The Water Quality Correlation Heatmap

## Objective
Now that you can load data, it's time to visualize it. 
In this project, you will use Pandas to calculate the correlation between different water quality metrics, 
and Seaborn to generate a beautiful heatmap of those relationships right inside your Jupyter Notebook.

## Step-by-Step Instructions

### Step 1: Set Up Your Notebook
1. In your workspace, create a new notebook file named `water_heatmap.ipynb`.
2. In your first code cell, import your necessary libraries: 
`import pandas as pd`, `import seaborn as sns`, and `import matplotlib.pyplot as plt`.

### Step 2: Load and Prepare Data
1. Use `pd.read_csv()` to load `environmental_data.csv` into a DataFrame named `df`.
2. Calculate the correlation matrix for the DataFrame using `df.corr()` 
and store it in a variable named `corr_matrix`. (Ensure your DataFrame only contains numeric columns for this step).

### Step 3: Plot the Heatmap
1. Use Seaborn's heatmap function to build the visual: `sns.heatmap(corr_matrix)`.
2. Make it readable by adding the parameter `annot=True` inside the heatmap function to display the exact correlation numbers on the colored squares.
3. Finally, neatly display the chart by calling `plt.show()`.

*Note: To see your heatmap, simply click inside your code cell and press **Shift + Enter** (or click the Play button at the top). 
The chart will instantly render inline right below your code!*