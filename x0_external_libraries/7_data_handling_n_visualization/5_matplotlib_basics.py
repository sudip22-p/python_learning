import matplotlib.pyplot as plt
import matplotlib.image as mpimg  # to save and display image files
import numpy as np

# Line plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.figure()
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.savefig("5_line_plot.png")  # save the plot as line_plot.png
plt.close()

# Bar chart
plt.figure()
plt.bar(["A", "B", "C"], [5, 8, 3])
plt.title("Bar Chart")
plt.savefig("5_bar_chart.png")  # save the plot as bar_chart.png
plt.close()

# Histogram
data = np.random.randn(1000)
plt.figure()
plt.hist(data, bins=20)
plt.title("Histogram")
plt.savefig("5_histogram.png")  # save the plot as histogram.png
plt.close()
