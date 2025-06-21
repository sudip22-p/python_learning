import pandas as pd

# Employee data
employees = pd.DataFrame(
    {
        "ID": [1, 2, 3, 4],
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "DeptID": [101, 102, 101, 103],
    }
)

# Department data
departments = pd.DataFrame(
    {"DeptID": [101, 102, 103], "Department": ["Engineering", "Marketing", "HR"]}
)
hobbies = pd.DataFrame(
    {"DeptID": [101, 102, 109], "Department": ["Cricket", "Cooking", "Gardening"]}
)
# Merge on DeptID
merged = pd.merge(employees, departments, on="DeptID")
print("Merged Data:\n", merged)

# Left Join Example
left_join = pd.merge(
    employees, hobbies, on="DeptID", how="left"
)  # Left join keeps all records from the left DataFrame (employees) and matches with the right DataFrame (departments)
# If there is no match, NaN is filled in the columns from the right DataFrame
print("\nLeft Join:\n", left_join)

# Right Join Example
right_join = pd.merge(
    employees, hobbies, on="DeptID", how="right"
)  # Right join keeps all records from the right DataFrame (hobbies) and matches with the left DataFrame (employees)
# If there is no match, NaN is filled in the columns from the left DataFrame
print("\nRight Join:\n", right_join)


# similarly there are innter join, outer join, cross join etc.
