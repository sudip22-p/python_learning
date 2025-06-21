import pandas as pd
import numpy as np

# NumPy is a powerful library in Python that allows you to work with large arrays and matrices of numerical data. It provides tools for performing mathematical operations on these arrays efficiently, making it a fundamental package for scientific computing and data analysis in Python.

# Create sample data with missing values
data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [
        25,
        np.nan,
        30,
        28,
    ],  # what if i put nan instead of np.nan?  NameError: name 'nan' is not defined
    "Salary": [50000, 60000, np.nan, 70000],
}
df = pd.DataFrame(
    data
)  # Create DataFrame with missing values . what is dataframe? A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types, similar to a spreadsheet or SQL table. It is one of the primary data structures in pandas, designed for data manipulation and analysis.

# Show data
print("Original:\n", df)

# Drop rows with any missing values
print("\nDrop rows with NaN:\n", df.dropna())

# Fill missing values
df_filled = df.fillna(
    {"Age": df["Age"].mean(), "Salary": df["Salary"].median()}
)  # Fill missing values with mean for Age and median for Salary
print("\nAfter filling:\n", df_filled)

# Check for nulls
print("\nNull count:\n", df.isnull().sum())  # Count of null values in each column
