import pandas as pd

# Load CSV
df = pd.read_csv("data.csv")

# View data
print(df.head())  # this line shows the first few rows of the DataFrame
print("--------------------------------------------")
print(df.tail())  # this line shows the last few rows of the DataFrame
print("--------------------------------------------")
print(
    df.info()
)  # this line provides a concise summary of the DataFrame, like the number of entries, column names, data types, and non-null counts
print("--------------------------------------------")

# Describe data
print(
    df.describe()
)  # this line generates descriptive statistics of the DataFrame, such as count, mean, std, min, 25%, 50%, 75%, and max for numeric columns
print("--------------------------------------------")

# Access column
print(df["Name"])  # this line accesses the "Name" column of the DataFrame
print("--------------------------------------------")
print(
    df[["Name", "Age"]]
)  # this line accesses multiple columns, "Name" and "Age", of the DataFrame
print("--------------------------------------------")

# Add new column
df["Bonus"] = (
    df["Salary"] * 0.1
)  # this line adds a new column "Bonus" to the DataFrame, which is 10% of the "Salary" column
print(
    df.head()
)  # this line shows the first few rows of the modified DataFrame with the new "Bonus" column
print("--------------------------------------------")

# Save modified file
df.to_csv(
    "data_modified.csv", index=False
)  # this line saves the modified DataFrame to a new CSV file named "data_modified.csv" without including the index
