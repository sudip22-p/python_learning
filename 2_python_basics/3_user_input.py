# Taking user input in Python
# input() always returns a string

name = input("Enter your name: ")  
print("Hello,", name)

# To take numeric input, convert the string to int or float
age = int(input("Enter your age: "))  
height = float(input("Enter your height in meters: "))  

print("Age:", age)
print("Height:", height)

# Note:
# Always convert input to the desired type if you want to perform numeric operations
# Otherwise, input stays as string by default
