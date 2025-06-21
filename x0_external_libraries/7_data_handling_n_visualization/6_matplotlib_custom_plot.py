import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 35]
y2 = [5, 15, 20, 25, 30]

# Multiple lines with labels, i.e 	Custom line plot with 2 lines
plt.plot(x, y1, label="Series 1", color="blue", marker="o")
plt.plot(x, y2, label="Series 2", color="green", linestyle="--")

plt.title("Custom Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid(True)

# Save plot
plt.savefig("6_custom_plot.png")
# plt.show() #won't work in this environment coz it doesn't support GUI
# TO display the image, you can use matplotlib's image module and it will display in the Jupyter Notebook or similar environments
# close the plot to free up memory
plt.close()
