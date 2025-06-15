# Writing to a file (creates or overwrites if exists)
file = open("1_sample.txt", "w")
file.write("Hello, this is a test file.\n")
file.write("Second line.\n")
file.close()  # Important: always close the file

# Reading the entire file
file = open("1_sample.txt", "r")
print("📄 Reading file using read():")
print(file.read())
file.close()

# Appending to the file
file = open("1_sample.txt", "a")
file.write("Appended line.\n")
file.close()

# Reading again after append
file = open("1_sample.txt", "r")
print("📄 After appending:")
print(file.read())
file.close()

# Best practice: using 'with' block (auto closes the file)
print("📄 Reading using 'with' block:")
with open("1_sample.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character
with open("1_sample.txt", "r") as file:
    print(file.read())

# File modes recap (commented)
"""
'r'  = read
'w'  = write (overwrites)
'a'  = append
'r+' = read + write (no overwrite)
'w+' = write + read (overwrites)
'a+' = append + read
"""
