import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Histogram of age
df["Age"].plot(
    kind="hist", bins=5, title="Age Distribution"
)  # here, kind="hist" specifies a histogram and bins=5 specifies the number of bins - bins are the intervals into which the data is divided.
plt.xlabel("Age")
plt.savefig("7_age_histogram.png")
plt.close()

# Bar chart of average salary by department
df.groupby("Department")["Salary"].mean().plot(
    kind="bar", title="Avg Salary by Department"
)
plt.ylabel("Salary")
plt.savefig("7_avg_salary_by_department.png")
plt.close()

# Scatter plot: Salary vs Experience
df.plot(kind="scatter", x="Experience", y="Salary", title="Salary vs Experience")
plt.savefig("7_salary_vs_experience.png")
plt.close()
