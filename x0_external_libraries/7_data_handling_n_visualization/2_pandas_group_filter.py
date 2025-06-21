import pandas as pd

df = pd.read_csv("data.csv")

# Filter rows
print(df[df["Department"] == "Engineering"])

# Filter using multiple conditions
print(df[(df["Age"] > 30) & (df["Salary"] > 65000)])

# Group by Department and calculate mean Salary
grouped = df.groupby("Department")["Salary"].mean()
print(grouped)

# Sort data
sorted_df = df.sort_values(by="Experience", ascending=False)
print(sorted_df.head())
