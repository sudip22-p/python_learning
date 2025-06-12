import main  # Importing the main module

print("Imported main_example module.")
# Only functions are imported. The code under if __name__ == "__main__" won't run here.

# Using functions from the main module
print("sum is :", main.add(9, 4))
